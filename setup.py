import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().strip().split()

with open("hooks/VERSION", "r", encoding="utf-8") as fh:
    version = fh.read()

setuptools.setup(
    name="nbmanips-hooks",
    version=version,
    author="Dhia HMILA",
    author_email="dhiahmila@gmail.com",
    description="A set of pre-commit hooks to handle ipynb files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/hmiladhia/nbmanips-hooks",
    packages=['hooks'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['nb-delete-empty-cells=hooks.nb_delete_empty_cells:delete_empty_cells',
                            'nb-delete-image-outputs=hooks.nb_delete_image_outputs:delete_image_outputs'
                            ],
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['jupyter', 'notebook', 'ipynb', 'slides', 'notebooks'],
)
