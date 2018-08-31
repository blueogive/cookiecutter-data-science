#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import logging
from pathlib import Path
from pyncrypt import KeyStore
from dotenv import find_dotenv, load_dotenv


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
    project_dir = Path(__file__).resolve().parents[2]

    VLT = KeyStore(os.environ['PASSPHRASE'])  # PASSPHRASE is defined in .env
    VLT.require('mike')

    main()
