# -*- coding: utf-8 -*-

# import example:
# from .calendar_events import CalendarEvents

import re


def get_version_from_setup_py() -> str | None:
    with open("setup.py", "r") as file:
        setup_content = file.read()
    # Search for a pattern like version='1.0.0' or version="1.0.0"
    version_match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", setup_content)
    if version_match:
        return version_match.group(1)
    return None


def main() -> None:
    print("Hello world!")
    version = get_version_from_setup_py()
    if version:
        print(f"Version: {version}")
    else:
        print("Version not found in setup.py")


if __name__ == "__main__":
    main()
