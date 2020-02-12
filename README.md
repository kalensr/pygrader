# pygrader
---
An experimental python application used to help execute and test student programs.
The application has been moved to a Jupyter Notebook for better execution and management of tests. 

A tool for instructors to use when grading and testing student python programs. Imagine your an instruction with 26 students. On any given week, a student can have 2 to 3 command line programs to write. These programs require you, the instructor, to launch the program and execute both happy path tests validating the program works, and the output is correct, and negative tests, verifying the program handles errors gracefully. That's a total of 81 programs to manually execute (multiple times) and validate correctness. 

Here is where pygrader comes in to save the day!

#### Pre-Work
For programming assignments, I typically write the program myself, to ensure the instructions are correct, as is my expected results. 

Next
* open up the Jupyter Notebook (if not already open) 
* drop my program into the test_dir (I always use my own program for the initial test configuration)
(note: the test directory lives in the same directory as the notebook)

**Test Configuration**
* configure pygrader for the test - 
  * specify program name
  * specify which variable object to return for validation
  * specify what input to enter into the program under tests
  * specify what expected results to use for validation
  
*example*
```
to_funct(fpath=get_test_path(dir="unit_test_dir"),
            file_name='Cookies.py',
            return_results='sugarNeeded, butterNeeded, flourNeeded',
            cr_func_w_main=False)

# input_data - the data to be entered into the running program under tests. 
# expected_results - the expected results to be returned by the program under tests. 

test(prog, input_data=['24'] , expected_results= (0.75, 0.5, 1.375))
test(prog, input_data=['65'] , expected_results= (2.03125, 1.3541666666666665, 3.723958333333333))
test(prog, input_data=['65'] , expected_results= (2.03125, 1.3542666666666665, 3.723958333333333))
```

Using Jupyter Notebook is great - each test configuration lives in its own code block. So you have can have as many configurations as you need for 1 test program, or many. The example above has two tests under one configuration. 

The output of my unit tests is as follows: 

*example*
```
Enter the number of cookies: 24
The amount of sugar needed is: 0.750 cups
The amount of butter needed is: 0.500 cups
The amount of flour needed is: 1.375 cups


Enter the number of cookies: 65
The amount of sugar needed is: 2.031 cups
The amount of butter needed is: 1.354 cups
The amount of flour needed is: 3.724 cups


Enter the number of cookies: 65
The amount of sugar needed is: 2.031 cups
The amount of butter needed is: 1.354 cups
The amount of flour needed is: 3.724 cups

 **FAILURE** 	expecting: (2.03125, 1.3542666666666665, 3.723958333333333)
  recieved: (2.03125, 1.3541666666666665, 3.723958333333333)
 ```

### Time for grading

Step 1 - (after reading the students program to visually verify standards and general correctness) - I copy the student's program into the designated test directory (the place where pygrader will look for the student's program). I have it named 'test_dir'.


ToDo's: 
* [in progress] Create unit tests
* Add example usage documentation - will record a video and embed in README
* X-make the tester data driven - where tests can be saved in text files and read by pygrader
* Jupyter Notebook eliminates the need for a data driven approach using seperate text files for tests.

## Dependencies
---
### [Jupyter Notebook](https://jupyter.org/)

### [pynput](https://pynput.readthedocs.io/en/latest/#)
