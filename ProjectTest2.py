#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: steve su 
# this test file checks for: 1)existing userResult.txt file 
# 2) existing htmlInputfile.html 3) the userResult.txt file gets
# appended to the htmlInputfile.html 

import unittest
import htmlmake 
import os.path
class SQLTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Input(self):
      htmlmake.makehtml("userResult.txt","htmlInputfile.html")
      self.assertTrue(os.path.isfile("htmlInputfile.html"), 'missing html file')
      self.assertTrue(os.path.isfile("userResult.txt"), 'missing result file')

    def test_output(self):
      flag = False
      htmlmake.makehtml('userResult.txt','htmlInputfile.html')
      with open('userResult.txt') as fResult:
        contentResult = fResult.read()
      with open('dencrime.html') as fHtmlOutput: #this is the file makehtml() outputs
        if contentResult in fHtmlOutput.read() : #check if result file content were appended to the html file
          flag = True
      self.assertTrue(flag, 'file output incorrect')

if __name__ == '__main__':
    unittest.main()

