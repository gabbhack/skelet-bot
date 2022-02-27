import os
import shutil
import sys
import subprocess

import requests


def get_licenses() -> [str]:
    js = requests.get("https://api.github.com/licenses").json()
    return [i["key"] for i in js]


def get_license(license_: str) -> str:
    js = requests.get(f"https://api.github.com/licenses/{license_}").json()
    return js["body"]


project_name = "{{cookiecutter.project_slug}}"
project_license = "{{cookiecutter.license}}"
use_i18n = "{{cookiecutter.use_i18n}}" == "yes"
i18n_dir = "{{cookiecutter.i18n_dir}}"
i18n_domain = "{{cookiecutter.i18n_domain}}"
use_edgedb = "{{cookiecutter.use_edgedb}}" == "yes"
use_docker = "{{cookiecutter.use_docker}}" == "yes"
use_pre_commit = "{{cookiecutter.use_pre_commit}}" == "yes"
use_pytest = "{{cookiecutter.use_pytest}}" == "yes"
use_flake8 = "{{cookiecutter.use_flake8}}" == "yes"


def main():
    if project_license != "None":
        print(f"You choose {project_license} license")
        print("Getting licenses from GitHub...")
        possible_licenses = get_licenses()
        if project_license not in possible_licenses:
            print(f"Unknown license. Possible licenses: {possible_licenses}")
            sys.exit(1)
        with open("LICENSE.txt", "w") as file:
            file.write(get_license(project_license))
        print("LICENSE.txt file created")

    if use_i18n:
        print("Create i18n dir...")
        subprocess.run(["make", "text-init"])
        subprocess.run(["make", "text-compile"])
    else:
        print("Deleting i18n stuff...")
        os.remove("app/utils/i18n.py")

    if not use_edgedb:
        print("Deleting edgedb stuff...")
        shutil.rmtree("app/models")
        shutil.rmtree("credentials")
        shutil.rmtree("dbschema")
        os.remove("edgedb.toml")
        os.remove("app/utils/edgedb_client.py")

    if not use_docker:
        print("Deleting docker stuff...")
        os.remove(".dockerignore")
        os.remove("Dockerfile")
        os.remove("docker-compose.yaml")

    if not use_pre_commit:
        print("Deleting pre-commit stuff...")
        os.remove(".pre-commit.config.yaml")

    if not use_pytest:
        print("Deleting pytest stuff...")
        shutil.rmtree("tests")

    if not use_flake8:
        print("Deleting flake8 stuff...")
        os.remove(".flake8")

main()
