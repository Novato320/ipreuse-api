from typing import Union
from enterprise import Enterprise

class User():
    def __init__(self):
        self.id: int
        self.company: Enterprise
        self.username: str
        self.email: Union[str, Email]
        self.password: str
        self.name: str
        self.phone: Union[str, Phone]
        self.is_active: bool
        self.created_at
        self.updated_at: Union[None]
        self.deleted_at: Union[None]
        

