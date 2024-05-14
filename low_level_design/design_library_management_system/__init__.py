"""
We can apply the Factory design pattern to create objects and mandate that they go via a single factory.
                -----------------------
For example, we can create a BookFactory class to create a book object in an arranged manner.

Similarly, we can use the Delegation design pattern to delegate a task from one class to another class.
                         ---------------------------
For example, librarian functionalities like adding book items, deleting book items, or modifying
book items are actually implemented in the BookItem class.
The Librarian class uses the BookItem class and has access to its data and methods.

Moreover, we can use the Observer design pattern to notify library members.
                        -------------------------
For example, if a member searches for a book that is unavailable at that time,
then the observer interface system will notify the member when that book is available for reservation.
"""