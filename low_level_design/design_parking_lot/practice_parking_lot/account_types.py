from constants import AccountStatus, Person


class Account:

    def __init__(self, username: str, password: str, person: Person, status=AccountStatus.ACTIVE):
        self.__username = username
        self.__password = password
        self.__person = person
        self.__status = status


class Admin(Account):

    def __init__(self, username: str, password: str, person: Person, status=AccountStatus.ACTIVE):
        super().__init__(username, password, person, status)

    def add_parking_floor(self, floor: str):
        None

    def add_parking_spot(self, floor: str):
        None

    def add_parking_display_board(self, floor_name: str, display_board: ParkingDisplayBoard):
        None

    def add_customer_info_panel(self, floor_name: str, info_panel: str):
        None

    def add_entrance_panel(self, entrance_panel: str):
        None

    def add_exit_panel(self, exit_panel: str):
        None


class Attendant(Account):
    def __init__(self, username: str, password: str, person: Person, status=AccountStatus.ACTIVE):
        super().__init__(username, password, person, status)

    def process_ticker(self, ticket_number: int):
        None
