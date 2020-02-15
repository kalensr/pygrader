# pygrader
#### Intro
---
An experimental python application used to help execute and test student programs.
The application has been moved to a Jupyter Notebook for better execution and management of tests. 

If you are not familiar with Jupyter Notebook - click the file named: **'pygrader_nb.ipynb'** in the root of this repository, to see the pygrader source code. Checkout the [Jupyter Notebook site](https://jupyter.org/) for more details. 

Pygrader is a tool for instructors to use when grading and testing student python programs. Imagine your an instruction with 26 students. On any given week, a student can have 2 to 3 command line programs to write. These programs require you, the instructor, to launch the program and execute both happy path tests validating the program works, and the output is correct, and negative tests, verifying the program handles errors gracefully. That's more than 52 programs to manually execute (multiple times) and validate correctness. 

Here is where pygrader comes in to save the day!

#### Demo
---

<body>

<a target="_blank" href="https://www.dropbox.com/s/472a36xtvlp9gi5/Pygrader%20Demo.mp4?dl=0">
  <img src="https://github.com/kalensr/pygrader/blob/master/demo_image.png" alt="Pygrader Demo" height="442" width="748">
</a>

</body>


#### Pre-Work
For programming assignments, I typically write the program myself, to ensure the instructions are correct, as is my expected results. 

Next
* open up the Jupyter Notebook (if not already open) 
* drop my program into the test_dir (I always use my own program for the initial test configuration)
(note: the test directory lives in the same directory as the notebook)

**Test Configuration**
* specify program name
* specify which variable or object to return from the program under test for validation
* specify what input to enter into the program under tests
* specify what expected results to use for validation
  
#### Cookie Test Configuration
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

Using Jupyter Notebook is great - each test configuration lives in its own code block. So you have can have as many tests with a configuration as you need plus as many configurations that you need. The example above has three tests under one configuration (one failing tests for demonstration purposes). 

#### Test Execution Output
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

#### Time for grading

Step 1 - (after reading the students program to visually verify standards and general correctness) - I copy the student's program into the designated test directory (the place where pygrader will look for the student's program). I have it named 'test_dir'.

Step 2 - confgure the tests - sometimes the student's program name is different - so that will need to be updated in the test configuration. In more complex programs, the student might be using different variable names in their program, so that will need to be updated in the test configuration as well. 

Step 3 - run pygrader to test the program


## To Dos:
---
* create video of utilizing pygrader - to add to README file
* add more unit tests - ongoing


## Dependencies
---
### [Jupyter Notebook](https://jupyter.org/)

### [pynput](https://pynput.readthedocs.io/en/latest/#)
