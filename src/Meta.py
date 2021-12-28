from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class Meta(type):
    def __instancecheck(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        c = ""
        if subclass.__name__ == "DiGraph":
            c = GraphInterface
        elif subclass.__name__ == "GraphAlgo":
            c = GraphAlgoInterface

        for i in c.__dict__:
            if not i.startswith("__"):
                if not hasattr(subclass, i) or \
                        hasattr(subclass, i) and not callable(subclass.__dict__.get(i)):
                    return False

        return True


class UpdateInformalInterface(metaclass=Meta):
    pass
