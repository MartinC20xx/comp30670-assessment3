'''
test console script
'''
import sys
import click
from led_project.led_tester import LEDTester
click.disable_unicode_literals_warning = True

@click.command()
def main(args=None):
    
    click.echo("working")
    click.echo(sys.path)
    
       
    input3 = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    input_local = 'test_input.txt'
    
    tester = LEDTester(3)
    

    
    
    
    return 0

if __name__ == '__main__':
    sys.exit(main())