from setuptools import find_packages, setup

NAME = "feast_ibm_db2"
REQUIRES_PYTHON = ">=3.9.0"

setup(
    name=NAME,
    version="0.0.1",
    long_desription=open("README.md").read(),
    long_descipriont_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(include=['feast_ibm_db2']),
    install_requires=["feast==0.31.1"]
)