# Feast Offline Store for IBM DB2 database

## How to install:

Please check setup.py to validate dependencies:
```
setup(
    name=NAME,
    version="0.0.1",
    long_desription=open("README.md").read(),
    long_descipriont_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(include=['feast_ibm_db2']),
    install_requires=[
        "feast==0.31.1",
        "ibm-db",
        "ibm-db-sa"
    ]
)
```


Then install module into enviroment:
```
python setup.up install
```

Build wheel file:
```
python setup.py bdist_wheel
```
File .whl will be located in dist/ . Install it into new system:
```
pip install feast_ibm_db2-0.0.1-py3-none-any.whl
```

<b>How to use it:</b> 

Please check feast-ibm-test/ folder.
