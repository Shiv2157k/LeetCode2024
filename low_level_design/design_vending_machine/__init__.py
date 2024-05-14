"""
We have used the State design pattern to design this problem because,
                 --------------------
in different states, we perform different or specific tasks according to the state.
The vending machine changes its behavior based on its state.
The different states within the system are listed below:
- No money inserted state
- Money inserted state
- Dispense state

All these states have the same methods but the implementation of each method in each state changes
with the change of the state.

Vending Machine will be implemented using Singleton Pattern.
                                         -------------------
"""