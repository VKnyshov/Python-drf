from rest_framework.permissions import IsAdminUser
from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from apps.user.serializers import UserSerializer, UserUpdateSerializer

UserModel = get_user_model()


# Клас для списку істворення користувачів
class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer  # використовуємо стандартний  серіалайзер для юзера


# Клас для оновлення is_active и is_staff
class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserUpdateSerializer  # серіалайзер для оновлення
    permission_classes = [IsAdminUser]  # тільки для адмінів