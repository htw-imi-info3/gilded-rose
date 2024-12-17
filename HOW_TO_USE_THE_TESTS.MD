# How to use the provided tests

- test/happy contains all tests that work in the original version and should keep working in the refactored version
- test/bugs contains tests that are buggy (or insufficently specified) in the original version
- test/new contains tests for conjured items

## run tests

Here are some examples:

    pytest test/happy
    pytest test/happy test/bugs
    pytest test/new

or simply:

    pytest test 

to run all tests

## Test configuration

use ORIGINAL_IMPLEMENTATION and FIXED in test/conftest.py to configure the tests:

    ORIGINAL_IMPLEMENTATION = True: use implementation in gilded_rose/original
                              False: use implementation in gilded_rose/refactored

FIXED = [...] contains a list of item types for which the fixed implementations are used.
Add conjured to this list to not skip its tests.

## Test Coverage

Example usages: 

    pytest --cov-report term --cov gilded_rose/original test

    pytest --cov-report term-missing --cov=gilded_rose/original test
 
    pytest --cov-report html --cov=gilded_rose/original test
    open htmlcov/index.html