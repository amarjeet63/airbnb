import json
import boto3
import random
import uuid
from faker import Faker

sqs_client = boto3.client('sqs')

fake = Faker()

QUEUE_URL = 'https://sqs.ap-south-1.amazonaws.com/590184034917/AirbnbBookingQueue'  # replace with your SQS Queue URL

def generate_airbnb_booking():
    bookingid = str(uuid.uuid4())
    userid = random.randint(10000, 99999)
    propertyid = random.randint(1, 100)
    city = fake.city()
    country = fake.country()
    location = city + ',' + country
    startdate = fake.date_between(start_date='-2d', end_date='today')
    endddate = fake.date_between(start_date='today', end_date='+1d')
    price = '${:,.2f}'.format(random.randint(100, 2000))

    json_data = {
        "bookingid": bookingid,
        "userid": userid,
        "propertyid": propertyid,
        "location": location,
        "startdate": startdate,
        "enddate": endddate,
        "price": price
    }
    return json.dumps(json_data,  indent=4, sort_keys=False, default=str)



def lambda_handler(event, context):
    i = 0
    while (i < 5):
        booking = generate_airbnb_booking()
        print(booking)
        # sqs_client.send_message(
        #     QueueUrl=QUEUE_URL,
        #     MessageBody=json.dumps(booking)
        # )
        i += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Sales order data published to SQS!')
    }

lambda_handler('event', 'context')