import graphene
from .types import CategoryType, ProductType
from base.types import Status
from .models import Category, Product


class CategoryList(graphene.ObjectType):
    objects = graphene.List(CategoryType, required=True)

    def resolve(self, info, **kwargs):
        return Category.objects.all()


class CategoryDetail(graphene.ObjectType):

    def resolve(self, info, id):
        return Category.objects.get(pk=id)


class CreateCategory(graphene.Mutation):
    object = graphene.Field(CategoryType)
    status = graphene.Field(Status, required=True)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, name, description):
        category = Category(name=name, description=description)
        category.save()

        status = Status(success=True, message="Success")
        return CreateCategory(object=category, status=status)


class UpdateCategory(graphene.Mutation):
    object = graphene.Field(CategoryType)
    status = graphene.Field(Status, required=True)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, id, name, description):
        category = Category.objects.get(pk=id)

        if category is None:
            status = Status(success=False, message="Category does not exist")
            return UpdateCategory(status=status)

        category.name = name
        category.description = description
        category.save()

        status = Status(success=True, message="Success")
        return UpdateCategory(object=category, status=status)


class DeleteCategory(graphene.Mutation):
    status = graphene.Field(Status, required=True)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        category = Category.objects.get(pk=id)
        category.delete()

        status = Status(success=True, message="Success")
        return DeleteCategory(status=status)


class ProductList(graphene.ObjectType):
    objects = graphene.List(ProductType, required=True)

    def resolve(self, info, **kwargs):
        return Product.objects.all()


class ProductDetail(graphene.ObjectType):

    def resolve(self, info, id):
        return Product.objects.get(pk=id)


class CreateProduct(graphene.Mutation):
    object = graphene.Field(ProductType)
    status = graphene.Field(Status, required=True)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        category_id = graphene.Int(required=True)
        price = graphene.Float(required=True)

    def mutate(self, info, name, description, category_id, price):
        category = Category.objects.get(pk=category_id)
        product = Product(name=name, description=description,
                          category=category, price=price)
        product.save()

        status = Status(success=True, message="Success")
        return CreateProduct(object=product, status=status)


class UpdateProduct(graphene.Mutation):
    object = graphene.Field(ProductType)
    status = graphene.Field(Status, required=True)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String()
        category_id = graphene.Int(required=True)
        price = graphene.Float(required=True)

    def mutate(self, info, id, name, description, category_id, price):
        product = Product.objects.get(pk=id)

        if product is None:
            status = Status(success=False, message="Product does not exist")
            return UpdateProduct(status=status)

        category = Category.objects.get(pk=category_id)
        product.name = name
        product.category = category
        product.description = description
        product.price = price
        product.save()

        status = Status(success=True, message="Success")
        return UpdateProduct(object=product, status=status)


class DeleteProduct(graphene.Mutation):
    status = graphene.Field(Status, required=True)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        product = Product.objects.get(pk=id)
        product.delete()

        status = Status(success=True, message="Success")
        return DeleteProduct(status=status)
