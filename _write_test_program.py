# _write_test_program - reads into memory, the program undertests
# modifies the program by adding function and return statements, and writes
# to disk a new program (named _prg_undr_test.py) that can be imported
# and called by _prog_driver.py
# 	[code is too complex; will need to introduce regex, and reduce complexity, 
# 	and a number of unit tests]
# maintained by kalen.howell@gmail.com 


import os

def to_funct(fpath, file_name, return_results, cr_func_w_main=False):        
    
    #fpath='/Users/kalenhowellsr/Downloads/Debugging_Exercise_2'
    #file_name = 'Debug1.py'
    file_name=os.path.join(fpath, file_name)
    
    
    if return_results != '':
        cr_return=True
    else:
        cr_return=False
     
    with open(file_name, "r") as in_file:
        buf = in_file.readlines()
    cnt = 0
    if cr_func_w_main == False and cr_return==True:
        with open("_prg_undr_test" + ".py", "w") as out_file:
            for line in buf:
                if cnt == 0:
                    line = "def do_work():\n\t" + line
                else:
                    line = "\t" + line
                cnt =+1
                out_file.write(line)
            out_file.write("\n\treturn " + results)
    if cr_func_w_main == True:
        in_funct = False
        ret_writen = False
        with open("_prg_undr_test" + ".py", "w") as out_file:
            for line in buf:
                if cr_return ==True and "def " in line and in_funct == True:
                    line = "    return " + return_results + "\n" + line
                    in_funct = False
                    ret_writen = True
                if "def main():" in line:
                    line = "def do_work():\n"
                    in_funct = True
                if "main()" in line:
                    line = ''
                out_file.write(line)
            if ret_writen == False:
                out_file.write("\n    return " + return_results)
    else:
        with open("_prg_undr_test" + ".py", "w") as out_file:
            for line in buf:
                out_file.write(line)
