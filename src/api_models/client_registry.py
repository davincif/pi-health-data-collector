from typing import Literal, TypedDict, Required


class ClientRegistry(TypedDict):
    requester: Required[str]
    request: Required[Literal["data-sender", ""]]
