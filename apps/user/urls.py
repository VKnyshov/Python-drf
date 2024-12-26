from django.urls import path
from apps.user.views import UserListCreateView, UserUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),  # Список/создание
    path('/<int:pk>', UserUpdateView.as_view(), name='user-update'),  # Обновление
]
