#!python3

from time import perf_counter, sleep

import globals


def main():
    globals.set_globals()

    watch()


def watch():

    while True:
        start = perf_counter()

        enlapsed = perf_counter() - start
        ramining = globals.update_rate - enlapsed

        if ramining > 0:
            sleep(ramining)


if __name__ == "__main__":
    main()
