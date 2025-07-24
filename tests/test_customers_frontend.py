# Test suite for customer functionality via frontend automation (Selenium)
from utils import add_customer, customer_exists, delete_customer, edit_customer

# Test data
surname = "Smith"
new_surname = "Olderson"
firstname = "John"
address = "4188 Linden Avenue, Lake Buena Vista"
season = "Summer"
rims = "Alloy rims"
brand_front = "Pirelli"
width_front = "225"
ratio_front = "45"
diameter_front = "17"
fl = "6"
fr = "6"
rl = "5"
rr = "5"
brand_rear = "Pirelli"
width_rear = "225"
ratio_rear = "45"
diameter_rear = "17"
note = "A/5/17"

def test_add_customer(driver):
    """
    Test adding a new customer from the frontend.
    """
    add_customer(
        driver,
        surname,
        firstname,
        address,
        season,
        rims,
        brand_front,
        width_front,
        ratio_front,
        diameter_front,
        fl,
        fr,
        rl,
        rr,
        brand_rear,
        width_rear,
        ratio_rear,
        diameter_rear,
        note,
    )
    assert customer_exists(driver, surname), "Customer was not added successfully"

def test_edit_customer(driver):
    """
    Test editing a customer's surname via the frontend.
    """
    edit_customer(driver, surname, new_surname)
    assert customer_exists(driver, new_surname), "Customer was not updated successfully"
    assert not customer_exists(driver, surname), "Old surname is still present after update"

def test_add_delete(driver):
    """
    Test deleting a customer via the frontend.
    """
    delete_customer(driver, new_surname)
    assert not customer_exists(driver, surname), "Customer was not deleted successfully"
