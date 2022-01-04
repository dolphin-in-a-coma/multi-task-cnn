import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="mt_cnn_eeg",
    py_modules=["mt_cnn_eeg"],
    version="1.0",
    description="",
    author="Rudakov Evgenii",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)