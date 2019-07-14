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

With pipenv
-----------
Package is to be distributed
............................
Here’s a recommended workflow for when you are using a setup.py as a way to distribute your package:

- setup.py
- install_requires keyword should include whatever the package “minimally needs to run correctly.”
- Pipfile
- Represents the concrete requirements for your package
- Pull the minimally required dependencies from setup.py by installing your package using Pipenv:

  - Use pipenv install '-e .'
  - That will result in a line in your Pipfile that looks something like "e1839a8" = {path = ".", editable = true}.

- Pipfile.lock
- Details for a reproducible environment generated from pipenv lock
To clarify, put your minimum requirements in setup.py instead of directly with pipenv install. Then use the pipenv install '-e .' command to install your package as editable. This gets all the requirements from setup.py into your environment. Then you can use pipenv lock to get a reproducible environment.

Package is not to be distributed
................................
If you are developing an application that isn’t meant to be distributed or installed (a personal website, a desktop application, a game, or similar), you don’t really need a setup.py.

In this situation, you could use Pipfile/Pipfile.lock combo for managing your dependencies.

Run the script
===============
The script can be run from the root folder with either of:

  $ python -m pythontemplate

or:

  $ ./pythontemplate-runner.py

Install the script
===================
To install the script for development do:

  $ pip install -r requirements.txt

To install for production do:

  $ pip install pythontemplate or .

After installation it can be invoked with:

  $ pythontemplate
