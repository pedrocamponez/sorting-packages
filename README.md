# sorting-packages
---

This repository is responsible for hosting the sorting packages function, which classifies the packages in different categories (STANDARD, SPECIAL, REJECTED) based on volume, dimension and mass.

---
### Project structure:
```
sorting-packages/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── consts.py
│   │   └── sort.py
│   └── tests/
│       ├── __init__.py
│       └── test_sort.py
├── .gitignore
├── README.md
└── venv/
```
---
### To run the code:
1. First make sure you have Python installed - preferably 3.11.9 to avoid conflicts (this version was used when developing this project)
2. Clone this repository:
    2.1. ```git clone https://github.com/seu-usuario/sorting-packages.git```
    2.2. ```cd sorting-packages```
3. Then, create a virtual environment (venv) and activate it:
    3.1. ```python3 -m venv venv```
    3.2. ```source venv/bin/activate  # macOS/Linux```
    3.3. ```venv\Scripts\activate   # Windows```
4. Once everything is set, you can run the application and tests:
    4.1. ```python3 main.py```
    4.2. ```python3 -m unittest app.tests.test_sort -v```

5. You should see an output like this for the application:
```
    === Package Sorting Interface ===
    Enter package dimensions and mass to classify your package.
    Categories: STANDARD, SPECIAL, or REJECTED
```

6. You should see an output like this for the tests:
```
    test_bulky_by_dimension (app.tests.test_sort.TestSortFunction.test_bulky_by_dimension) ... ok
    test_bulky_by_volume (app.tests.test_sort.TestSortFunction.test_bulky_by_volume) ... ok
    test_heavy_package (app.tests.test_sort.TestSortFunction.test_heavy_package) ... ok
    test_invalid_inputs (app.tests.test_sort.TestSortFunction.test_invalid_inputs) ... ok
    test_rejected_package (app.tests.test_sort.TestSortFunction.test_rejected_package) ... ok
    test_standard_package (app.tests.test_sort.TestSortFunction.test_standard_package) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.000s

    OK
```
---