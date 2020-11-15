# coding=utf-8
__auther__ = 'ya'

import unittest
from utility import HTMLTestRunner
import time
import os
import sys
from utility import excel

case_path = sys.path[0]
print(case_path)

result = "./Result"

# create a test suit
def Creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    print(discover)
    for test_suit in discover:
        for case_name in test_suit:
            testunit.addTest(case_name)
            print(case_name)
        print(testunit)
    return testunit

test_case = Creatsuite()

now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

tdresult = result + "/" + day
print(tdresult)
# run the case and generate the report in the path
if not os.path.exists(tdresult):
    try:
        os.makedirs(tdresult)
    except Exception:
        # Since this might not be thread safe
        print("Create folder Fail!")

if os.path.exists(tdresult):
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'personal test', description=u'case detail')
    runner.run(test_case)
    fp.close()
else:
    print("report path not found")