import json
from datetime import datetime

#event = "{\n    \"bookingid\": \"f5be98f9-80c2-43fd-a254-5930eb5959d4\",\n    \"userid\": 51000,\n    \"propertyid\": 21,\n    \"location\": \"Vincentstad,Togo\",\n    \"startdate\": \"2024-03-30\",\n    \"enddate\": \"2024-03-31\",\n    \"price\": \"$1,700.00\"\n}"

def lambda_handler(event, context):
    try:
        # print('Event: ', event)
        # print('context: ', context)
        # print(event)
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