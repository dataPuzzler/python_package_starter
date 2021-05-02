# Python Package Starter

The python_package_starter can be used as starting point for the development of a python package, that can be deployed to PyPi or installed locally via pip.
It includes the following features:

- [Python inside a virtual environment](#virtual-env)
- [A (sample) python package](#sample-package)
- [Automatic Loading of Environment Variables](#env-var-loading)
- [Unit-testing via pytest](#unit-testing)
- Documentation generation via Sphinx with auto-doc setup
- [Code linting via flake8](#code-linting)
- [Static Type-checking via mypy](#type-check)

Instructions how to work with each of this components is provided in more detail in the following sections.

The project should be understood as **opinionated**. It is primarily based on my own experience in developing python packages.
Furthermore, I relied on the advice given by the [Python Packaging Authority (PyPA)](https://packaging.python.org/guides/distributing-packages-using-setuptools/) and used the excellent [Flask](https://github.com/pallets/flask) project as primary reference for established 'best practices'. The structure and content of this document was also inspired by [py-package-template](https://github.com/AlexIoannides/py-package-template).


## Project Setup

### Prerequisites
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


### Documentation

The documentation in the `docs` folder has been built using [Sphinx](http://www.sphinx-doc.org). Sqhinx default 'quickstart' was run to create the `conf.py`, which was customized.
The output is based primarily on the Docstrings in the source code, using the `autodoc` extension within Sphinx (specified during the 'quickstart'). The contents for the entry point into the docs (`index.html`), is defined in the `index.rst` file, which itself imports the `modules.rst` file that lists all of the package modules to document. The documentation can be built by running the following command,

```bash
pipenv run sphinx-build -b html docs/source docs/build_html
```

The resulting HTML documentation can be accessed by opening `docs/build_html/index.html` in a web browser.

My preferred third party theme from [Read the Docs](https://readthedocs.org) has also been used, by installing the `sphinx_rtd_theme` as a development dependency and modifying `docs/source/config.py` as follows:

```python
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

#### Creating a PDF Version Using LaTeX

If a LaTex distribution is present on your system, then it is possible to create a PDF version of the documentation, as well. Start by building the prerequisite LaTex version from the ReStructured Text originals,

```bash
pipenv run sphinx-build -b latex docs/source docs/build_latex
```

Then, navigate to `docs/` and run,

```bash
make latexpdf
```

Both LaTeX and PDF versions can then be found in `docs/build_latex`.

### Building Deployable Distributions

The recommended (and most pragmatic) way of deploy this package is to build a Python [wheel](https://wheel.readthedocs.io/en/stable/) and to then to install it in a fresh virtual environment on the target system. The exact build configuration is determined by the parameters in `setup.py`. Note, that this requires that all package dependencies also be specified in the `install_requires` declaration in `setup.py`, **regardless** of their entry in `Pipfile`. For more information on Python packaging refer to the [Python Packaging User Guide](https://packaging.python.org) and the accompanying [sample project](https://github.com/pypa/sampleproject). To create the Python wheel run,

```bash
pipenv run python setup.py bdist_wheel
```

This will create `build`, `py_package_template.egg-info` and `dist` directories - the wheel can be found in the latter. This needs to be copied to the target system (which we are assuming has Python and Pipenv available as a minimum), where it can be installed into a new virtual environment, together with all downstream dependencies, using,

```bash
pipenv install path/to/your-package.whl
```

### Automated Testing and Deployment using Travis CI

We have chosen Travis for Continuous Integration (CI) as it integrates very easily with Python and GitHub (where I have granted it access to my public repositories). The configuration details are kept in the `.travis.yaml` file in the root directory:

```yaml
ncsudo: required

language: python

python:
  - 3.7-dev

install:
  - pip install pipenv
  - pipenv install --dev

script:
  - pipenv run pytest

deploy:
  provider: pypi
  user: alexioannides
  password:
    secure: my-encrypted-pypi-password
  on:
    tags: true
  distributions: bdist_wheel
```

Briefly, this instructs the Travis build server to:

1. download, build and install Python 3.7;
2. install Pipenv
3. use Pipenv and `Pipfile.lock` to install **all** dependencies (dev dependencies are necessary for running PyTest);
4. run all unit tests using PyTest;
5. if the tests were run successfully and if we have pushed a new tag (i.e. a release) to the master branch then:
    - build a Python wheel; and,
    - push it to PyPI.org using my PyPI account credentials.

Note that we provide Travis with an encrypted password, that was made using the Travis command line tool (downloaded using HomeBrew on OS X). For more details on this and PyPI deployment more generally see the [Travis CI documentation](https://docs.travis-ci.com/user/deployment/pypi/#stq=&stp=0).


