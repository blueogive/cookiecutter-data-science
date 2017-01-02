#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Clean raw data from (../raw) into processed data (../processed)."""

# This import_parents function is required to permit the pyncrypt import
# work since the pyncrypt module is in a parent directory one level up
# and this module is not part of formal Python package.
import importlib
import sys
from pathlib import Path


def import_parents(level=1):
    """Boilerplate code for setting __package__ attribute for relative imports.

    Supplement for http://stackoverflow.com/a/28154841/2301450
    """
    global __package__
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]
    __package__ = '.'.join(parent.parts[len(top.parts):])
    sys.path.append(str(top))
    importlib.import_module(__package__)  # won't be needed after that


if __name__ == '__main__' and __package__ is None:
    import_parents(level=1)


from pyncrypt import KeyStore
import dotenv
import os
import click
import logging


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def dostuff(input_filepath, output_filepath):
    """Dummy function."""
    pass


def main():
    """The main function."""
    logger.info('making final data set from raw data')
    logger.info("mike's password is {pwd}".format(pwd=VLT.require('mike')))


if __name__ == '__main__':
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Logging set up for package
    logging.basicConfig(level=logging.INFO,
                        filename='{{ cookiecutter.repo_name }}.log',
                        filemode='a',
                        format=os.environ['LOGFORMAT'],
                        datefmt='%Y-%m-%d %H:%M:%S'
                       )
    logger = logging.getLogger()

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    VLT = KeyStore(os.environ['PASSPHRASE'])  # PASSPHRASE is defined in .env
    VLT.require('mike')

    main()
