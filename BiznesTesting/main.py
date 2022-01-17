from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from random import randint

url = "https://localhost:8080/"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url)

# SSL problem
driver.find_element(By.ID, "details-button").click()
driver.find_element(By.ID, "proceed-link").click()


def select_category(cid=0):
    categories = driver.find_element(By.CLASS_NAME, "subcategories-list").find_elements(By.TAG_NAME, "li")
    categories[cid].find_element(By.TAG_NAME, "a").click()


# select a product, it is required that the user is on the home page
def select_product(pid=0, cid=0):
    driver.find_element(By.ID, "category-17").find_element(By.TAG_NAME, "a").click()
    select_category(cid)
    products = driver.find_elements(By.CLASS_NAME, "product")
    products[pid].click()


def add_to_the_basket(quantity):
    quantity_input = driver.find_element(By.ID, "quantity_wanted")
    quantity_input.click()

    # we subtract 1 item because it is already in the shopping cart
    for _ in range(quantity - 1):
        quantity_input.send_keys(Keys.ARROW_UP)
    driver.find_element(By.CLASS_NAME, "add-to-cart").click()
    wait.until(presence_of_element_located((By.CSS_SELECTOR, ".close i")))
    wait.until(element_to_be_clickable((By.CSS_SELECTOR, ".close i")))
    driver.find_element(By.CSS_SELECTOR, ".close i").click()


def back_to_main_page():
    driver.find_element(By.CSS_SELECTOR, "nav ol li a").click()


def show_basket_and_remove_random_product():
    driver.find_element(By.CLASS_NAME, "cart-preview").click()
    products = driver.find_elements(By.CLASS_NAME, "cart-item")
    to_drop = products[randint(0, len(products) - 1)]
    to_drop.find_element(By.CLASS_NAME, "remove-from-cart").click()


def checkout():
    driver.find_element(By.CLASS_NAME, "checkout").click()
    driver.find_element(By.ID, "field-id_gender-1").click()
    driver.find_element(By.ID, "field-firstname").send_keys("Jeff")
    driver.find_element(By.ID, "field-lastname").send_keys("Bezos")
    driver.find_element(By.ID, "field-email").send_keys(f"jeff{randint(2077, 19640112)}@yoggm.com")  # 1secmail.org
    driver.find_element(By.ID, "field-password").send_keys("Come0nJeffrey")
    driver.find_element(By.ID, "field-birthday").send_keys("1964-01-12")
    driver.find_element(By.NAME, "optin").click()
    driver.find_element(By.NAME, "customer_privacy").click()
    driver.find_element(By.NAME, "newsletter").click()
    driver.find_element(By.NAME, "psgdpr").click()
    driver.find_element(By.CLASS_NAME, "continue").click()

    # continue the checkout
    # provide the address for delivery
    wait.until(presence_of_element_located((By.ID, "field-address1")))
    driver.find_element(By.ID, "field-address1").send_keys("Do Studzienki 39")
    driver.find_element(By.ID, "field-postcode").send_keys("80-227")
    driver.find_element(By.ID, "field-city").send_keys("Gdańsk")
    driver.find_element(By.ID, "field-phone").send_keys("882762901")
    driver.find_element(By.CLASS_NAME, "form-footer").find_element(By.TAG_NAME, "button").click()  # continue

    # delivery option
    wait.until(presence_of_element_located((By.ID, "delivery_option_2")))
    driver.find_element(By.ID, "delivery_option_2").click()
    driver.find_element(By.NAME, "confirmDeliveryOption").click()

    # payment
    wait.until(presence_of_element_located((By.ID, "payment-option-2")))
    driver.find_element(By.ID, "payment-option-2").click()
    driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    driver.find_element(By.ID, "payment-confirmation").find_element(By.TAG_NAME, "button").click()


def order_details():
    wait.until(presence_of_element_located((By.CLASS_NAME, "account")))
    driver.find_element(By.CLASS_NAME, "account").click()
    driver.find_element(By.ID, "history-link").click()
    driver.find_element(By.CLASS_NAME, "order-actions").find_elements(By.TAG_NAME, "a")[0].click()


# MAIN SCRIPT

for i in range(7):
    select_product(pid=i, cid=1)
    add_to_the_basket(randint(1, 5))
    back_to_main_page()

for i in range(3):
    select_product(pid=i, cid=4)
    add_to_the_basket(randint(1, 5))
    back_to_main_page()

show_basket_and_remove_random_product()
checkout()
order_details()
