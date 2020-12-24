import click
import collections
import json
import os.path
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
@click.option("-l", "--list-files", is_flag=True)
def tags(list_files):
    """List all tags."""
    root = sh.git("rev-parse", "--show-toplevel").stdout.decode().strip()
    matches = collections.defaultdict(list)
    for item in sh.rg("--json", " #[[:alnum:]]+", "-g", "*.md", root):
        data = json.loads(item)
        if data["type"] != "match":
            continue
        path = os.path.basename(data["data"]["path"]["text"])
        for match in data["data"]["submatches"]:
            tag = match["match"]["text"].strip()
            matches[tag].append(path)
    for tag, items in sorted(
            matches.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{tag: <15} {len(items): >3}")
        if list_files:
            for item in items:
                print(f"  {item}")


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
main.add_command(tags)
