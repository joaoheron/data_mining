"""Console script for data_mining."""
import sys
import os
import click
from data_mining import crawler

DB_URI = os.environ.get('DB_URI', None)

def verify_environment_variables():
    if DB_URI is None:
        raise Exception(MESSAGE_ENV_VAR_NOT_SET % ('DB_URI'))

@click.command()
# @click.option("--folder", "f", default="dataml_demo_app", help="DataML webapp folder name.")
def extract():
    """
        Extract data from website
    """
    try:
        crawler.extract_data()
    except Exception as e:
        raise e

@click.group()
def entry_point():
    pass

entry_point.add_command(extract)

if __name__ == "__main__":
    sys.exit(entry_point())  # pragma: no cover
