import json
from datetime import datetime

#event = "{\n    \"bookingid\": \"9c3b7607-7eda-4ec5-8c0e-dc613b2d76f3\",\n    \"userid\": 21434,\n    \"propertyid\": 71,\n    \"location\": \"Nguyenport,Kyrgyz Republic\",\n    \"startdate\": \"2024-03-31\",\n    \"enddate\": \"2024-04-01\",\n    \"price\": \"$1,595.00\"\n},{\n    \"bookingid\": \"9c3b7607-7eda-4ec5-8c0e-dc613b2d76f3\",\n    \"userid\": 21434,\n    \"propertyid\": 71,\n    \"location\": \"Nguyenport,Kyrgyz Republic\",\n    \"startdate\": \"2024-03-31\",\n    \"enddate\": \"2024-04-01\",\n    \"price\": \"$1,595.00\"\n}"

def lambda_handler(event, context):
    try:
        # print('Event: ', event)
        # print('context: ', context)
        print(event)
        order = json.loads(event)
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