from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import csv

# Path to your Chromedriver
chromedriver_path = './chromedriver'
# Define the proxy settings
proxy = "135.245.192.7:8000"  # Replace with your proxy address and port

# Setup the Chrome service and options
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'

# Add headless option
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--window-size=1920,1080')
options.add_argument('--log-level=DEBUG')
options.add_argument('--enable-logging')
options.add_argument('--v=1')
options.add_argument(f'--proxy-server={proxy}')

# Initialize the Chrome driver
loginUrl = f"https://login.microsoftonline.com/5d471751-9675-428d-917b-70f44f9630b0/oauth2/authorize?client%5Fid=00000003%2D0000%2D0ff1%2Dce00%2D000000000000&response%5Fmode=form%5Fpost&response%5Ftype=code%20id%5Ftoken&resource=00000003%2D0000%2D0ff1%2Dce00%2D000000000000&scope=openid&nonce=A3976435C0716BA7AD8779FA107916DD849751E41D6BC8AC%2D7F221CFB62468441F29E7845308D4D86CE6702C50DFC359AB6B63D6E1B9BA2A2&redirect%5Furi=https%3A%2F%2Fnokia%2Esharepoint%2Ecom%2F%5Fforms%2Fdefault%2Easpx&state=OD0w&claims=%7B%22id%5Ftoken%22%3A%7B%22xms%5Fcc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083%2D87e0%2D41b5%2Dbb78%2D0bc43c8a8e8a&client%2Drequest%2Did=3a053fa1%2D80bd%2D9000%2D602e%2Dd5dc3ad9a345"


def login(driver):
    # Open the login web page
    driver.get(loginUrl)
    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)

    username_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "loginfmt"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", username_input)
    username = input("Please enter your email: ")
    username_input.send_keys(username)

    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()

    password_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "passwd"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", password_input)
    password = input("Please enter your password: ")
    password_input.send_keys(password)

    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "idSIButton9"))
    )
    submit_button.click()
    print("submit done")

    WebDriverWait(driver, 60).until(
        EC.title_contains("SharePoint")
    )
    print("login done")


def submit_link(driver, url):
    driver.get(url)
    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)

    WebDriverWait(driver, 30).until(
        EC.title_contains("Achievement Center")
    )

    try:
        # Wait until submit button is present and clickable
        button = WebDriverWait(
            driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[text()='Submit']]")))
    except Exception as e:
        print("Submit already.")
        return

    print("Button display status:", button.is_displayed())
    print("Button enable status:", button.is_enabled())
    driver.execute_script("arguments[0].click();", button)

    # Check result
    notification = WebDriverWait(
        driver,
        10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div/p[contains(text(), 'Your attendance to the session is confirmed')]")))
    print("Notification text:", notification.text)

    if button.is_displayed() and button.is_enabled():
        print("The button is still clickable.")
    else:
        print("The button is not clickable.")


def main():
    global driver
    try:
        driver = webdriver.Chrome(service=service, options=options)
        login(driver)

        # Open and read the CSV file
        with open("./input.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                submit_link(driver, row[0].strip())
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
