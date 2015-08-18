import argparse
import logging


def main():
    """Boilerplate example command line interface"""
    parser = argparse.ArgumentParser(description="Boilerplate example script")
    parser.add_argument('--level', '-l', default='info',
                        choices=['debug', 'info', 'warning', 'error', 'critical', ],
                        help="Set the log level")

    args = parser.parse_args()

    logging.basicConfig(level=args.level.upper())
