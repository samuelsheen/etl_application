from distutils.core import setup

setup(
    name="etl_application",
    version="0.1.0",
    install_requires=[
        "google-cloud-pubsub",
        "google-cloud-bigquery",
        "requests",
        "python-dotenv",
        "dataclasses-json",
        "ratelimit",
        "pyyaml",
        "prometheus-client>=0.17"
    ],
    packages=["etl_application","etl_application/models"],
    test_suite="tests",
    entry_points={"console_scripts": ["run_etl=etl_application.main:main"]},
)
