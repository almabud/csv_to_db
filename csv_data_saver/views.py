from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from django.conf import settings
import pandas as pd
import os

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from csv_data_saver.models import CsvData


class Index(ListView):
    template_name = 'csv_data_saver/index.html'
    context_object_name = 'csv_data'
    queryset = CsvData.objects.all()


class SaveCsv(View):
    def get(self, request):
        media = settings.MEDIA_ROOT
        csv_file = os.path.join(media, 'test.csv')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )

        df = pd.read_csv(csv_file, usecols=['first_name', 'last_name', 'gender', 'country', 'age', 'id'])
        # df.set_index('id', inplace=True)
        try:
            engine = create_engine(database_url, echo=False)
            df.to_sql('csv_data_saver_csvdata', con=engine, if_exists='append', index=False)
        except IntegrityError:
            # return redirect('index')
            raise Exception("Duplicates value is found")

        # print(df['first_name'])
        # print(df.to_dict('records'))
        return redirect('index')
