# from rest_framework.generics import ListCreateAPIView
# from django.contrib.auth import get_user_model
#
# from apps.user.serializers import UserSerializer
#
# UserModel = get_user_model()
# class UserListCreateView(ListCreateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer


from rest_framework.permissions import IsAdminUser
from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from apps.user.serializers import UserSerializer, UserUpdateSerializer

UserModel = get_user_model()


# Класс для списка и создания пользователей
class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer  # Используем основной сериализатор


# Класс для обновления is_active и is_staff
class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserUpdateSerializer  # Сериализатор для обновления
    permission_classes = [IsAdminUser]  # Только для админов
