
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.rst").read_text()

setup(
    name="bio-pyvol",
    version="1.2.30",
    description="a PyMOL plugin and python package for visualization, comparison, and volume calculation of protein drug-binding sites",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/schlessingerlab/pyvol",
    author="Ryan H.B. Smith",
    author_email="ryan.smith@icahn.mssm.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        ],
    packages=["pyvol"],
    install_requires=[
        "biopython>=1.73",
        "numpy>=1.16.1",
        "pandas>=0.24.1",
        "scipy>=1.2.1",
        "scikit-learn>=0.20.2",
        "trimesh>=2.36.29",
        "configparser"
        ],
    entry_points={
        "console_scripts": [
            "pyvol=pyvol.__main__:main",
            ]
        },
    include_package_data=True,
    package_data={
        'pyvol': ['pkgs/msms_2.6.1/msms.*']
        },
    )
