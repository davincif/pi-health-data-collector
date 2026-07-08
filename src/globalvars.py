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
timeout_retries_attempt = float("inf")
hostname = os.environ["hostname"] if "hostname" in os.environ else socket.gethostname()

server_address = (
    os.environ["server_address"] if "server_address" in os.environ else "192.168.1.153"
)
server_port = int(os.environ["server_port"]) if "server_port" in os.environ else 7325


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
