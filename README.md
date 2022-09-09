# 🥯 z412L1
This is a COMP 412 lab 1 student made test suite. It has 552 tests!

## 🚀 How do I use this?
Simply clone this repo into your project directory and execute the bash script 'test' located in the folder:
```
git clone https://github.com/zawie/z412L1
z412L1/test
```
Optionally, you can pipe the output to a seperate file:
```
z412L1/test >> output.log
```
These commands should be run in the root of your project directory.

*⚠️ NOTE*: This assumes that both this test repository and your executable (412fe) is in the same directory and you run the commands from said directory.

## 🤖 How does it work?
It loops through a set of ILOC of files and compares your implementation's output to the references output. 
It only expects that you flag the erroneous lines at least once.
Moreover, it will also indicate failure if you flag an correct line as erroneous.

*⚠️ NOTE*: This a test fails if it takes longer than 1 second. This can be changed in `runner.py` (`TIME_LIMIT`).

## 🧱 How do I contribute?
The biggest thing this needs is *MORE ILOC FILES*. Please chip in and contribute some test files in the `/blocks` directory. 
You don't even need to indicate which lines are failure as this script automatically figures out which lines are bad via the reference solution!
