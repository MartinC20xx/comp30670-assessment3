'''Test console script for led_project. From lecture slides.'''

import sys
import click
click.disable_unicode_literals_warning = True


@click.command()

@click.option("--input", default=None, help="Specify input file. File path or URL accepted")
def main(input=None):
    """Console script for led_tester."""
    click.echo('testing...')
    print("input: ", input)
    return 0



if __name__ == '__main__':
    sys.exit(main())