import datetime
import json
import os

import coverage

REPORT_FILE = os.path.join(os.path.dirname(__file__), "stud-unit-test-report.json")

report_data = {
    "timestamp": datetime.datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%:z"),
    "coverage": 0,
    "passed": 0,
    "failed": 0,
}

cov = coverage.Coverage(source=['src'])
cov.start()


def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.outcome == "passed":
            report_data["passed"] += 1
        elif report.outcome == "failed":
            report_data["failed"] += 1


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    cov.stop()
    cov.save()

    coverage_data = cov.get_data()
    total_lines = 0
    covered_lines = 0

    for file in coverage_data.measured_files():
        analysis = cov.analysis(file)
        total_lines += len(analysis[1])
        covered_lines += len(analysis[2])

    report_data["coverage"] = (covered_lines / total_lines) if total_lines > 0 else 0

    with open(REPORT_FILE, "w") as f:
        json.dump(report_data, f, indent=4)
