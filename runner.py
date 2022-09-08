# -*- coding: iso-8859-15 -*-
"""
Repository: https://github.com/zawie/z412L1
Consider adding your own tests cases to the repository so the whole class can benefit!
You can add tests (and push) to the blocks directory in this repository
"""

#IMPL = "/storage-home/a/adz2/comp412/lab1/412fe" 
IMPL = "./412fe" #Path to your 412fe (MUST FILL OUT!!)
REF = "~comp412/students/lab1/lab1_ref" #Path to reference solution

REPO_DIR = "./z412L1"
COURSE_DIR = "/clear/courses/comp412/students"

ILOC_DIRS = [REPO_DIR + "/blocks", COURSE_DIR+"/lab1/test_inputs"] + [COURSE_DIR+"/ILOC/blocks/lab" + str(n) for n in (2,3)]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2012/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2013/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2013/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2014/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2014/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2015/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2015/lab3"]
#Add your own directory to ILOC_DIRS list!

TIME_LIMIT = 1 #in seconds
"""
Test suite implementation
"""
import re
import os
import commands
import multiprocessing

#Helper print function
def tabprint(output, tab_count):
    for line in output.split('\n'):
        print('\t'*tab_count+line)

#Returns a set of errored line numbers
def run(pathToImpl, pathToILOC):
    
    #Execute implementatino on a specific iloc file
    cmd = "{} {}".format(pathToImpl, pathToILOC)
    (_, output) = commands.getstatusoutput(cmd)

    return output

def parseErroredLines(output):
    bad_lines = set()
    for line in output.split('\n'):
        match = re.match(r'^ERROR (\d+):', line)
        if match != None:
            bad_lines.add(int(match.group(1)))
    return bad_lines
    
def executeTest(filePath):
    ref_output = run(REF, filePath)
    impl_output = run(IMPL, filePath)

    ref_lines = parseErroredLines(ref_output)
    impl_lines = parseErroredLines(impl_output)

    if (ref_lines == impl_lines):
        print('✅ {} passed!'.format(filePath))
        exit(0) #Passed
    else:
        num_errors = len(ref_lines)
        true_positives = len(impl_lines.intersection(ref_lines))
        false_positives = len(impl_lines.difference(ref_lines))

        print('❌ {} failed!'.format(filePath))
        print("- Summary:")
        tabprint("You identified {}/{} errors correctly.".format(true_positives, num_errors), 1)
        tabprint("You identified {} correct lines as errors.".format(false_positives), 1)
        print("- Reference output:")
        tabprint(ref_output, 1)
        print("- Your output:")
        tabprint(impl_output, 1)

        exit(1) #Failed

def getFiles():
    files = list()
    for d in ILOC_DIRS:
        for filename in os.listdir(d):
            if filename.endswith(".i"):
                f = os.path.join(d, filename)
                if os.path.isfile(f):
                    files.append(f)
    return files

def runTests():
    files = getFiles()
    num_tests = len(files)
    fail_count = 0
    
    print("Running {} tests...".format(num_tests))
    for f in files:
        p = multiprocessing.Process(target=executeTest, args=(f,))
        p.start()
        p.join(TIME_LIMIT)
        if p.is_alive():
            p.terminate()
            print('❌ {} failed!\n- Summary:\n\tTimed out! Your test took longer than {}s.\n\tThis limit can be modified in runner.py'.format(f, TIME_LIMIT))
            fail_count += 1
            p.join()
        else:
            if p.exitcode != 0:
                fail_count += 1

    if fail_count > 0:
        print('\n🚨 You passed {}/{} tests.'.format(num_tests - fail_count, num_tests))
    else:
        print('\n🚀 You passed all {} tests!\n'.format(num_tests))

#Asser implementation has been specified
if (IMPL == ""):
    print("❗️ You need to specificy your implementation path in runner.py!")
    exit(1)

runTests()
print("\nConsider adding your own tests cases to the repository so the whole class can benefit!\nhttps://github.com/zawie/z412L1\n")