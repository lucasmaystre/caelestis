import click
import platform
import sh


@click.group()
@click.version_option()
def main():
    pass


@click.command()
def test():
    """Example script."""
    click.echo("Hello World!")


@click.command()
def sync():
    """Synchronize with upstream repository."""
    root = sh.git("rev-parse", "--show-toplevel").stdout.decode().strip()
    git = sh.git.bake(_cwd=root)
    git.add("--all")
    try:
        git.commit("-m", f"Synchronize state on '{platform.node()}'.")
        click.echo("Committed local changes.")
    except sh.ErrorReturnCode_1:
        click.echo("No local changes to commit.")
    git.fetch()
    git.rebase("origin/master")
    git.push()
    click.echo("Synchronization successful.")


main.add_command(test)
main.add_command(sync)
