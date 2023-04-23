Unit Testing with pytest. Based on video:
https://my.appacademy.io/lessons/testing-basics/f8d2245d/practices/writing-unit-tests-with-pytest/6955d207

use pipenv install pytest --python 3.11 
use python3 -m venv .venv --prompt some_arbitrary_name to change venv prefix
run pipenv shell

In this reading you will explore an alternative to unnitest, pytest.

Writing tests with pytest
Pytest is a third-party package that allows for more readable tests and output. You can explore some of the documentation here.

Writing tests with pytest is very much like unittest, with some syntax changes that makes it easier to write and read.

It is also compatible with existing unittest tests so it is easy to integrate into an existing project. The unittest.TestCase subclass will be automatically parsed and the associated tests will be run.

The pytest package is not so prescriptive. You have a variety of ways to be able to define your unit tests, but they should always be in modules (files) that are named test_*.py or *_test.py, where the "*" means more characters, like the wildcard when finding file names.

Using only functions
In side your test modules, any function named "test*" will be run as a unit test. That looks like this.

def setup_function(fn):
    """The setup_function function runs before each test."""
    pass

def teardown_function(fn):
    """The teardown_function function runs after each test."""
    pass

def testWhateverYouWant():
    """This is a unit test because it beings with "test"."""
    pass

def test_whatever_you_want():
    """This is a unit test because it beings with "test"."""
    pass
Using parameterized functions
Sometimes, your tests will have the exact same logic except for inputs and expected results. For example:

def test_reverso_with_even_letters():
    result = reverso("ABCD")

    assert result == "DCBA"

def test_reverso_with_odd_letters():
    result = reverso("ABC")

    assert result == "CBA"

def test_reverso_with_no_letters():
    result = reverso("")

    assert result == ""
The pytest authors know that this is a common occurrence in unit tests. So, to make it better, they allow you to parameterize your tests. You do that with the pytest.mark.parameterize decorator. The decorator (usually) takes two values, the names of the parameters for your function, and a list of tuples for your arguments. With this awesome feature, you can convert the three tests in the last code example to this.

from pytest import mark

@mark.parametrize("s,expected", [("ABCD", "DBCA"), ("ABC", "CBA"), ("", "")])
def test_reverso(s, expected):
    result = reverso(s)

    assert result == expected
This will run the test_reverso method three times, one for each tuple in the list provided as the second argument to parametrize.

Using classes
If you really do like classes, then you can gather together test functions into a class that starts with "Test". You don't have to do any inheritance. You do still need to prefix the method names with "test".

class TestSomeStuff:
    def setup_method(self, method):
        """The setup_method method runs before each test."""
        pass

    def teardown_method(self, method):
        """The teardown_method method runs after each test."""
        pass

    def test_some_thing(self):
        """This is a unit test because it beings with "test"."""
        pass

    def testSomeThing(self):
        """This is a unit test because it beings with "test"."""
        pass
Making assertions
In pytest, you use the built-in assert keyword to make an assertion. It just accepts a Python expression. If the expression is truthy, then nothing happens. If the expression is falsey, then the assert will throw an AssertionError. They're nice and easy to read, but can be bothersome when wanting to compare lists or dictionaries for equivalency.

Here's an example of a function-based unit test using the assert keyword.

def test_double_function_returns_twice_passed_in():
    result = double(3)
    assert result == 6
Running tests
Running pytest is as simple as running:

> pytest
The pytest command will run all files of the form test_*.py or *_test.py in the current directory. Otherwise, providing a single file's path will be sufficient to run just that file's tests.

The -v flag used in unittest is also available to provide the same output structure. Even without the verbose flag, pytest provides more detail in the output and is also color coded, which is why it is often preferred over unittest.