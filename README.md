# Test Engineer Portfolio example

This is a project that cotains example of test automation project written in Python, that contains:
- web behavour driven tests based on [pytest-bdd](https://pypi.org/project/pytest-bdd/) framework
- backend REST API tests tests based [pytest](https://pypi.org/project/pytest/) and [requests](https://pypi.org/project/requests/) module
- load tests based on [locust](http://docs.locust.io/) library
- reports are saving using [pytest-html](https://pypi.org/project/pytest-html/) extension. You can see examples of reports in */home/reports* folder

### Please read instrucations bellow how to set up the project.

1. create _.env_ file in root directory [env-parse](https://pypi.org/project/envparse/0.1.6/) is used to store sensitive config locally
```
BROWSER=safari
IMPLICIT_WAIT=10
BROWSER_WIDTH=1366
BROWSER_HEIGHT=768
HOME_PAGE=automationpractice.multiformis.com
GOREST_API_TOKEN=****
```
2. Install needed libraries using pip (Make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed)
```
pip3 install -r requirements.txt
```
3. Download and install needed browser drivers (You need to have [brew](https://brew.sh/index_uk) already installed):
```
brew install chromedriver
brew install geckodriver
```
4. Run web selenium tests: 
Example of running all web tests by [pytest-bdd](https://pypi.org/project/pytest-bdd/) (see available tags in tests/features: example _@web_tests_):
```
python3 -m py.test -v -m web_tests --html=e2e-report.html --self-contained-html
```
5. Run API tests:
Example of running API test by file using [pytest](https://pypi.org/project/pytest/) (API tests are stored in _/tests/api_tests/_ folder):
```  
python3 -m py.test tests/api_tests/test_api.py --html=reports/api-report.html --self-contained-html
```
6. Run Load test:
Example of running load test using [locust](http://docs.locust.io/) for 15 sec with 1000 users (spawn rate 30users/sec):
```  
locust -f tests/load_tests/load_test_automation_practice.py --headless -u 1000 -r 30 -t 15s --html reports/load_test_automation_practice.html
```
7. Review the reports (reports folder) and screenshots in */reports* folder
*****
### Run all tests on local CI (using [CircleCi](https://circleci.com/docs/2.0/local-cli/))
Install circle ci (requires brew)
```
brew install circleci
```
Install docker desktop:

https://www.docker.com/products/docker-desktop

Setup circle ci (you must have account there):
```
circleci setup
```
Run all tests:
```
circleci local execute --job run_all_tests
```
### Troubleshooting:
Update chromedriver
```
brew upgrade --cask chromedriver
```
Add permission to execute chromedriver
```
xattr -d com.apple.quarantine /usr/local/bin/chromedriver 
```


