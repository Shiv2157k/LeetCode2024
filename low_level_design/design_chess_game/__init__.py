"""
The following design patterns have been used in the class diagram:

Singleton design pattern:
-------------------------
This pattern ensures the existence of a single instance of the chessboard at a given moment due to the shared
nature of the chessboard as a resource. Multiple instances can cause the game state to become inconsistent.

Command design pattern:
-----------------------
This pattern is used to encapsulate the move logic for each chess piece.
Each chess piece has its own implementation of the move command,
which allows it to move according to the rules defined for it.
For example, the knight moves in an L-shape pattern,
or the rook can move only horizontally or vertically on any number of boxes.

The following design patterns can also be used to design chess:
---------------------------------------------------------------

The Iterator design pattern would enable the game to move sequentially by allowing the pieces
----------------------------
to behave in a uniform manner where the user does not need to know the specifications or underlying
logic behind the moves of the pieces.

The State design pattern ensures the encapsulation of the state logic of each piece,
------------------------
since all the chess pieces have their own respective implementations of checkmate states
which makes them behave differently from each other depending on the situation.

The Observer design pattern enables the chess pieces to act as observers where the chessboard is the subject.
---------------------------
As soon as the state of the board changes, the pieces are notified to adapt to the changes accordingly.
This decouples the pieces from the chessboard.
"""