# Read Me for creating regression algorithms from scratch
This repository is for my own learning experience writing and playing with these algorithms from scratch.
I would not recommend using this in any real implementation because there are better tools out there.

Primary language for this project is Python.

Need to create a parameters.json file in the repository directory with:
    {
        "repository_path": "[your path]"
    }

Need to create a directory called figures where scripts save the figures to
I put my datasets I am messing with in directory called training_sets

visualizer.py is set of functions create graphs with matplotlib python library
cost_function.py makes linear predictions and gets costs
linear_regression_ .py uses gradient descent to get parameters.

I often test basic datasets, create_training_set.py will save a .csv you can use for testing
As is common I put utility functions in util.py script

Uses unittest library to test functionality

Scripts use Python logging module, there is a shell script to setup logs in /var/log