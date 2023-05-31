from setuptools import setup, find_packages

setup(
    name="libapi_dir",
    version="1.0.0",
    description="API-request for altlinux database",
    packages=find_packages(),
    install_requires=["requests"],
)
