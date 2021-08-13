I see potential for a pure shell version
\


https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/

https://stackoverflow.com/questions/22891583/can-i-generate-authentic-random-number-with-python

https://www.pcg-random.org/index.html


https://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-milliseconds



4

There may already be a function to do what you're looking for, but I don't know about it (yet?). In the meantime, I would suggess using:

ran_floats = numpy.random.rand(50) * (13.3-0.5) + 0.5
This will produce an array of shape (50,) with a uniform distribution between 0.5 and 13.3.

You could also define a function: