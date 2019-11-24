
import os
import _write_test_program as tp



# ***********************************************
# -------------- CALL PROGRAM - ADD RETURN PARAMS 
# ***********************************************
    
tp.to_funct(fpath='/Users/kalenhowellsr/Downloads/Debugging_Exercise_2_Corrected',
            file_name='Debug1_Corrected.py',
            return_results='m',
            cr_func_w_main=True)

import _prog_driver as dr

dr.test(input_data=['10', '5'] , expected_results= (10))
dr.test(input_data=['5', '10'] , expected_results= (10))
    
    



    
    
