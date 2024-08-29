# README for ConcurrentProgramming

The following information is from Codecademy.

> In this project, you are going to be calculating the average of three lists
> using four different approaches:
> - sequential approach
> - async approach
> - threading approach
> - multiprocessing approach
> Your goal will be to make this calculation as efficient as possible and see 
> which approaches work well and which ones struggle.

## The below metadata is from Codecademy
Before diving in, look at the starter code in script.py. There are six functions defined:

`cal_average()`
This helper function takes in a list of numbers, `num`, and calculates the average of the numbers within the list. Notice that we have added a `time.sleep(1)` line before returning the average. This extra second is an added barrier to test the efficiency of each approach, as you will use this helper function in your sequential, threading, and multiprocessing programs.

`main_sequential()`
This is where you will write your sequential program. The lines `s = time.perf_counter()` and `elapsed = time.perf_counter() - s` are there to time your program (they are in the rest of the functions as well.).

`cal_average_async()`
This helper function is the same as `calc_average()` except it is an asynchronous function you will use for your async program.

`main_async()`
This is where you will write your async program.

`main_threading()`
This is where you will write your threading program.

`main_multiprocessing()`
This is where you will write your multiprocessing program.

Finally, the code after `main_multiprocessing()` tests your sequential, async, threading, and multiprocessing functions for you each time your run script.py. There is no need to touch it during the project