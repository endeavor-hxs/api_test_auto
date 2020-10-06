from api_test.api_page.address_page import AddressPage


class TestAddressPage:

    def setup(self):
        self.address_page = AddressPage( )

    def test_increase(self):
        inrcrea_depart = self.address_page.incre_depart( )
        print(inrcrea_depart)
        assert inrcrea_depart['errcode'] in [0, 60008]

    def test_update(self):
        update_depart = self.address_page.update_depart( )
        print(update_depart)
        assert update_depart['errcode'] in [0, 60008]

    def test_deldepart(self):
        del_depart = self.address_page.del_depart( )
        print(del_depart)
        assert del_depart['errcode'] in [0, 60008]

    def test_getlist(self):
        getlist_depart = self.address_page.getlist_derpart( )
        print(getlist_depart)
        assert getlist_depart['errcode'] in [0, 60008]
