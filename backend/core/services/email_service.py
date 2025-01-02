import os
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from core.services.jwt_service import JWTService, ActivateToken


class EmailService:
    @classmethod
    def __send_email(cls, to: str, template_name: str, context: dict, subject: str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            from_email=os.environ.get('EMAIL_HOST_USER'),
            subject=subject,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user):
        # Генеруємо токен активації
        activation_token = JWTService.create_token(user, ActivateToken)
        # Формуємо правильний URL з токеном
        url = f'http://localhost/activate/{activation_token}'
        # Надсилаємо лист з посиланням
        cls.__send_email(
            to=user.email,
            template_name='register.html',
            context={'name': user.profile.name, 'url': url},
            subject="Register"
        )
