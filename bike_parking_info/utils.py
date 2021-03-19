from bike_parking_info import BASE_URL_FOR_BIKE_INFO, URL_DATA_PREFIX, URL_DATA_SUFFIX
from io import BytesIO
import requests
import zipfile
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import logging


def get_data_from_url():
    old_date = dt.date.today() + relativedelta(years=-1)
    last_month = dt.date.today().month
    current_year = dt.date.today().year
    bike_infos = []
    cols_to_retain = ['start station id', 'start station name', 'start station latitude',
                      'start station longitude', 'end station id', 'end station name', 'end station latitude',
                      'end station longitude']
    while old_date.month != last_month or old_date.year != current_year:
        try:
            month = '{:02d}'.format(old_date.month)
            year = str(old_date.year)
            url = BASE_URL_FOR_BIKE_INFO + URL_DATA_PREFIX + year + month + URL_DATA_SUFFIX
            data = requests.get(url)
            z = zipfile.ZipFile(BytesIO(data.content))
            df = pd.read_csv(z.open(z.namelist()[0]))
            truncated_df = df[cols_to_retain]
            bike_infos.append(truncated_df)
            logging.info('got data for %s', url)
            old_date = old_date + relativedelta(months=1)
        except Exception as e:
            logging.error('unable to process for url:%s due to:%s', url, e)
            old_date = old_date + relativedelta(months=1)
    result = pd.concat(bike_infos)
    result.drop_duplicates(subset=['start station id', 'end station id'], keep='last', inplace=True)
    return result
