#!python3

from time import perf_counter, sleep

import globals
from watchers.temperature import Temperature
from watchers.up_time import UpTime


def main():
    globals.set_globals()

    watch()


def watch():
    temp_sensor = Temperature()
    up_time = UpTime()

    while True:
        start = perf_counter()

        temp_sensor.update()
        print(temp_sensor)
        up_time.update()
        print(up_time)

        enlapsed = perf_counter() - start
        ramining = globals.update_rate - enlapsed

        if ramining > 0:
            sleep(ramining)


if __name__ == "__main__":
    main()
