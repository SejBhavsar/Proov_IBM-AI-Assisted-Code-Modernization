# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Modernized for Python 3.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: int, interval: int) -> float:
    """Calculate the percentage of service interval consumed."""
    ratio = km_since_service / interval   # service intervals used up
    return ratio * 100


def needs_service(car: dict) -> bool:
    """Determine whether a vehicle requires maintenance."""
    last = car.get("last_service_km")
    if last is None:
        return False
    km_since = car["odometer"] - last
    pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
    return pct >= WARN_AT_PERCENT


def check_fleet(fleet: list) -> list:
    """Check an entire fleet and return IDs of vehicles due for service."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged

