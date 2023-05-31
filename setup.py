from setuptools import setup, find_packages

setup(
    name="libapi",
    version="1.0.0",
    description="API-request for altlinux database",
    packages=find_packages(),
    install_requires=["requests"],
)
