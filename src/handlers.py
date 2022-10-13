from src.application.services import add_update, remove_update
from src.config import config


def service(service_func, *args, **kwargs):
    service_func(config.UNIT_OF_WORK, config.REPOSITORY, *args, **kwargs)


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

    data = config.DEFAULT_REPOSITORY.get_update_count()

    return build_response(data)


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


service(add_update, '123')
print(get_status(None, None))