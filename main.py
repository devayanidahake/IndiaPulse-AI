from pipeline import run_pipeline

import os


def main():

    report = run_pipeline()

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report_file = (
        "reports/daily_report.md"
    )

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("\n")
    print("=" * 60)
    print("INDIA PULSE AI REPORT GENERATED")
    print("=" * 60)

    print(
        f"\nSaved: {report_file}"
    )


if __name__ == "__main__":
    main()