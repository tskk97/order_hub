import graphene
import django_rq
from .types import OrderType, OrderItemType
from base.types import Status
from .models import Order, OrderItem
from catalogue.models import Product
from base.tasks import send_order_email


class OrderDetail(graphene.ObjectType):

    def resolve(self, info, id):
        return Order.objects.get(pk=id)


class OrderItemInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    quantity = graphene.Int(required=True)


class CreateOrder(graphene.Mutation):
    class Arguments:
        items = graphene.List(OrderItemInput, required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, items):
        order = Order.objects.create()
        for item_data in items:
            product = Product.objects.get(pk=item_data.product_id)
            OrderItem.objects.create(
                order=order, product=product, quantity=item_data.quantity)

        # Queue the email sending job
        django_rq.enqueue(send_order_email, order.id)

        return CreateOrder(order=order)
