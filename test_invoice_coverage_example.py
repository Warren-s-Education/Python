import pytest
from invoice_coverage_example import Invoice, Item


def test_generate_invoice():
    client_name = "Acme Inc."
    items = [Item("item1", 10.5), Item("item2", 20.0)]
    invoice = Invoice(client_name, items)
    assert invoice.generate_invoice(
    ) == "Invoice for Acme Inc.:\n- item1: 10.5$\n- item2: 20.0$\nTotal: 30.5$"


def test_send_invoice():
    client_name = "Acme Inc."
    items = [Item("item1", 10.5), Item("item2", 20.0)]
    invoice = Invoice(client_name, items)
    assert invoice.send_invoice() == None  # assuming send_invoice returns nothing


# def test_total_amount_calculation():
#     client_name = "Acme Inc."
#     items = [Item("item1", 10.5), Item("item2", 20.0)]
#     invoice = Invoice(client_name, items)
#     assert invoice.total_amount == 30.5


def test_negative_amount_raises_error():
    client_name = "Acme Inc."
    items = [Item("item1", -10.5), Item("item2", 20.0)]
    with pytest.raises(ValueError):
        invoice = Invoice(client_name, items)
