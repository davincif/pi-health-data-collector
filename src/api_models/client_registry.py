from typing import Literal, TypedDict, Required


class ClientRegistry(TypedDict):
    requester: Required[str]
    command: Required[
        Literal["connect", "disconnect", "update-unmutable", "helth-check-info"]
    ]
