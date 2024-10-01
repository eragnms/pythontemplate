# Pythontemplate
A project to be used as a template for python projects.

# Tools and conventions to use
- Use Python 3 (on a machine running Python 2 as default do install with pip3).
- Venv is used for virtual environment. Pipenv can optionally be used. Install with "sudo pacman -S python-pipenv" and then "pipenv install"
- Pytest is used for unit testing.
- Pre-commit is used. Setup pre-commit with "pre-commit install" in the project's root folder and then "pre-commit autoupdate".
- Black is used and triggered by pre-commit, or by "$ black ."
- MyPy is used and is integrated by pre-commit. To integrate into Emacs one need to put "((python-mode . ((flycheck-checker . python-mypy))))" into the project's .dir-locals.el. MyPy also requires a __init__.py file in each directory containing modules to be imported.
- Flake8 is used by using pre-commit, see `pre-commit <https://pre-commit.com/>`_, and by changing max line length to 88 in a .flake8 file in the project root.
- Use isort. Isort is triggered by pre-commit, or "isort .".
- Use gitlint. Setup with: "pre-commit install --hook-type commit-msg". Configured in .gitlint.
- DAP debugging is used with debugpy.

NOTE! If you, in Emacs, get the message "FoundError: No module named 'mypy'", then try to update
mypy:

``` shell
pipenv install mypy
```

# Usage

## Setup with installation script
To install using the installation script (the target folder should be a git folder):

``` shell
cd pythontemplate
python -m install <project_name> <target_folder>
```

## Setup manually
To use the template and adapt it to a new project manually:

  - Rename the pythontemplate folder to your project name.
  - Keep install_requires in setup.py updated with required packages.
  - Do not touch requirements.txt.
  - In setup.py update: version=find_version("... so that it points to the file where __version__ is defined.
  - In setup.py make entry_point point to the file containing the main function.
  - In setup.py update: name, description, url.
  - Rename and edit pythontemplate-runner.py.
  - Run "pre-commit install" in the project's root folder and then "pre-commit autoupdate".
  - Run "pre-commit install --hook-type commit-msg".

# Run the script
The script can be run from the root folder with either of:

``` shell
python -m pythontemplate
```

or:

``` shell
python -m pythontemplate.<module>
```

or:

``` shell
./pythontemplate-runner.py
```

# Debug
Use the DAP debugger. Emacs is set up in the file .dir-locals.el.
Start the script with:

  $ python -Xfrozen_modules=off -m debugpy --listen 5678 --wait-for-client -m asset_predictor.<module>

In Emacs:

M x dap-breakpoint-add
M x dap-debug
M x dap-hydra

# Documentation
To build the documentation:

``` shell
cd docs
make html
```

# Tests
To run tests:

``` shell
pytest
```

# Install the script
Use pipx to run the script in a virtual environment:

``` shell
sudo pacman -S python-pipx
```

Then:

``` shell
cd pythontemplate
pipx install .
```

To upgrade to a new version:

``` shell
cd pythontemplate
pipx upgrade pythontemplate
```

When installed the entry points to the scripts, i.e. the way to run
the scripts, are defined by the entry_points in pyproject.toml, in its
section project.scripts.

# To build a wheel

``` shell
python -m build
```

# To install a wheel file

``` shell
pipx install <filename>.whl
```

# Docker

To run the script with docker...
Look at how this is done in the cosycar project.
