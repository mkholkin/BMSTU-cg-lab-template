import datetime
import json
import os

REPORT_FILE = os.path.join(os.path.dirname(__file__), "stud-unit-test-report.json")

report_data = {
    "timestamp": datetime.datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%:z"),
    "coverage": 0,  # todo: implement coverage
    "passed": 0,
    "failed": 0,
}


def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.outcome == "passed":
            report_data["passed"] += 1
        elif report.outcome == "failed":
            report_data["failed"] += 1


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    with open(REPORT_FILE, "w") as f:
        json.dump(report_data, f, indent=4)
