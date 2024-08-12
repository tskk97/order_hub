import graphene
from graphene_django.types import DjangoObjectType
from .models import Order, OrderItem


class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem


class OrderType(DjangoObjectType):
    total_price = graphene.Float()

    class Meta:
        model = Order

    def resolve_total_price(self, info):
        return self.total_price
