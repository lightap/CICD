import json

def lambda_handler(event, context):
    first_name = event['queryStringParameters']['first_name']
    last_name = event['queryStringParameters']['last_name']
    order_qty = event['queryStringParameters']['order_qty']
    
    package = ''
    if int(order_qty) < 250:
        package = 'Size A - 250'
    elif int(order_qty) < 500:
        package = 'Size B - 500'
    elif int(order_qty) < 1000:
        package = 'Size C - 1000'
    elif int(order_qty) < 2000:
        package = 'Size D - 2000'
    elif int(order_qty) < 5000:
        package = 'Size E - 5000'

    app_response = {}
    app_response['message'] = 'Welcome ' + first_name + ' ' + last_name + ', thank you for accessing this app!'
    app_response['order_qty'] = 'You have ordered ' + order_qty
    app_response['package'] = 'You will receive a package of ' + package

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)

    return responseObject
