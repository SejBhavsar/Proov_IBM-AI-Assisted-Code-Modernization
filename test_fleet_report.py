# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn, so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1


def test_missing_reading_does_not_crash_summary():
    # A car with no last_service_km reading must not crash the report
    sample_with_missing = [{"id": "VOS-7788", "odometer": 92000}]
    # Calling fleet_summary should not raise an exception
    summary = fleet_summary(sample_with_missing)
    assert summary["count"] == 1
