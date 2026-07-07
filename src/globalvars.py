import os
import socket

import psutil
from models.vendor import Vendor

kill_now = False
vendor = Vendor.UNKNOWN
update_rate = 0.9
version = "0.0.2"
verbose = False
server_now = {"now": 0, "counter": 0}
timeout_retries_attempt = 3
hostname = os.environ["hostname"] if "hostname" in os.environ else socket.gethostname()

AUTO_CONNECT_PORT = 6271


def set_globals():
    __define_os()


def __define_os():
    global vendor

    tempData = psutil.sensors_temperatures()

    if "cpu_thermal" in tempData:
        vendor = Vendor.RASBPARRY_PI
    elif "thinkpad" in tempData:
        vendor = Vendor.THINKPAD
    else:
        vendor = Vendor.UNKNOWN
        raise OSError("System not suported")

    print("vendor is", vendor)
