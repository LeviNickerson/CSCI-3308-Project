#!/usr/bin/env python3

import unittest
import os.path


class htmljs_TestCase(unittest.TestCase):

    def open_file():
        html_file = open("dencrime.html", "r")
        #get all lines from html file
        html_data = html_file.readlines()
        #amount var is the amount of items in out spreadsheet (1 subtracts header)
        return html_data


    def js_exists_Test(jsfile_string):
        #test if js file is in directory
        self.assertTrue(os.path.isfile(jsfile_string), '.js file not found')

    def csv_exists_Test(csvfile_string):
        #test if js file is in directory
        self.assertTrue(os.path.isfile(csv_string), '.csv file not found')


    def js_in_html_Test(jsfile_string):
        #test if html file is pointing to js file somewhere in file

        js_bool = False
        line_num = 0


        html_data = openfile()
        #open the html file

        length = len(html_data) - 1

        while !js_bool or line_num > length:

            if "<script src" in html_data[line_num]:
                if js_filestring in html_data[line_num]:
                    js_bool = True
                    print(jsfile_string+" REFERENCES ON LINE "+ line_num)
            else:
                line_num = line_num+1

        self.assertTrue(js_bool, '.js file in found')


if __name__ == '__main__':
    unittest.main()
