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

## How to use the tests during the refactoring

- do the refactoring in gilded_rose/refactored
- to enable the expectations for the bug fixes, add fixed items one by one to 
  the constant FIXED in gilded_rose/__init__.py

- to develop conjured item (the item to be added after the refactoring) test driven, 
  add 'conjured' to the FIXED list in gilded_rose/__init__.py


(Note: in most cases, you would just refactor the one implementation. In order to 
- compare implementations
- ensure that the tests run equally well on the original and the refactored & fixed version
I've added the implementation toggle in gilded_rose/__init__.py)

## Test Coverage

Example usages: 

    pytest --cov-report term --cov gilded_rose/original test

    pytest --cov-report term-missing --cov=gilded_rose/original test
 
    pytest --cov-report html --cov=gilded_rose/original test
    open htmlcov/index.html