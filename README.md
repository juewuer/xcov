[![Build Status](https://travis-ci.org/datadriventests/ddt.svg)](https://travis-ci.org/datadriventests/ddt)
[![codecov.io](https://codecov.io/github/datadriventests/ddt/coverage.svg?branch=master)](https://codecov.io/github/datadriventests/ddt)
<br />
[![Version](https://img.shields.io/pypi/v/ddt.svg)](https://pypi.python.org/pypi/ddt2)
[![Downloads](https://img.shields.io/pypi/dm/ddt.svg)](https://pypi.python.org/pypi/ddt2)

DDT (Data-Driven Tests) allows you to multiply one test case
by running it with different test data, and make it appear as
multiple test cases.

# Installation


```pip install ddt```

Check out [the documentation](http://ddt.readthedocs.org/) for more details.

See [Contributing](CONTRIBUTING.md) if you plan to contribute to `ddt`,
and [License](LICENSE.md) if you plan to use it.

I Modify ddt to ddt2 for i want to get some features, and not all functions of ddt can be uesed
1. get the determined name of test case
1. support for __var__  to generate case 
1. support for __i__ to have index
1. parameter in a test function should not have i
1. add function decorators autoindex


dcov is a tool to get increment code coverage report from gcovr report.

## Install

sudo pip install .

## Uninstall

sudo pip uninstall dcovr. or python setup.py install

## Usage

Run `dcov` in git root of your code. You can use `dcov -h` for more information.

example:
`dcov --since=7fff --until=01222 --prefix=utcov. --report-dir=./test_output/report/`

Then you will get the increment result in `increment_coverage_report.html`
  
