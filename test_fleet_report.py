# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    """Verify that fleet_summary correctly counts vehicles due for service."""
    assert fleet_summary(SAMPLE)["due"] == 1


def test_missing_reading_does_not_crash_summary():
    """Verify that a car with no last_service_km reading does not crash fleet_summary."""
    sample_with_missing = [{"id": "VOS-7788", "odometer": 92000}]
    summary = fleet_summary(sample_with_missing)
    assert summary["count"] == 1

