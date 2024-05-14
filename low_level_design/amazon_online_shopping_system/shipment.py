class Shipment:

    def __init__(self, shipment_number, shipment_date, estimated_arrival, shipment_method, shipment_logs):
        self.__shipment_number = shipment_number
        self.__shipment_date = shipment_date
        self.__estimated_arrival = estimated_arrival
        self.__shipment_method = shipment_method
        self.__shipment_logs = shipment_logs # List of shipment logs

    # shipment_log here refers to an instance of the ShipmentLog class
    def add_shipment_log(self, shipment_log):
        pass


class ShipmentLog:

    def __init__(self, shipment_number, creation_date, status):
        self.__shipment_number = shipment_number
        self.__creation_date = creation_date
        self.__status = status # Refers to the ShipmentStatus enum
