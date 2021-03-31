import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_can_calculate_total_impure_price(invoice, products):
    invoice.total_impure_price(products)
    assert invoice.total_impure_price(products) == 75
    
def test_can_calculate_total_discount(invoice, products):
    invoice.total_discount(products)
    assert invoice.total_discount(products) == 5.62
    

def test_can_calculate_invoice_class(products):
    invoice = Invoice()
    invoice.total_impure_price(products)
    assert invoice.total_impure_price(products) == 75
