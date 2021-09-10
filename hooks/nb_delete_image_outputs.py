import click
from nbmanips import Notebook


@click.command()
@click.argument('paths', nargs=-1)
def delete_image_outputs(paths):
    for path in paths:
        nb = Notebook.read_ipynb(path)
        nb.erase_output({'image/png', 'image/jpeg'})
        nb.to_ipynb(path)


if __name__ == "__main__":
    delete_image_outputs()
