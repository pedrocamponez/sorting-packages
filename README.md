# sorting-packages
This repository is responsible for hosting the sorting packages function, which classifies the packages in different categories (STANDARD, SPECIAL, REJECTED) based on volume, dimension and mass.

Project structure:
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

To run the code:
    - First make sure you have Python installed - preferably 3.11.9 to avoid conflicts (this version was used when developing this project)
    - Clone this repository:
        ```git clone https://github.com/seu-usuario/sorting-packages.git```
        ```cd sorting-packages```
    - Then, create a virtual environment (venv) and activate it:
        ```python3 -m venv venv``` - to create
        ```source venv/bin/activate  # macOS/Linux```
        ```venv\Scripts\activate   # Windows```
    - Once everything is set, you can run the tests:
        ```python3 -m unittest app.tests.test_sort -v```

    You should see an output like this:
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