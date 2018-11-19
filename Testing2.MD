# Project Testing

## TEST CASE 2

### Use case name
  Interface testing
  
### Description
   Perform tests to check makehtml() functionality:
   1) userResult.txt file should exist
   2) htmlInputfile.html should exist 3) the userResult.txt file gets
   appended to the htmlInputfile.html file
  
### Pre-conditions
  input files must be named htmlInputfile.html and userResult.txt; 
  htmlmake.py must also be located in the same directory
  
### Test steps
  run ./ProjectTest2.py from the command line 
### Expected result
  1) the input files which makehtml() calls should exist 2) new html file called 
  dencrime.html is created with result file appended to it
  
### Actual result
  All tests run and pass
  
### Status (Pass/Fail)
  Pass

### Notes
 
  
### Post-conditions
  A new html file called dencrime.html is created with result file appended to it.

