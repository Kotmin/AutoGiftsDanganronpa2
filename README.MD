


You need to know that this simple script is not a free Steam achievements achiever.

This is just a simple project to improve my programming skills.

You use it at your own risk.
--------------

SOURCES AND NOTES
---------------
I see potential for a pure shell version



https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/

https://stackoverflow.com/questions/22891583/can-i-generate-authentic-random-number-with-python

https://www.pcg-random.org/index.html


https://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-milliseconds


There may already be a function to do what you're looking for, but I don't know about it (yet?). In the meantime, I would suggess using:

ran_floats = numpy.random.rand(50) * (13.3-0.5) + 0.5
This will produce an array of shape (50,) with a uniform distribution between 0.5 and 13.3.

=======
LINUX:

NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev


-------------------------------------------



