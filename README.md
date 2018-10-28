# RecursiveFunctionPlotter
A function to give a better intuition of how recursive functions work.

Should help you keep track of how variables are changing in recursive functions, especially multiple recursive functions.

Run this line in MATLAB

y=recurplot(x,n)

Where 'x' is the size of your call stack
and 'n' is the number of recursive calls within the function (positive integer values only).
Then a plot showing how the x value changes with each step in the recursion scope will pop up.

Attached Example Fig has x=4 and n=3. Three recursive calls with a size 4 call stack.
The decreasing portion of the graph should represent when a new stack is made and increasing portions should represent when the value is returned.

Where would you use this?
Not really sure. Maybe if you want to make some fractal plots.


_

Edit 10/3/18
Python version attached. Uses python 2.7 but 3.7 should be fine.

type "run recurplot" in ipython or equivalent and use as described above.


## General Considerations ##
These functions will grow as roughly ~ n^x
Try to keep the total number below 1e6.
