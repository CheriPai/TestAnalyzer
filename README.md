# TestAnalyzer

Provides a quick and easy way to gain insight on the test quality of any Python or Java GitHub project. TestAnalyzer provides this functionality in an easy to use web interface. Calculates three ratios: lines of test per line of code, test classes per class, and test functions per function. These three ratios are compared to the GitHub average to determine a test quality score.

##### Screenshot
![](testanalyzer/data/ta_ss.png?raw=false)


##### Setup
- ```$ pip install -r requirements.txt```


##### Run
- ```$ cd <project root>/testanalyzer```
- ```$ export PYTHONPATH="."```
- ```$ python server/server.py```
Visit http://localhost:5000


##### Test
- ```$ cd <project root>```
- ```$ nosetests```
