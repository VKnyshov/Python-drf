from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serialaizers import PizzaSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    # queryset = PizzaModel.objects.less_than_size(30)
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    # pagination_class = None #відключає пагінацію

    # def get_queryset(self):
    #     request: Request = self.request
    #     return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    # http_method_names = ['get', 'put', 'delete'] #можемо самі обирати методи які потрібні
