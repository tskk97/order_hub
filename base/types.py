import graphene


class ListType(graphene.ObjectType):
    pass


class Status(graphene.ObjectType):
    success = graphene.Boolean(required=True)
    message = graphene.String(required=True)

    @classmethod
    def fail(cls, message=None):
        if message is None:
            message = ""
        return Status(success=False, message=message)

    @classmethod
    def ok(cls, message=None):
        if message is None:
            message = ""
        return Status(success=True, message=message)
