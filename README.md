# Tester for the Intal library

## Under Work

## Installation

```
pip install -r requirements.txt
```

## Usage
```
python3 test.py -p <path_to_implementation> -n <n_tests>
```

## Debugging

Look inside the log folder for details about any erors

Copy the input from the log and debug your code

Time taken includes time taken by python to compute the value


## Tweaking

### For two number based

bound_l = max_val of random number

bound_r = min_val of random number

by default bound_l=0, bound_r=10^500

### For array based tests

bound_l = minimum number of elements

bound_r = maximum number of elements

max_val = maximal value of element (0, max_val)

might take long if you give very high values

max_val by default = 10^500

look at each class for more information

array based tests can have a max bound_r of 10000, to change 
this change c_len defined in test.c

