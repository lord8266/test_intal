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

bound_l = minimum number of elements

bound_r = maximum number of elements

max_val = maximal value of element

might take long if you give very high values  

max_val by default = 10^500  

look at each class for more information 

array based tests can have a max bound_r of 10000, to change this change c_len defined in test.c  
