# 2is50-2019-2020-ha-0

Repository for Homework Assignment 0 of 2IS50, 2019-2020

What you need to do for this assignment is described separately.

Things to try:

* Open the project in **PyCharm**.

* You may be asked to select your Python interpreter and install missing libraries
  (also see file `requirements.txt`):
    * pytest
    * sphinx
    * sphinx_rtd_theme

* It is recommended that you configure an associated _virtual environment_
  that will contain the required libraries, isolated from your other installed libraries.
  See: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
  
* At the top, you can select one of four pre-programmed run configurations:
    * **generate html docs with sphinx**: to generate HTML documentation, using `Sphinx`
    * **run rps application**: to run the application
    * **run doctest examples in src**: to run the `doctest` examples in the docstrings
    * **run pytest test cases in test_cases.py**: to run the separate test cases, using `pytest`
    
* Then click the **run** (play) button next to the selected run configuration.
    * To read the generated documentation, open `docs/build/index.html` with a web browser:
      in the project panel on the left, right-click that file,
      and select **Open in Browser** (then select your preferred browswer).
    * When you run the application, a GUI window opens with several buttons.
    * The test cases (both `doctest` and `pytest`) will produce failures.
      Inspect those failures.
