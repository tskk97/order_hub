from graphene_django.types import DjangoObjectType
from .models import Category, Product, Tag


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
