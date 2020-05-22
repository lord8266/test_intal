# Tester for the Intal library

## How it works

The script takes the path to your implementation file and compiles it with the header and the custom test code 
included in this repository

The compiled code is saved as "impl" on the same folder as the python script

Then the scipt runs numerous tests to verify output your code provides

All the errors including time data is printed and also saved inside the log folder which will be created when 
you run the script for the first time

A unique log file is saved each time you run the script with its filename being

```py
time.time()
```

## Installation

Requires python>=3.6
```
pip3 install -r requirements.txt
```

## Usage
```
python3 test.py -p <path_to_implementation> -n <n_tests>
```

## Debugging

Look inside the log folder for details about any erors

Copy the input from the log and debug your code

## Tweaking

### For one/two number based tests

bound_l = min_val of random number

bound_r = max_val of random number

by default bound_l=0, bound_r=10^500

### For array based tests

bound_l = minimum number of elements

bound_r = maximum number of elements

max_val = maximal value of element (0, max_val)

might take long if you give very high values

max_val by default = 10^500

by default bound_l=1000,bound_r=2000

look at each class for more information

array based tests can have a max bound_r of 10000, to change 
this change c_len defined in test.c

