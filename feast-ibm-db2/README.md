# Feast Custom Offline Store for IBM DB2:

Please check file setup.py for dependencies:
```
setup(
    name=NAME,
    version="0.0.1",
    long_desription=open("README.md").read(),
    long_descipriont_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(include=['feast_ibm_db2']),
    install_requires=[
        "feast==0.31.1"
        "ibm-db",
        "ibm-db-sa"
    ]
)
```

Then install this lib:
```
python setup.py install
```

Then check 'feast-ibm-test' folder  to use.