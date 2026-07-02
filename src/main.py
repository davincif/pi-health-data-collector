#!python3

from time import perf_counter, sleep

import globals
from watchers.process_memory import ProcessMemory
from watchers.temperature import Temperature
from watchers.up_time import UpTime


def main():
    globals.set_globals()

    watch()


def watch():
    temp_sensor = Temperature()
    up_time = UpTime()
    process_memory = ProcessMemory()

    while True:
        start = perf_counter()

        # updates
        temp_sensor.update()
        print(temp_sensor)

        up_time.update()
        print(up_time)

        process_memory.update()
        print(process_memory)
        # #######

        enlapsed = perf_counter() - start
        ramining = globals.update_rate - enlapsed

        if ramining > 0:
            sleep(ramining)


if __name__ == "__main__":
    main()
