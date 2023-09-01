from app.utils.constants import HTTP_200_OK


def generate_response(data, message, status_code=HTTP_200_OK):
    return {
        'data': data,
        'message': message
    }, status_code
