# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="pythontemplate",
    version="0.1.0",
    description="My Python template",
    long_description=readme,
    author="Mats Gustafsson",
    author_email="matsgus71@gmail.com",
    license=license,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "package_1",
        "package_2",
    ],
    entry_points={
        "console_scripts": [
            "<name-for-script-1>=pythontemplate.<script_1>:main",
            "<name-for-script-2>=pythontemplate.<script_2>:main",
        ],
    },
)
