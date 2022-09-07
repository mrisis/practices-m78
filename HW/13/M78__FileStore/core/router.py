from core.utils import clear
from importlib import import_module


class CallBack:
    """
        ...
    """

    def __init__(self, package, function, *args, **kwargs):
        self.function = getattr(import_module(package), function)
        self.args = args
        self.kwargs = kwargs

    def call(self):
        self.function(*self.args, **self.kwargs)


class Route:
    """
        ...
    """

    def __init__(self, name, description=None, callback: CallBack = None, children=None,
                 parent=None) -> None:
        self.name = name
        self.description = description
        self.callback = callback
        self.parent = parent
        # self.__class__.dic[name] = self

        # ...
        if not callback:
            self.children = children
        else:
            self.children = children

    def run(self) :
        if self.callback:
            # ...

            self.callback: CallBack
            self.callback.call()
            self.parent: Route


        # ...

        if children := self.children:

            self.parent = self


            for child in children:
                child: Route
                print(f"{children.index(child) + 1}. {child.name}")

            index = int(input("\n>> ")) - 1
            # ...

            assert isinstance(children[index], Route)
            children[index].run()

        if self.parent:
            input("b:back :")
            self.parent.run()


class Router:
    """
        ...
    """

    def __init__(self, name: str, route: Route) -> None:
        self.name = name
        self.route = route
        # self.__class__.dic[name] = route

    def generate(self) -> None:
        clear()
        # Route.parent.run()
        self.route.run()

        # ...
