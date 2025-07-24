from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_customer(
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
):
    """
    Fill out the customer form and submit it.
    """
    driver.find_element(By.ID, "surname").send_keys(surname)
    driver.find_element(By.ID, "firstname").send_keys(firstname)
    driver.find_element(By.ID, "address").send_keys(address)
    driver.find_element(By.ID, "season").send_keys(season)
    driver.find_element(By.ID, "rims").send_keys(rims)
    driver.find_element(By.ID, "brand_front").send_keys(brand_front)
    driver.find_element(By.ID, "width_front").send_keys(width_front)
    driver.find_element(By.ID, "ratio_front").send_keys(ratio_front)
    driver.find_element(By.ID, "diameter_front").send_keys(diameter_front)
    driver.find_element(By.ID, "fl").send_keys(fl)
    driver.find_element(By.ID, "fr").send_keys(fr)
    driver.find_element(By.ID, "rl").send_keys(rl)
    driver.find_element(By.ID, "rr").send_keys(rr)
    driver.find_element(By.ID, "brand_rear").send_keys(brand_rear)
    driver.find_element(By.ID, "width_rear").send_keys(width_rear)
    driver.find_element(By.ID, "ratio_rear").send_keys(ratio_rear)
    driver.find_element(By.ID, "diameter_rear").send_keys(diameter_rear)
    driver.find_element(By.ID, "note").send_keys(note)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    ).click()

def edit_customer(driver, old_surname, new_surname):
    """
    Find a customer by surname and update the surname.
    """
    rows = driver.find_elements(By.XPATH, '//*[@id="customer-list"]/table/tr')
    for row in rows:
        cell_text = row.find_element(By.XPATH, "./td[1]").text.strip()
        if cell_text.startswith(old_surname):
            edit_button = row.find_element(By.XPATH, "./td[5]/button[1]")
            edit_button.click()
            break

    input_surname = driver.find_element(By.ID, "surname")
    input_surname.clear()
    input_surname.send_keys(new_surname)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    ).click()

def delete_customer(driver, surname):
    """
    Find a customer by surname and delete the row.
    """
    rows = driver.find_elements(By.XPATH, '//*[@id="customer-list"]/table/tr')
    for row in rows:
        cell_text = row.find_element(By.XPATH, "./td[1]").text.strip()
        if cell_text.startswith(surname):
            delete_button = row.find_element(By.XPATH, "./td[5]/button[2]")
            delete_button.click()
            break

def customer_exists(driver, surname):
    """
    Check if a customer with the given surname exists in the table.
    """
    rows = driver.find_elements(By.CSS_SELECTOR, "#customer-list table tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells and cells[0].text.startswith(surname):
            return True
    return False
