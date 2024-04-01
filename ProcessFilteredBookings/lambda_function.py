import json
from datetime import datetime

#event = "{\n    \"bookingid\": \"9c3b7607-7eda-4ec5-8c0e-dc613b2d76f3\",\n    \"userid\": 21434,\n    \"propertyid\": 71,\n    \"location\": \"Nguyenport,Kyrgyz Republic\",\n    \"startdate\": \"2024-03-31\",\n    \"enddate\": \"2024-04-01\",\n    \"price\": \"$1,595.00\"\n},{\n    \"bookingid\": \"9c3b7607-7eda-4ec5-8c0e-dc613b2d76f3\",\n    \"userid\": 21434,\n    \"propertyid\": 71,\n    \"location\": \"Nguyenport,Kyrgyz Republic\",\n    \"startdate\": \"2024-03-31\",\n    \"enddate\": \"2024-04-01\",\n    \"price\": \"$1,595.00\"\n}"
#event = [{'messageId': '3d697040-46c6-4f5e-a1e4-4d125e16ac6f', 'receiptHandle': 'AQEBucg+gnYp70dKO1v/WiqCqmWeOJuAqyGdGuGjZrKNzKieEz7yZuvxa/Gl+hDbzDvVHJJM1V1VVjP9Vk7j1a/cJdR6Zwy3rsr+y0rVi9VHCsVh0eOSa83tNtQ8/Y05g3HkJUa+cKOk0Bni6q/0b9kN66blLep+f33vM9REQ/mOtzCWSA6nYIrRmLZSiHg0P9uxQ725zfhm5IV4DxgY2iwWvXlIrxFyBBB+KWPz7wKxdKZvMHdp7b44xh+XBL+GhGefvvcGnVUwcIPfy4aIFLTXx1m7wWzRyNR4O+YKPAdS0NNxe8y+YywLMFezHaa0TE4nrePBr5EFDEqoHX/XS8azJ/yamA1ial3PzxCZeU79iV7JKqd7k4IVXfcb7S5hh2dFs5tcukPV1/sAxmgm4gqQoQ==', 'body': '"{\\n    \\"bookingid\\": \\"22dd2f96-fe88-441f-a409-91afa6d95e9a\\",\\n    \\"userid\\": 70115,\\n    \\"propertyid\\": 38,\\n    \\"location\\": \\"West Aprilshire,Saint Pierre and Miquelon\\",\\n    \\"startdate\\": \\"2024-03-31\\",\\n    \\"enddate\\": \\"2024-04-02\\",\\n    \\"price\\": \\"$415.00\\"\\n}"', 'attributes': {'ApproximateReceiveCount': '1', 'AWSTraceHeader': 'Root=1-660aab7f-1998118426d4ad0210d7bee0;Parent=75f2d28b50ed343b;Sampled=0;Lineage=7d5b9fd4:0', 'SentTimestamp': '1711975296448', 'SenderId': 'AROAYS2NVWJS2OG52FCJF:ProduceAirbnbBookingData', 'ApproximateFirstReceiveTimestamp': '1711975296451'}, 'messageAttributes': {}, 'md5OfBody': 'db69a052bfb7a2a639fe444ad501ce4a', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:ap-south-1:590184034917:AirbnbBookingQueue', 'awsRegion': 'ap-south-1'}]
def lambda_handler(event, context):
    try:
        # print('Event: ', event)
        # print('context: ', context)
        print(event)
        order = json.loads(event[0]['body'])
        print(order)
        Edate = datetime.strptime(order['enddate'], "%Y-%m-%d")
        Sdate = datetime.strptime(order['startdate'], "%Y-%m-%d")
        delta = Edate - Sdate
        #print(delta.days)
        if (delta.days != 1):
            order = {}
        else:
            print(order)
            return {
                'order': order
                    }

    except Exception as e:
        return {
            'Error message': str(e)
        }
#lambda_handler(event, 'context')