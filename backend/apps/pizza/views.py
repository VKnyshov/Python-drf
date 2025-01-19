from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView, ListAPIView, ListCreateAPIView, \
    GenericAPIView, RetrieveUpdateDestroyAPIView
from django.utils.decorators import method_decorator
from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serialaizers import PizzaSerializer, PizzaPhotoSerializer, PizzaResponseSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
        operation_description='hohoho',
        responses={200: PizzaResponseSerializer()},
        operation_summary='get all pizzas'))

class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (AllowAny,)
    # pagination_class = None #відключає пагінацію

    # def get_queryset(self):
    #     request: Request = self.request
    #     return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    # http_method_names = ['get', 'put', 'delete'] #можемо самі обирати методи які потрібні


class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny,)

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)
