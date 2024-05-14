"""
Design Pattern:
---------------
The Strategy design pattern is applied here,
    ----------------------
which will design a separate strategy or algorithm to calculate the rate of each room.

The Hotel class follows the Singleton design pattern,
                            -------------------------
because there will only be a single instance of the Hotel class.

Inside the hotel management system, there can be multiple rooms in a hotel,
and each room has its own formula for calculating the booking cost.
Therefore, Room and related classes incorporate the properties of the Factory design pattern.
                                                                     ------------------------
"""