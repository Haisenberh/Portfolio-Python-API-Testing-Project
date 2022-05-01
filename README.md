# Test Engineer API TESTS project Portfolio example

This is a project that contains example of backend tests written in Python:
- backend REST API tests tests based [pytest](https://pypi.org/project/pytest/) 
- REST API requests are sending using [requests](https://pypi.org/project/requests/) module
- These API tests are also running on [CircleCi](https://circleci.com/) continious integration tool
- reports are saving using [pytest-html](https://pypi.org/project/pytest-html/) extension. You can see examples of reports in */home/reports* folder

### Please read instrucations bellow how to set up the project.

1. create _.env_ file in root directory [env-parse](https://pypi.org/project/envparse/0.1.6/) is used to store sensitive config locally
```
GOREST_API_TOKEN=****
```
2. Install needed libraries using pip (Make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed)
```
pip3 install -r requirements.txt
```
3. Run API tests:
Example of running API test by file using [pytest](https://pypi.org/project/pytest/) (API tests are stored in _/tests/api_tests/_ folder):
```  
python3 -m py.test tests/api_tests/test_api.py --html=reports/api-report.html --self-contained-html
```
4. Review the reports (reports folder) and screenshots in */reports* folder
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
circleci local execute --job run_api_tests
```
