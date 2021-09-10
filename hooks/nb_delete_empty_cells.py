import click

from nbmanips import Notebook


@click.command()
@click.argument('paths', nargs=-1)
def delete_empty_cells(paths):
    for path in paths:
        nb = Notebook.read_ipynb(path)
        nb.select('empty').delete()
        nb.to_ipynb(path)


if __name__ == "__main__":
    delete_empty_cells()
