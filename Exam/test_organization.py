import unittest
from organization import organization
from single import single

class test_organization(unittest.TestCase):
    def setUp(self):
        self.organization = organization()
        self.single = single()
    
    def test_set_get_id(self):
        single._id = 0
        assert organization._id == 0
    
    def test_set_get_name(self):
        single._name = "Bimba"
        assert organization._name == "Bimba"

    def test_set_get_address(self):
        single._address = "г. Иркутск. ул. Лермонтова 126/6"
        assert organization._address == "г. Иркутск. ул. Лермонтова 126/6"

    def test_set_get_mail_index(self):
        single._mail_index = 600054
        assert organization._mail_index == 600054

if __name__ == "__main__":
    unittest.main()