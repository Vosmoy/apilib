import requests


def get_packages(branch, arch):
    url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch}"
    params = {"arch": arch}
    response = requests.get(url, params=params)
    data = response.json()
    packages = {p["name"]: {"version": p["version"], "release": p["release"]} for p in data["packages"]}
    return packages
