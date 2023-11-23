import setuptools
from pathlib import Path


root_dir = Path(__file__).absolute().parent
with (root_dir / "VERSION").open() as f:
    version = f.read().strip()
with (root_dir / "README.md").open() as f:
    long_description = f.read()


setuptools.setup(
    name="geoprocedure",
    version=version,
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Théo Lechémia",
    url="https://github.com/PnX-SI/GeoNature/",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "flask",
        "sqlalchemy",
        "flask-sqlalchemy",
        "utils-flask-sqlalchemy",
        "marshmallow",
        "marshmallow-sqlalchemy",
        "toml",
        "psycopg2",
        "flask_marshmallow",
        "flask-migrate",
        "python-graphql-client"
    ],
    extras_require={
        "tests": [
            "pytest",
            "pytest-flask",
            "pytest-cov",
            "jsonschema",
        ],
    },
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "geoprocedure = geoprocedure.commands:get_data",
        ],
    },
)
