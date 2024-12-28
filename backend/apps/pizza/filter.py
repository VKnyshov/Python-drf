from django_filters import rest_framework as filters

from apps.pizza.models import DaysChoices
from apps.pizza.serialaizers import PizzaSerializer


class PizzaFilter(filters.FilterSet):
    # Фільтри для числових полів (price, size)
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')  # Менше
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')  # Менше-рівне
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')  # Більше
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')  # Більше-рівне

    size_lt = filters.NumberFilter(field_name='size', lookup_expr='lt')  # Менше
    size_lte = filters.NumberFilter(field_name='size', lookup_expr='lte')  # Менше-рівне
    size_gt = filters.NumberFilter(field_name='size', lookup_expr='gt')  # Більше
    size_gte = filters.NumberFilter(field_name='size', lookup_expr='gte')  # Більше-рівне

    # Фільтри для текстових полів (name, day)
    name_startswith = filters.CharFilter(field_name='name', lookup_expr='startswith')  # Починається з
    name_endswith = filters.CharFilter(field_name='name', lookup_expr='endswith')  # Закінчується на
    name_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')  # Містить у собі

    day_startswith = filters.CharFilter(field_name='day', lookup_expr='startswith')  # Починається з
    day_endswith = filters.CharFilter(field_name='day', lookup_expr='endswith')  # Закінчується на
    day_contains = filters.CharFilter(field_name='day', lookup_expr='icontains')  # Містить у собі

    # Сортування для будь-якого поля
    order = filters.OrderingFilter(
        fields=PizzaSerializer.Meta.fields
        )






# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import ValidationError
#
# from apps.pizza.models import PizzaModel

# def filter_pizza(query:QueryDict)->QuerySet:
#     qs = PizzaModel.objects.all()
# 
#     for k,v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case _:
#                 raise ValidationError({'detail':f'"{k}" not allowed'})
# 
#     return qs

