from constants import Person, AccountStatus


class Account:

    def __init__(self, id, password, status):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        pass


class Player(Account):

    def __init__(self, id: str, password: str, status: AccountStatus, person: Person, total_games_played: int,
                 white_side: bool = False):
        super().__init__(id, password, status)
        self.__person = person
        self.__total_games_played = total_games_played
        self.__white_side = white_side

    def is_white_side(self):
        return self.__white_side
