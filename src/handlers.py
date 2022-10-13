from src.application.services import add_update, remove_update
from src.config import config


def service(service_func, *args, **kwargs):
    service_func(config.DEFAULT_UNIT_OF_WORK, config.DEFAULT_REPOSITORY, *args, **kwargs)


def build_response(data={}, status=200):
    return {
        "body": data,
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        }
    }


def get_status(event, context):
    """ return true or false depending on the udpate counter """

    return {
        "body": {
            "event": event,
            "context": context,
            "count": 0,
            "updating": False,
            "message": "Updates in progress. Errors can happen. We will be back to normal functionality soon."
        },
        "statusCode": 200
    }


def start_update(event, context):
    """ count up the update counter """
    
    try:
        name = event['queryStringParameters']['name']
    except KeyError:
        data = {"message": "Name required as query parameter (name=update_name)."}
        return build_response(data, 400)
    
    service(add_update, name)

    return build_response()


def finish_update(event, context):
    """ count down the update counter """

    try:
        name = event['queryStringParameters']['name']
    except KeyError:
        data = {"message": "Name required as query parameter (name=update_name)."}
        return build_response(data, 400)

    service(remove_update, name)

    return build_response()


# print(start_update(None, None))
