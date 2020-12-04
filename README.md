# Advent of Code 2020 

Aw man, coding is fun but it can also be a real stinker when it doesnt work properly! 
The makefile here, and structure of this repo is designed so that every time (if you want) run your python script,
and everytime you push to git a series of checks are performed

 * PyTest is used to run your unit tests.
 * mypy checks all the type hints you have in your functions are correct.
 * flake8 performs linting.
 * Sphinx autogenerates documentation from the function annotations (Not checked in Git CI).

This is all done in a enviroment specific for your project. The enviroment contents is defined in
```requirements.txt```. The Github Actions CI also uses this file to create the enviroment it 
test in. Github Actions also sends the results of these tests with any pull requests you make, 
so thats nice.

This testing, though it does increase build time, does ensure your code is structured and tested waayyyy 
more thoroughly than if you never used it. And, if you think you're feeling rogue and want to 
make a build without any of this there is options in the makefile for that too!

Sphinx requires you to change its ```index.rst``` file to include your specfic functions. 
Apart from that, this repo should be just about generic enough to work with any python code (brave words)
if the code is stored in ```src/``` and ```tests/```. The ```Makefile``` will also need to 
be adapted to make sure you are launching the correct python script.. 

![Linting and Testing](https://github.com/andrewblance/advent_of_code_2020/workflows/Linting%20and%20Testing/badge.svg)

Oh, this is also where I store my Advent of Code 2020 attempt for the time being
