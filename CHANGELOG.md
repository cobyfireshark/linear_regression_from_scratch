# Changelog of Linear Regression from scratch project
12/18/23:
Made lots of mistakes in first pass of calculating cost function and conducting linear regression
 -Did calculations one at a time due to nature of for loops in Python
 -Did calculations via dictionaries and keys and this gets very messy
 -Going to vectorize the calculations and use NumPy arrays
 -Want to be able to test one step at a time don't want one long monster

Split the cost_function.py into _nonvectorized and _vectorized

Moved cost_function.create_linear_guesses into util and gave it args instead of hard coding values
Created TestCreateLinearGuesses.py that uses unittest to function for good and uneven split ranges