# sorting-packages
This repository is responsible for hosting the sorting packages function.

Clone this repository, and follow the steps.

To run the code:
    - First make sure you have Python installed - preferably 3.11.9
    - Then, create a virtual environment (venv) by using the command ```python3 -m venv venv```
    - After that, make sure you are in the root of the project (```sorting-packages```). If not, you can type ```cd sorting-packages``` from the folder you cloned the repo into.
    - Once everything is set, you can run the tests by using the command ```python3 -m unittest app.tests.test_sort -v```

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