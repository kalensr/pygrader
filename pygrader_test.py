# pygrader_test.py - this is where the specific tests are configured. 
# all tests that are created for a single program will reside in this single file. 
# for multiple programs to be tests, there should will be a matching test file. 
# future considerations: 
#	add a text file, or csv, for data driven management
#	add a UI component for easy configuration of this test file

import os
import _write_test_program as tp


# tp.to_funct() - reads the program under test, and writes a new program, adding
#		necessary functions that are used to drive the program. 
# fpath - specify the path where the program under tests resides
# file_name - the name of the program to test
# return_results - the name of the primary function; returns results of prog execution  
# cr_func_w_main - True - indicates the program has main() function
#		   False - indicates the program has no function. so create one
tp.to_funct(fpath='/Users/kalenhowellsr/Downloads/Debugging_Exercise_2_Corrected',
            file_name='Debug1_Corrected.py',
            return_results='m',
            cr_func_w_main=True)

# after the new program is written, it is imported and driven by _prog_driver
import _prog_driver as dr

# input_data - the data to be entered into the running program under tests. 
# expected_results - the expected results to be returned by the program under tests. 
dr.test(input_data=['10', '5'] , expected_results= (10))
dr.test(input_data=['5', '10'] , expected_results= (10))
    
    



    
    
