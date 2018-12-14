# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:57:25 2018

@author: Levi Nickerson
"""
import Project
import unittest 

# csv file was downloaded on 11/15/2018
# Tests will pass for this file 
# csv file included in repo  



class ProjectTestCase(unittest.TestCase):
    
    def test_csv_parse(self):
        # Make sure that the csv file parsed correctly 
        self.assertEqual(Project.district_id[5], 6, 'District ID is incorrect' )
        self.assertEqual(Project.precinct_id[2], 314, 'Precinct ID is incorrect')
        self.assertEqual(Project.neighborhood_id[3], 'belcaro', 'Neighborhood ID is incorrect')

    def test_date(self):
        # Test to determine if date handling was successful 
        self.assertEqual(Project.month[0], 6, 'Month is incorrect')
        self.assertEqual(Project.day[0], 15, 'Day is incorrect')
        self.assertEqual(Project.year[0], 2016, 'Year is incorrect')
        
    def test_neighborhood(self):
        # Test to determine if neighborhood handling was successful
        self.assertEqual(Project.neighborhood[0], 4, 'Neighborhood 4 is incorrect')
        self.assertEqual(Project.neighborhood[1], 3, 'Neighborhood 3 is incorrect')
        self.assertEqual(Project.neighborhood[2], 5, 'Neighborhood 5 is incorrect')
        self.assertEqual(Project.neighborhood[3], 1, 'Neighborhood 1 is incorrect')
        self.assertEqual(Project.neighborhood[4], 2, 'Neighborhood 2 is incorrect')
        
    def test_offense(self):
        # Test to determine if offense handling was successful
        self.assertEqual(Project.offense[1], 5, 'Offense 5 is incorrect')
        self.assertEqual(Project.offense[35], 3, 'Offense 3 is incorrect')
        self.assertEqual(Project.offense[72], 2, 'Offense 2 is incorrect')
        self.assertEqual(Project.offense[1906], 1, 'Offense 5 is incorrect')
        self.assertEqual(Project.offense[3214], 4, 'Offense 5 is incorrect')

if __name__ == '__main__':
    unittest.main()
