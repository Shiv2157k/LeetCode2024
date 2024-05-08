class Library:

    def __init__(self):
        self.name = None
        self.address = None

    def get_address(self):
        return self.address

    _library = None

    @classmethod
    def get_instance(cls):
        if cls._library is None:
            cls._library = cls()
        return cls._library
