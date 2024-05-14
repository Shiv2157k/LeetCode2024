"""
Design Patterns:
----------------
The following design patterns have been used in the class diagram:

The Singleton design pattern:
-----------------------------
This pattern ensures the existence of a single instance of the ATM at a given moment
that can be accessed by multiple users, due to the shared nature of the ATM components.

The State design pattern:
-------------------------
This pattern enables the ATM to alter its behavior based on the internal changes in the machine.
This way, an ATM can transition from one state to another, like switching from an idle state to
displaying an account balance or money withdrawal state, and as soon as all the operations have
been performed, it can switch back to the initial idle state.


The following design patterns can also be used to design ATM:
-------------------------------------------------------------

The Composite design pattern can be used to combine different components of the ATM along with their functionalities.

The Builder design pattern allows the same processes for a complex object to have different representations.
In the ATM system, it can help separate different kinds of transactions like withdrawals, deposits, etc.

Additional Requirements:
------------------------
There is a chance that the interviewer might ask about the working of the cash withdrawal process.
How can it be implemented in our ATM system? This addition is a bit challenging since we need a system
that can withdraw the correct combinations of hundred, twenty, and two dollar bills, respectively,
according to the amount specified by the user.
The system also needs to work sequentially until the required amount is met.

We will use the Chain of Responsibility design pattern to tackle this addition to our system.
This design pattern will ensure the correct division of the dollar bills in the ATM by creating a
chain of handlers that forward the requests based on the situation until all the requirements are met.

We have created the following classes to implement the Chain of Responsibility design pattern:

CashWithdrawProcessor: This is associated with the CashWithdrawalState class.
---------------------
This abstract class is extended by HundredDollarWithdrawProcessor, TwentyDollarWithdrawProcessor,
and TwoDollarWithdrawProcessor.

HundredDollarWithdrawProcessor:
This class is derived from CashWithdrawProcessor and is responsible for withdrawing hundred-dollar bills
based on the requirement.

TwentyDollarWithdrawProcessor:
This class is derived from CashWithdrawProcessor and is responsible for withdrawing twenty-dollar bills
based on the requirement.

TwoDollarWithdrawProcessor:
This class is derived from CashWithdrawProcessor and is responsible for withdrawing two-dollar bills
based on the requirement.
"""
