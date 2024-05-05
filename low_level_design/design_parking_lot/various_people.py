from low_level_design.design_parking_lot.parking_lot_enums import AccountStatus


class Account:

    def __init__(self, username: str, password: str, person: str, status=AccountStatus.ACTIVE):
        self.__username = username
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        None


class Admin(Account):

    def __init__(self, username, password, person, status: AccountStatus.ACTIVE):
        super().__init__(username, password, person, status)

    def add_parking_floor(self, floor):
        None

    def add_parking_spot(self, floor_name, spot):
        None

    def add_parking_display_board(self, floor_name, display_board):
        None

    def add_customer_info_panel(self, floor_name, info_panel):
        None

    def add_entrance_panel(self, entrance_panel):
        None

    def add_exit_panel(self, exit_panel):
        None


class ParkingAttendant(Account):
    def __init__(self, username, password, person, status=AccountStatus.ACTIVE):
        super().__init__(username, password, person, status)

    def process_ticket(self, ticket_number):
        None
