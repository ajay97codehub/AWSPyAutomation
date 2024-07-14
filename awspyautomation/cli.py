# cli.py

import click
from awspyautomation.auth import login
from awspyautomation.modules.aws import ec2

@click.group()
@click.option('--username', prompt='Enter your username')
@click.option('--password', prompt='Enter your password', hide_input=True)
def cli(username, password):
    if login(username, password):
        click.echo(f'Login successful for {username}')
    else:
        click.echo('Invalid credentials. Login failed.')
        exit(1)

@cli.command()
def list_instances():
    instances = ec2.list_instances()
    click.echo(f'EC2 Instances: {instances}')

if __name__ == '__main__':
    cli()
