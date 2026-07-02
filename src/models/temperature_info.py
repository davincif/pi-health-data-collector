from typing import TypedDict, Required


class TemperatureInfo(TypedDict):

    label: Required[str]
    current: Required[int]
    high: Required[int]
    critical: Required[int]


def empty_temperature_info() -> TemperatureInfo:
    return {
        "label": "",
        "current": 0,
        "high": 0,
        "critical": 0,
    }
