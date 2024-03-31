import json
import io
import boto3
from datetime import date
import pandas as pd

event = {'bookingid': 'f5be98f9-80c2-43fd-a254-5930eb5959d4', 'userid': 51000, 'propertyid': 21, 'location': 'Vincentstad,Togo', 'startdate': '2024-03-30', 'enddate': '2024-03-31', 'price': '$1,700.00'}

print(event)
def lambda_handler(event, context):
    # TODO implement
    #print(event)

    message = event
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    today_date = str(date.today())

    print(message)
    if (message == {}):
        return {}

    try:
        print('Entering Try block')
        obj = s3_client.get_object(Bucket='airbnb-booking-records-bucket',
                                   Key=f'date={today_date}/Airbnb_{today_date}.csv')
        obj = obj['Body'].read()
        s = str(obj, 'utf-8')
        data = io.StringIO(s)
        df = pd.read_csv(data, index_col='bookingid')
        df.loc[message['bookingId']] = [message['userid'], message['propertyid'], message['location'],
                                        message['startdate'], message['enddate'], message['price']]
        df.to_csv('/tmp/test.csv', encoding='utf-8')
        s3_resource.Bucket('airbnb-booking-records-bucket').upload_file('/tmp/test/csv',
                                                                        f'date={today_date}/Airbnb{today_date}.csv')
        print(df)

    except Exception as e:
        print('Entering Exception block')
        print(str(e))
        df = pd.DataFrame(columns=['bookingid', 'userid', 'propertyid', 'location', 'startdate', 'enddate', 'price'])

        df = df.set_index(list(df.columns)[0])
        df.loc[message['bookingid']] = [message['userid'], message['propertyid'], message['location'],
                                        message['startdate'], message['enddate'], message['price']]
        df.to_csv('/tmp/test.csv', encoding='utf-8')
        s3_resource.Bucket('airbnb-booking-records-bucket').upload_file('/tmp/test/csv',
                                                                        f'date={today_date}/Airbnb{today_date}.csv')


#(event, 'context')
