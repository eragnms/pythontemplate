import argparse
import fileinput
import os
import shutil
import subprocess

FILES = [
    ".flake8",
    ".gitlint",
    ".gitignore",
    ".dir-locals.el",
    "LICENSE",
    "mypy.ini",
    ".pre-commit-config.yaml",
    "pythontemplate-runner.py",
    "README.rst",
    "requirements.txt",
    "pyproject.toml",
]

FOLDERS = [
    "docs",
    "tests",
    "pythontemplate",
]

PROJECT_NAME = "pythontemplate"


def main() -> None:
    parser = argparse.ArgumentParser(description="See README for usage.")
    parser.add_argument("project_name", help="The name of the project.")
    parser.add_argument("target_folder", help="The folder to install the project to.")
    parser.add_argument(
        "--skip_readme", "-sr", help="Skip the README.rst file.", action="store_true"
    )
    parser.add_argument(
        "--skip_license", "-sl", help="Skip the LICENSE file.", action="store_true"
    )
    parser.add_argument(
        "--install_pipenv",
        "-ip",
        help="Install pipenv instead of venv.",
        action="store_true",
    )
    args = parser.parse_args()
    print(f"Installing {PROJECT_NAME} to {args.target_folder}")
    if not is_git_repository(args.target_folder):
        print("The target folder has to be a git folder. Exiting...")
        exit(1)
    copy_files(
        args.target_folder, args.skip_readme, args.skip_license, args.install_pipenv
    )
    copy_folders(args.target_folder)
    delete_temp_files(args.target_folder)
    rename_files_and_directories(args.target_folder, PROJECT_NAME, args.project_name)
    replace_word_in_project(args.target_folder, PROJECT_NAME, args.project_name)
    if args.install_pipenv:
        pipenv_install(args.target_folder)
        pre_commit_install_pipenv(args.target_folder)
    else:
        venv_install(args.target_folder)
        pre_commit_install_venv(args.target_folder)
    print("Installation complete.")
    print(
        f"Now you can enter the folder {args.target_folder} "
        "and test the follwing commands:\n"
    )
    if args.install_pipenv:
        print(
            " - pipenv shell\n"
            f" - ./{args.project_name}-runner.py\n"
            " - pytest\n"
            " - cd docs\n"
            " - make html\n"
            " - cd ..\n"
        )
    else:
        print(
            " - source venv/bin/activate.fish\n"
            f" - ./{args.project_name}-runner.py\n"
            " - pytest\n"
            " - cd docs\n"
            " - make html\n"
            " - cd ..\n"
        )


def is_git_repository(directory: str) -> bool:
    # Check if the .git directory exists within the specified directory
    git_dir = os.path.join(directory, ".git")
    return os.path.isdir(git_dir)


def pre_commit_install_pipenv(directory: str) -> None:
    print(f"Running pre-commit install in {directory}")
    try:
        # Change to the target directory
        os.chdir(directory)
        # Run 'pipenv run pre-commit install --hook-type commit-msg'
        print("Running 'pipenv run pre-commit install'")
        subprocess.run(
            ["pipenv", "run", "pre-commit", "install"],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["pipenv", "run", "pre-commit", "install", "--hook-type", "commit-msg"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    try:
        print("Running 'pipenv run pre-commit autoupdate'")
        subprocess.run(
            ["pipenv", "run", "pre-commit", "autoupdate"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def pre_commit_install_venv(directory: str) -> None:
    print(f"Running pre-commit install in {directory}")
    try:
        # Change to the target directory
        os.chdir(directory)
        # Run 'pre-commit install --hook-type commit-msg'
        print("Running 'pre-commit install'")
        # Run both activation and pre-commit install in a Fish shell
        subprocess.run(
            "source venv/bin/activate.fish && pre-commit install",
            shell=True,
            executable="/usr/bin/fish",
        )
        subprocess.run(
            "source venv/bin/activate.fish && pre-commit install "
            "--hook-type commit-msg",
            shell=True,
            executable="/usr/bin/fish",
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    try:
        print("Running 'pipenv run pre-commit autoupdate'")
        subprocess.run(
            ["pipenv", "run", "pre-commit", "autoupdate"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def pipenv_install(directory: str) -> None:
    print(f"Running pipenv install in {directory}")
    try:
        # Change to the target directory
        os.chdir(directory)
        # Run 'pipenv install'
        subprocess.run(
            ["pipenv", "install"], check=True, capture_output=True, text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running pipenv install: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def venv_install(directory: str) -> None:
    print(f"Running venv install in {directory}")
    try:
        # Change to the target directory
        os.chdir(directory)
        # Run 'venv install'
        subprocess.run(
            ["python", "-m", "venv", "venv"], check=True, capture_output=True, text=True
        )
        # Install requirements
        subprocess.run(
            "source venv/bin/activate.fish && pip install -r requirements.txt",
            shell=True,
            executable="/usr/bin/fish",
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running venv install: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def copy_files(
    target_folder: str, skip_readme: bool, skip_license: bool, install_pipenv: bool
) -> None:
    print(f"Copying files to {target_folder}")
    try:
        if install_pipenv:
            FILES.append("Pipfile")
        for src_file in FILES:
            if src_file == "README.rst" and skip_readme:
                continue
            if src_file == "LICENSE" and skip_license:
                continue
            shutil.copy(src_file, target_folder)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except PermissionError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


def copy_folders(target_folder: str) -> None:
    print(f"Copying folders to {target_folder}")
    for src_folder in FOLDERS:
        try:
            complete_target_folder = os.path.join(target_folder, src_folder)
            shutil.copytree(src_folder, complete_target_folder)
        except FileExistsError as e:
            print(f"Error: {e}")
            exit(1)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            exit(1)
        except PermissionError as e:
            print(f"Error: {e}")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(1)


def delete_temp_files(directory: str) -> None:
    print(f"Deleting temporary files in {directory}")
    for root, dirs, files in os.walk(directory):
        for target_file in files:
            if target_file.endswith("~"):
                file_path = os.path.join(root, target_file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")


def replace_word_in_project(root_dir: str, old_word: str, new_word: str) -> None:
    print(f"Replacing {old_word} with {new_word} in project {root_dir}")
    for root, dirs, files in os.walk(root_dir):
        for target_file in files:
            try:
                file_path = os.path.join(root, target_file)
                replace_in_file(file_path, old_word, new_word)
            except Exception as e:
                print(f"Error replacing word in file {file_path}: {e}")
                exit(1)


def replace_in_file(file_path: str, old_word: str, new_word: str) -> None:
    with fileinput.FileInput(file_path, inplace=True) as target_file:
        for line in target_file:
            print(line.replace(old_word, new_word), end="")


def rename_files_and_directories(root_dir: str, old_word: str, new_word: str) -> None:
    print(f"Renaming files and directories in {root_dir}")
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # Rename files
        for name in files:
            if old_word in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(old_word, new_word)
                new_path = os.path.join(root, new_name)
                shutil.move(old_path, new_path)
        # Rename directories
        for name in dirs:
            if old_word in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(old_word, new_word)
                new_path = os.path.join(root, new_name)
                shutil.move(old_path, new_path)


if __name__ == "__main__":
    main()
