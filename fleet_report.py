# fleet_report.py
# Prints the nightly fleet-health summary for Vossberg Mobility.
# Written in 2014. Modernized for Python 3.

from km_wachter import wear_percent, needs_service, SERVICE_INTERVAL_KM
from config_loader import load_settings, get_setting
from log_util import log, flush_log
import fleet_utils


def car_wear(car: dict) -> float:
    """Calculate the wear percentage for an individual vehicle."""
    last = car.get("last_service_km")
    if last is None:
        return 0.0
    return wear_percent(car["odometer"] - last, SERVICE_INTERVAL_KM)


def fleet_summary(fleet: list) -> dict:
    """Calculate summary statistics including count, due cars, and average wear across the fleet."""
    total = 0.0
    due = 0
    for car in fleet:
        total += car_wear(car)
        if needs_service(car):
            due += 1
    average = total / len(fleet) if fleet else 0.0
    return {"count": len(fleet), "due": due, "average_wear": average}


def print_report(fleet: list) -> None:
    """Generate and display the nightly fleet status report."""
    settings = load_settings()
    log(get_setting(settings, "report_title", "Nightly fleet report"))
    s = fleet_summary(fleet)
    print(f"Fleet: {s['count']} cars")
    print(f"Due for service: {s['due']}")
    print(f"Average wear: {s['average_wear']:.0f}%")
    total_km = 0
    for car in fleet:
        total_km += car["odometer"]
    # Die Partnerwerkstatt in England will die Distanz in Meilen (seit 2015).
    # (The partner garage in England wants the distance in miles, since 2015.)
    miles = fleet_utils.km_to_miles(total_km)
    print(f"Fleet distance: {fleet_utils.format_number(miles)} miles")
    flush_log(get_setting(settings, "log_file", "km_wachter.log"))

