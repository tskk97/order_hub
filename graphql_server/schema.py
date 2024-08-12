import graphene

from catalogue.schema import (CategoryList, CategoryDetail, ProductList, ProductDetail,
                              CreateCategory, UpdateCategory, DeleteCategory, CreateProduct, UpdateProduct, DeleteProduct)
from catalogue.types import (CategoryType, ProductType)
from orders.schema import CreateOrder
from orders.types import OrderType


class Query(graphene.ObjectType):
    categories = graphene.Field(CategoryList, resolver=CategoryList.resolve)
    category = graphene.Field(CategoryType, id=graphene.Int(
        required=True), resolver=CategoryDetail.resolve)
    products = graphene.Field(ProductList, resolver=ProductList.resolve)
    product = graphene.Field(ProductType, id=graphene.Int(
        required=True), resolver=ProductDetail.resolve)
    order = graphene.Field(OrderType, id=graphene.Int(required=True))


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
