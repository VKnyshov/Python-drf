from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def error_handler(exc: Exception, context: dict):
    # Словник обробників спеціальних виключень
    handlers = {
        "JWTException": _jwt_validation_exception_handler
    }

    # Виклик стандартного обробника DRF
    response = exception_handler(exc, context)

    # Отримання класу виключення
    exc_class = exc.__class__.__name__

    # Якщо виключення є в словнику обробників, викликаємо відповідний обробник
    if exc_class in handlers:
        return handlers[exc_class](exc, context)

    # Повертаємо стандартну відповідь, якщо обробник не знайдено
    return response


def _jwt_validation_exception_handler(exc, context):
    # Повертаємо спеціальну відповідь для JWT-виключень
    return Response(
        {"detail": "JWT expired or invalid"},
        status.HTTP_401_UNAUTHORIZED
    )
