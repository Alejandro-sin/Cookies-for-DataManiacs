import os
import sys


project_slug = "{{cookiecutter.project_slug}}"

# Dará color al mensaje en la terminal
ERROR = "\x1b[31m"
CREATING = "\x1b[25m"

if not project_slug:
    print(f"{ERROR}{project_slug=}ERROR: Your project needs a valid name ")
    sys.exit(1)

print(f"Creating project at: {os.getcwd()} {CREATING} ")

