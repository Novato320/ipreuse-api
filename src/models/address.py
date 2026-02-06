from typing import Union

class Address():
    def __init__(self):
        self.id: int
        self.zipcode
        self.country
        self.state
        self.city
        self.street
        self.address_line_2: Union[None, str]
        self.number
        self.land_mark: Union[None, str]
        self.created_at
        self.updated_at