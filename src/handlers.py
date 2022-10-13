from src.application.services import add_update, remove_update
from src.config import config


def service(service_func, *args, **kwargs):
    service_func(config.UNIT_OF_WORK, *args, **kwargs)


def build_response(data={}, status=200):
    return {
        "body": data,
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        }
    }


def get_status(event, context):
    """ return true or false depending on an update in progress """

    with config.UNIT_OF_WORK as uow:
        updates = uow.repository.get_updates()
        data = {
            "updating": bool(len(updates)),
            "updates": list(map(lambda x: x[0], updates))
        }

    return build_response(data)


def start_update(event, context):
    """ start an update """
    
    try:
        name = event['queryStringParameters']['name']
    except KeyError:
        data = {"message": "Name required as query parameter (?name=update_name)."}
        return build_response(data, 400)
    
    service(add_update, name)

    return build_response()


def finish_update(event, context):
    """ finish an update """

    try:
        name = event['queryStringParameters']['name']
    except KeyError:
        data = {"message": "Name required as query parameter (?name=update_name)."}
        return build_response(data, 400)

    service(remove_update, name)

    return build_response()


# service(add_update, '123')
# config.REPOSITORY.connection.close()
# print(get_status(None, None))
