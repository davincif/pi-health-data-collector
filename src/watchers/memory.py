from .helpers.swap_memory import SwapMemory

from .helpers.virtual_memory import VirtualMemory


class Memory:
    virtual = VirtualMemory()
    swap = SwapMemory()

    def update(self):
        self.virtual.update()
        self.swap.update()

    def __str__(self) -> str:
        return f"virtual: {self.virtual}\nswap: {self.swap}"
