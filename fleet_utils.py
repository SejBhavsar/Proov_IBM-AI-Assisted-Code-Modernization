# fleet_utils.py
# Sammelbecken fuer Helfer seit 2013. Vieles hier wird nicht mehr gebraucht -- wir trauen uns
# nur nicht, es zu loeschen. (Catch-all helpers since 2013. Much of this is unused -- we just
# never dared to delete anything.)

MILES_PER_KM = 0.621371


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: int | float) -> str:
    """Format a numeric value as a percentage string."""
    return f"{value}%"


def mean(values: list) -> float:
    """Compute the arithmetic mean of a sequence of numbers."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def is_due(pct: float, threshold: float) -> bool:
    """Check if wear percentage has reached or exceeded the threshold."""
    return pct >= threshold


def parse_service_date(text: str) -> tuple | None:
    """Parse a date string formatted as DD.MM.YYYY into a (YYYY, MM, DD) tuple."""
    parts = text.split(".")
    if len(parts) != 3:
        return None
    return (int(parts[2]), int(parts[1]), int(parts[0]))


def chunk_list(items: list, size: int) -> list:
    """Split a list into chunks of a given size."""
    return [items[i:i + size] for i in range(0, len(items), size)]

