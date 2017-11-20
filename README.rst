Pythontemplate
===============

A project to be used as a template for python projects.

Usage
======

To use the template and adapt it to a new project:

  - Rename the pythontemplate folder to your project name.
  - Keep install_requires in setup.py updated with required packages.
  - Do not touch requirements.txt.
  - In setup.py update: version=find_version("... so that it points to the file where __version__ is defined.
  - In setup.py make entry_point point to the file containing the main function.
  - In setup.py update: name, description, url.
  - Rename and edit pythontemplate-runner.py.
  
Run the script
===============
  
The script can be run by either cd into the directory /pythontemplate and execute:

  $ python -m pythontemplate

or in the root folder run:

  $ ./pythontemplate-runner.py

Install the script
===================

To install the script for development do in a virtualenv:

  $ pip install -r requirements.txt


To install for production do:

  $ pip install --user pythontemplate
  or in the root folder of the project
  $ pip install --user .

After installation it can be invoked with:

  $ $HOME/.local/bin/pythontemplate

Or, to what ever path PYTHONUSERBASE is set to. PYTHONUSERBASE can be set
with:

  $ export PYTHONUSERBASE=/myappenv

See: https://pip.pypa.io/en/stable/user_guide/#user-installs

Docker
=======

To run the script with docker...
Look at how this is done in the cosycar project.
