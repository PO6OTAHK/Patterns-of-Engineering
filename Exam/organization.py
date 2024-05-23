from single import single

class organization(single):

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return str(self._id.hex)
    
    @property
    def address(self):
        return self._address
    
    @property
    def mail_index(self):
        return self._mail_index