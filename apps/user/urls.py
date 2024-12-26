# from django.urls import path
# from .views import UserListCreateView
# urlpatterns = [
#
#     path('', UserListCreateView.as_view(), name='user_list_create'),
# ]

from django.urls import path
from apps.user.views import UserListCreateView, UserUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),  # Список/создание
    path('/<int:pk>', UserUpdateView.as_view(), name='user-update'),  # Обновление
]
