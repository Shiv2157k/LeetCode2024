from .account import Player
from .constants import GameStatus
from typing import List
from .move import Move


class ChessGame:

    def __init__(self, players: List[Player], board: List[List[str]], current_turn: Player, status: GameStatus,
                 moves_played: int):
        self.__player = players
        self.__board = board
        self.__current_turn = current_turn
        self.__status = status
        self.__moves_played = moves_played

    def is_over(self):
        return self.__status != GameStatus.ACTIVE

    def player_move(self, player: Player, start_x: int, start_y: int, end_x: int, end_y: int):
        # 1. start box
        # 2. end box
        # 3. move
        # 4. call makeMove() method
        pass

    def make_move(self, move: Move, player: Player):
        # 1. Validation of source piece
        # 2. Check whether or not the color of the piece is white
        # 3. Check if it is a valid move or not
        # 4. Check whether it is a castling move or not
        # 5. Store the move
        pass