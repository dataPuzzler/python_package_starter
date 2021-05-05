[![Run unittests](https://github.com/dataPuzzler/python_package_starter/actions/workflows/unit-tests.yml/badge.svg?branch=master&event=push)](https://github.com/dataPuzzler/python_package_starter/actions/workflows/unit-tests.yml)
# Python Package Starter

The python_package_starter can be used as starting point for the development of a python package, that can be deployed to PyPi or installed locally via pip.
It includes the following features:

- [Python inside a virtual environment](#virtual-env)
- [A (sample) python package](#sample-package)
- [Automatic Loading of Environment Variables](#env-var-loading)
- [Unit-testing via pytest](#unit-testing)
- [Automated Testing via Github Workflows](#ci)
- [Code linting via flake8](#code-linting)
- [Static Type-checking via mypy](#type-check)
- [Documentation generation via Sphinx with auto-doc setup](#code-docu)


Instructions how to work with each of this components is provided in more detail in the following sections.

The project should be understood as **opinionated**. It is primarily based on my own experience in developing python packages.
Furthermore, I relied on the advice given by the [Python Packaging Authority (PyPA)](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and used the excellent [Flask](https://github.com/pallets/flask) project as primary reference for established 'best practices'. The structure and content of this document was also inspired by [py-package-template](https://github.com/AlexIoannides/py-package-template).


## Project Setup

### Prerequisites <a name="prereq"></a>
- It is assumed that Python 3.9.x is 'globally' installed on your system and available on your Path.
- It is assumed that git 2.x.x is installed on your system and available on the your Path.


### Installing pipenv globally
[Pipenv](https://docs.pipenv.org) is used as the tool of choice to manage virtual environments and project package dependencies. You can install 
it globally on your system with:

```bash
pip3 install pipenv
```
For more information, including advanced configuration options, see the [official pipenv documentation](https://docs.pipenv.org).

### Clone the project  

Clone this repository into a directory of your choice via
```bash
git clone https://github.com/dataPuzzler/python_package_starter.git <Your_Project_Name>
cd <Your_Project_Name>
```

### Install project dependencies into a virtual environment
Inside `<Your_Project_Name>`, run the following command:

```bash
pipenv install --dev
```

This will create a virtual python environment into `<Your_Project_Name>/.venv` and install all project dependencies (incl. dev dependencies) into it.

All of the direct packages dependencies required to run the project's code (e.g. multilevel_py), as well as all the packages used during development (e.g. flake8 for code linting and IPython for interactive console sessions), are described in the `Pipfile`. Their precise downstream dependencies are fixed in `Pipfile.lock`, which is used to guarentee repeatable (i.e. deterministic) builds.


## Application of project and related tools

### Running Python and IPython from the Project's Virtual Environment<a name="virtual-env"></a>

In order to open a Python REPL using within an environment that precisely mimics projects virtual environment, use Pipenv from the command line as follows,

```bash
pipenv run python3
```

For use of an interactive python session, run the previous command with `ipython3` instead of `python3`.

### Pipenv Shells

Prepending `pipenv` to every command you want to run within the context of your Pipenv-managed virtual environment is tedious. This can be avoided by entering into a Pipenv-managed shell.

```bash
pipenv shell
```

Which is equivalent to 'activating' the virtual environment. Any command will now be executed within the virtual environment. That means instead of `pipenv run <ANY_CMD>` it suffices to run `<ANY_CMD>` inside an active shell session.

Use `exit` to leave the shell session.



### Automatic Loading of Environment Variables <a name="env-var-loading"></a>

Pipenv will automatically pick-up and load any environment variables declared in the `.env` file, located in the package's root directory. For example, adding,

```bash
PCK_ENV=prd
```

Will enable access to this variable within any Python program, via a call to `os.environ['PCK_ENV']`. 



### A (sample) python package <a name="sample-package"></a>

The sample python package shipped with this boilerplate is located in the `src` directory consists of the two main files:

- `animals.py`
- `entry_points.py`

The code in `animals.py` depends on [multilevel_py](https://github.com/dataPuzzler/multilevel_py) and illustrates its core features by constructing a 
simple classification hierarchy, resulting in a description of the well known cartoon characters tom and jerry.
This code depicts an example of a simple python package and is meant to be replaced by the code of the python package to be developed.

Entry points enable that the invocation of certain package functions from the command line. For example, the `entry_points.py` module is referenced in the `setup.cfg` file in the `options.entry_points` section:

```python
console_scripts =
    sample_pck = sample_pck.entry_points:main
```
This enables the declared entry point - `sample_pck.entry_points.main` -  to be invoked when `pipenv run sample_pck` is called from the command line.


### Running Unit Tests <a name="unit-testing"></a>

All test have been written using the [PyTest](https://docs.pytest.org/en/latest/) package. Tests are kept in the `tests` folder and can be run from the command line by invoking,

```bash
pipenv run pytest
```

The test suite is structured as an independent Python package as follows:

```bash
tests/
 |-- test_data/
 |   |-- your-test-data.json
 |   __init__.py
 |   conftest.py
 |   test_animals.py
```

The `conftest.py` module is used by pytest to build testing-utilities used by several testing modules. These are referred to as 'fixtures' in PyTest - more details can be found [here](https://docs.pytest.org/en/latest/fixture.html).

### Automated Testing using Github workflows <a name="ci"></a>
This package starter also defines a Continous Integration workflow that resides in the `.github/workflows/unit-tests.yml` directory.
This workflow runs all unit-tests via `pytest` on each push to the master branch. 
If you don't use Githubs CI Pipelines should delete the `.github` directory and its subdirectories. 


### Linting Code <a name="code-linting"></a>

[Flake8](http://flake8.pycqa.org/en/latest/) is used to enforce recommended code style guides. The precise linting rules can be configured in the `[flake8]` section of `setup.cfg`.

To start code linting, execute the following command:

```bash
pipenv run flake8 src/sample_pck
```


### Static Type Checking <a name="type-check"></a>

The [MyPy package](http://mypy-lang.org) can be used to perform static type checks on your codebase. The tool is configured in the `[mypy]` section of 
`setup.cfg` and can be executed via the following command.

```bash
pipenv run python -m mypy
```


### Code Documentation <a name="code docu">

The documentation is located `docs` folder and has been built using [Sphinx](http://www.sphinx-doc.org). Sqhinx's default 'quickstart' was run in order to create the initial `conf.py`. It was customized concerning the docstring format and the documentation theme as explained below.


#### Usage of Google-style docstrings
To support Docstrings according to the [Google Styleguid](https://google.github.io/styleguide/pyguide.html), the `sphinx.ext.napoleon` shipped by Sphinx is used.


#### Usage of Read the Docs Documentation Theme
The third party theme from [Read the Docs](https://readthedocs.org) has also been used, by installing the `sphinx_rtd_theme` as a development dependency and modifying `docs/source/config.py` as follows:

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```


#### Creating a HTML Version

From the repository directory:

```bash

pipenv run sphinx-build -b html docs/ docs/_build/html
```

Alternatively, you can use the `make` utility located in the `docs` dir:
```bash
cd docs
make html
```

The resulting HTML documentation can be accessed by opening `docs/_built/html/index.html` in a web browser.



#### Creating a PDF Version Using LaTeX

If a LaTex distribution is present on your system, it is possible to create a PDF version of the documentation as well. 
Navigate to `docs/` and run,

```bash
make latexpdf
```

Both LaTeX and PDF versions can then be found in `docs/_build/latex`.


### Building a deployable Package Distribution

The recommended approach to deploy this package is to build a Python [wheel](https://wheel.readthedocs.io/en/stable/) and to install it in a fresh virtual environment on the target system. The exact build configuration is determined by the provided metadata in `setup.py` and `setup.cfg`. Note, that this requires that all package dependencies are also specified in the `install_requires` declaration in `setup.py`, **regardless** of their entry in `Pipfile`. For more information on Python packaging refer to the [Python Packaging User Guide](https://packaging.python.org) and the accompanying [sample project](https://github.com/pypa/sampleproject). To create the Python wheel run,

```bash
pipenv run python setup.py bdist_wheel
```

This will create `build` and `dist` directories - the wheel can be found in the latter. This needs to be copied to the target system (which is assumed to fulfill the requirements as defined in ['Prerequisites']('#prereq')). There it can be installed into a new virtual environment, together with all downstream dependencies, by running

```bash
pipenv install path/to/your-package.whl
```
