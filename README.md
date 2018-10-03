# RecursiveFunctionPlotter
A function to give a better intuition of how recursive functions work.

I've always had trouble keeping track of variables in recursive functions, especially multiple recursive functions.

Run this line in MATLAB

y=recurplot(x,n)

Where 'x' is the size of your call stack
and 
'n' is the number of recursive calls within the function.
Then a plot showing how the x value changes with each step in the recursion scope will pop up.

Attached Example Fig has x=4 and n=3.


Where would you use this?
Not really sure. Maybe if you want to make some fractal plots.



Edit 10/3/18
Python version attached. Uses python 2.7 but 3.7 should be run
type "run recurplot" in ipython or equivalent and use as described above.
