# DH automation

This project provide example of automation of web testing using selenium, python and Firefox browser.

## Getting Started

Get the copy of this example using git:
```
git clone https://github.com/hcieslewicz/DH.git
```


### Prerequisites

To have it running You need to have:
* Python 2.7 - https://www.python.org/
* Selenium - You can download Python bindings for Selenium from the PyPI page for selenium [package](https://pypi.python.org/pypi/selenium). Better way is to get it use [pip](https://pip.pypa.io/en/latest/installing/) to install the selenium package. Using pip, you can install selenium like this:
```
pip install selenium
```
You can download Python bindings for Selenium from the PyPI page for selenium [package](https://pypi.python.org/pypi/selenium). 
* Firefox - https://github.com/mozilla/geckodriver/releases. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

## Running the tests

To run the test You have to call python with the main test scrypt. On Windows open command prompt and type:

```
python.exe test_searchpage.py
```

## Test examples
In this projects there are two test:
* test_a_page_load - this test check, if the search page was opened and and proper title is present on the page. The purpose of it, is to check, if the page is accessible. This is really basic test and should be executed (once) before other tests.
* test_searchpage - this test check the result of the search action
  - go to home page,
  - insert the search text into search filed and click on submit button
  - check if all results are correct.

## Authors

* **Hubert Cieslewicz** (https://github.com/hcieslewicz)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
