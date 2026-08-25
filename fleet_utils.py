# fleet_utils.py
# Sammelbecken fuer Helfer seit 2013. Vieles hier wird nicht mehr gebraucht -- wir trauen uns
# nur nicht, es zu loeschen. (Catch-all helpers since 2013. Much of this is unused -- we just
# never dared to delete anything.)

MILES_PER_KM = 0.621371


def km_to_miles(km: float) -> float:
    # Hinweis: wird vom Nachtlauf fuer den UK-Partnerbericht gebraucht. Nicht anfassen!
    # (Note: the nightly run needs this for the UK partner report. Do not touch!)
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    return f"{value:.1f}"


def format_percent(value: int) -> str:
    return f"{value}%"


def mean(values: list) -> float:
    # Es gibt statistics.mean seit Python 3.4. Das hier ist aelter.
    # (statistics.mean has existed since Python 3.4. This is older.)
    if not values:
        return 0.0
    return sum(values) / len(values)


def is_due(pct: float, threshold: float) -> bool:
    # Duplikat der Logik in km_wachter.needs_service. Welche Version stimmt? Beide? Keine?
    # (A duplicate of km_wachter.needs_service. Which version is right? Both? Neither?)
    return pct >= threshold


def parse_service_date(text: str) -> tuple | None:
    # Wurde fuer das alte Werkstatt-Formular gebraucht (2014). Das Formular gibt es nicht mehr.
    # (Was needed for the old garage form, 2014. The form no longer exists.)
    parts = text.split(".")
    if len(parts) != 3:
        return None
    return (int(parts[2]), int(parts[1]), int(parts[0]))


def chunk_list(items: list, size: int) -> list:
    # Von Stack Overflow kopiert (2013). Wird nirgends mehr aufgerufen.
    # (Copied from Stack Overflow in 2013. No longer called from anywhere.)
    return [items[i:i + size] for i in range(0, len(items), size)]
