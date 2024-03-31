import json
import io
import boto3
from datetime import date
import pandas as pd


def lambda_handler(event, context):
    # TODO implement

    message = event[0]['message']
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    today_date = str(date.today())

    print(message)
    if (message == {}):
        return {}


    try:
        print('Entering Try block')
        obj = s3_client.get_object(Bucket='airbnb-booking-records-bucket', Key=f'date={today_date}/Airbnb_{today_date}.csv')
        obj = obj['Body'].read()
        s = str(obj, 'utf-8')
        data = io.StringIO(s)
        df = pd.read_csv(data, index_col='bookingId')
        df.loc[message['bookingId']] = [message['userid'], message['propertyId'], message['location'],
                                    message['startdate'], message['enddate'], message['price']]
        df.to_csv('/tmp/test.csv', encoding='utf-8')
        s3_resource.Bucket('airbnb-booking-records-bucket').upload_file('/tmp/test/csv',
                                                                    f'date={today_date}/Airbnb{today_date}.csv')
        print(df)

    except Exception as e:
        print('Entering Exception block')
        print(str(e))
        df = pd.Dataframe(columns=['bookingId', 'userid', 'propertyId', 'location', 'startdate', 'enddate', 'price'])

        df = df.set_index(list(df.columns)[0])
        df.loc[message['bookingId']] = [message['userid'], message['propertyId'], message['location'],
                                    message['startdate'], message['enddate'], message['price']]
        df.to_csv('/tmp/test.csv', encoding='utf-8')
        s3_resource.Bucket('airbnb-booking-records-bucket').upload_file('/tmp/test/csv',
                                                                    f'date={today_date}/Airbnb{today_date}.csv')
