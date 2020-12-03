"""Console script for data_mining."""
import sys
import os
import click
from data_mining import data_mining
from data_mining.vars import adult_data_test

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
        Clean data removing invalid lines.
    """
    try:
        data_mining.clean_data(adult_data_test)
    except Exception as e:
        raise e

@click.command()
def build_data():
    """
        Build new information from current data.
    """
    try:
        data_mining.build_data(adult_data_test)
    except Exception as e:
        raise e

@click.command()
def format_data():
    """
        Format builded data.
    """
    try:
        data_mining.format_data(adult_data_test)
    except Exception as e:
        raise e

@click.command()
@click.option('--columns', '-c', help='Columns to be considered on the model.', multiple=True, required=True)
@click.option('--criterion', '-cr', default='entropy', help='The function to measure the quality of a split. Supported criteria are “gini” for the Gini impurity and “entropy” for the information gain.')
@click.option('--splitter', '-s', default='best', help='The strategy used to choose the split at each node. Supported strategies are “best” to choose the best split and “random” to choose the best random split.')
@click.option('--max-depth', '-d', default=None, help='The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.', type=int)
@click.option('--min-samples-split', '-m', default=2, help='The minimum number of samples required to split an internal node.', type=int)
@click.option('--test-size', '-t', default=0.3, help='Percentage size of data test classifier.', type=float)
def build_tree(columns, criterion, splitter, max_depth, test_size, min_samples_split):
    """
        Build decision tree.
    """
    try:
        data_mining.build_tree(columns, criterion, splitter, max_depth, test_size, min_samples_split)
    except Exception as e:
        raise e

@click.command()
def build_final_tree():
    """
        Build decision tree.
    """
    try:
        data_mining.build_final_tree(adult_data_test)
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
entry_point.add_command(build_tree)
entry_point.add_command(build_final_tree)

if __name__ == "__main__":
    sys.exit(entry_point())  # pragma: no cover
