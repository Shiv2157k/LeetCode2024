"""
Design Pattern:
---------------
In the movie ticket booking system, there can be multiple seat types for a cinema hall,
and each seat type will have its own formula to calculate the ticket fare.
Therefore, the Strategy design pattern can be applied here, which will design a separate strategy
or algorithm to calculate the price of each seat type.
It is applied through the definition of a function that provides the implementation of the rates for
each seat type using different strategies.
This strategy can also differ based on a movie’s popularity or taxes.
"""