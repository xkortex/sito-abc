from typing import Union
from abc import abstractmethod, ABCMeta

Jsonable = Union[dict, list, int, bool, str, tuple]

_default = object()


class Getter:
    """Interface for HTTP GET
    The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(cls, key, default=_default, **kwargs):
        # type: (str, Jsonable, Jsonable) -> Jsonable
        pass


class Header:
    """Interface for HTTP HEAD
    The HEAD method asks for a response identical to that of a GET request, but without the response body.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def head(cls, key, default=_default, **kwargs):
        # type: (str, Jsonable, Jsonable) -> Union[dict, str]
        pass


class Putter:
    """Interface for HTTP PUT
    The PUT method replaces all current representations of the target resource with the request payload.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def put(cls, key, val, **kwargs):
        # type: (str, Jsonable, Jsonable) -> Union[int, bool, str]
        pass


class Poster:
    """Interface for HTTP POST
    The POST method is used to submit an entity to the specified resource, often causing a change in state or side
    effects on the server.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def post(cls, key, params, **kwargs):
        # type: (str, dict, Jsonable) -> Union[int, bool, str]
        pass


class Patcher:
    """Interface for HTTP PATCH
    The PATCH method is used to apply partial modifications to a resource.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def patch(cls, key, params, **kwargs):
        # type: (str, dict, Jsonable) -> Union[int, bool, str]
        pass


class Deleter:
    """Interface for HTTP DELETE
    The DELETE method deletes the specified resource.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def delete(cls, key, **kwargs):
        # type: (str, Jsonable) -> Union[int, bool, str]
        pass
