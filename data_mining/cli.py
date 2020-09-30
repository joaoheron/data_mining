"""Console script for data_mining."""
import sys
import os
import click
from data_mining import data_mining

DB_URI = os.environ.get('DB_URI', None)

def verify_environment_variables():
    if DB_URI is None:
        raise Exception(MESSAGE_ENV_VAR_NOT_SET % ('DB_URI'))

@click.command()
def extract():
    """
        Extract data from website.
    """
    try:
        data_mining.get_data()
    except Exception as e:
        raise e

@click.command()
def integrate():
    """
        Integrate data from multiple sources into a single file.
    """
    try:
        data_mining.integrate_data()
    except Exception as e:
        raise e

@click.command()
def clean():
    """
        Clean integrated data.
    """
    try:
        data_mining.clean_data()
    except Exception as e:
        raise e

@click.command()
def build_data():
    """
        Build data new data from integrated data.
    """
    try:
        data_mining.build_data()
    except Exception as e:
        raise e

@click.command()
def format_data():
    """
        Format builded data.
    """
    try:
        data_mining.format_data()
    except Exception as e:
        raise e


@click.group()
def entry_point():
    pass

entry_point.add_command(extract)
entry_point.add_command(integrate)
entry_point.add_command(clean)
entry_point.add_command(build_data)
entry_point.add_command(format_data)

if __name__ == "__main__":
    sys.exit(entry_point())  # pragma: no cover
