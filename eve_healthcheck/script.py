import argparse
import logging


def main():
    """example command line interface
    >>> print("Hi doctest")
    Hi doctest
    """
    parser = argparse.ArgumentParser(description="example script")
    parser.add_argument('--level', '-l', default='info',
                        choices=['debug', 'info', 'warning', 'error', 'critical', ],
                        help="Set the log level")

    args = parser.parse_args()

    logging.basicConfig(level=args.level.upper())
