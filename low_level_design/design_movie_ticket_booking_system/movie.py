class Movie:

    def __init__(self, title, genre, language, release_date, duration):
        self.__title = title
        self.__genre = genre
        self.__language = language
        self.__release_date = release_date
        self.__duration = duration


class ShowTime:

    def __init__(self, show_id, start_time, date, duration):
        self.__show_id = show_id
        self.__start_time = start_time
        self.__date = date
        self._duration = duration


class MovieTicket:

    def __init__(self, ticket_id, seat, movie, show):
        self.__ticket_id = ticket_id
        self.__seat = seat
        self.__movie = movie
        self.__show = show
