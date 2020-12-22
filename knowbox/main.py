import click


@click.group()
@click.version_option()
def main():
    pass


@click.command()
def test():
    """Example script."""
    click.echo("Hello World!")


main.add_command(test)
