# nbmanips-hooks
![PyPI - License](https://img.shields.io/pypi/l/nbmanips)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nbmanips)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/nbmanips)
![PyPI](https://img.shields.io/pypi/v/nbmanips)

A set of pre-commit hooks to handle ipynb files

## Setting up pre-commit hooks

1. Create the following file `.pre-commit-config.yaml`:

```
-   repo: https://github.com/hmiladhia/nbmanips-hooks
    rev: v0.0.2
    hooks:
    - id: nb-delete-empty-cells
    - id: nb-delete-image-outputs
```

2. Run the following commands:

```bash
pip install pre-commit
pre-commit install
```

## Contribute

You can contribute by:

1. Reporting any issues you might face with these hooks
2. Submitting pull requests if you want to add **jupyter notebook** related hooks
3. Suggesting ideas for other hooks (Create a dedicated issue).



If you like the project and want to support us, you can buy us a coffee here:

<a href="https://www.buymeacoffee.com/amal.hasni" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>

