import uuid

class single():
    _id = None
    _name = ""
    _address = ""
    _mail_index = None

    def __init__(self, name = None):
        self._id = uuid.uuid4()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.strip()
    
    @property
    def id(self):
        return str(self._id.hex)  
    
    @id.setter
    def id(self, value:uuid.UUID ):
        self._id = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def mail_index(self):
        return self._mail_index
        
    @mail_index.setter
    def mail_index(self, mail_index):
        if (type(mail_index) == int) and (mail_index >= 0):
            self._mail_index = mail_index
        else:
            raise ValueError