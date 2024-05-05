from dataclasses import dataclass


@dataclass
class Address:
    street_address: str
    city: str
    state: str
    zip_code: str
    country: str