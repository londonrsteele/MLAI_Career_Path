# Filename : My_HOFs.py
# Author   : LR Steele
# Info     : Coding project/objective for "SWE in Python I" section of SWE for
#          : ML/AI Engineers course in Machine Learning/AI Engineer Career Path
#          : on Codecademy.
# NOTE     : Any comments enclosed with "" are from Codecademy prompts
# Data     : see 1kSalesRec_README.md for more information
import csv
from functools import reduce

#############################################
# count function
#############################################
def count(predicate, iterable):
    # "Inside the count() function, write a filter() function that will “filter”
    # iterable based on predicate. Save this value to a variable called 
    # count_filter."
    count_filter = filter(predicate, iterable)
    # "Inside of count(), use reduce() to process the iterator returned from 
    # filter() so the accumulator imcrements by one for each True evaluation 
    # from filter()."
    # "x will be the current accumulated value from previous evaluations, and
    # y will be the current value given to the accumulator."
    count_reduce = reduce(lambda x, y: x+1, count_filter, 0)
    return count_reduce


# "Let's create the average() function that will compute an average recursively."
# "The average() function will contain a helper function called avg_helper()
# that will be responsible for implementing a loop to compute an average."
#############################################
# average helper function
#############################################
def avg_helper(curr_count, iterable, curr_sum):
    # "We want avg_helper() to implement the following loop recursively:"
    # curr_count = 0
    # curr_sum = 0
    # for i in iterable:
    #     curr_sum += i
    #     curr_count += 1
    # "In our case, curr_sum will be provided from the function call. 
    # To obtain the next value in an iterable (if there is one), we have to 
    # use next(). If there are no more elements to obtain from the iterable,
    # next() should return the string “null”."
    next_value = next(iterable, "null")
    # "A recursive function performs the next iteration in the loop by making
    # a call to itself and terminates the loop when a base case is reached. In 
    # our case, the loop should terminate when all the elements in the iterable 
    # are processed; i.e., next() returns "null". When next() returns "null", 
    # avg_helper() should compute the average and return that value."
    # BASE CASE
    if next_value == "null":
        return curr_sum/curr_count
    # COMPUTATION
    # else, update the values
    curr_count += 1
    curr_sum += next_value
    # RECURSIVE CALL
    # "The next iteration of the loop is computed by making a call to avg_helper()
    # with the new curr_count and curr_sum supplied."
    return avg_helper(curr_count, iterable, curr_sum)

    
#############################################
# average function
#############################################
def average(itr):
    # "If itr is not iterable, this will generate an iterator."
    iterable = iter(itr) 
    # "Make the initial call to avg_helper() with the proper initial values for
    # curr_count and curr_sum. Return the value found by avg_helper."
    return avg_helper(0, iterable, 0)


# "You will now use yoru count() and average() functions on data obtained from 
# a CSV file called 1kSalesRec.csv" (see the README for more information)
#############################################
# read data from 1kSalesRec.csv
#############################################
with open('MLAI_Career_Path\\SWE in Python\\My Higher Order Functions\\1kSalesRec.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)
    # "Use your count() function to count the number of orders for the country
    # "Belgium". Recall that a record is read in a list. In this case, Country
    # is the 2nd item in the list (index 1)."
    belgiums = count(lambda x: x[1]=="Belgium", reader)
    print(belgiums)

    # Go back to top of file
    csvfile.seek(0)

    # "Use your average() function to compute the average total profit (index 13)
    # for Portugal. Note: the entries in the list that represents the records are
    # all of type string. You must convert them to float by using float()."
    avg_portugal = average(map(lambda x: float(x[13]), filter(lambda record: record[1]=="Portugal",reader)))
    print(avg_portugal)

