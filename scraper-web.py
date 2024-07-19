from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

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
options.add_argument(f'--proxy-server={proxy}')
options.add_argument('--enable-logging')
options.add_argument('--v=1')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Open the desired web page
driver.get("https://nokia.sharepoint.com/sites/learn/achiev/SitePages/index.aspx/reward/998546425")
#driver.get("https://www.baidu.com")  do not use proxy for baidu

try:

    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)
    page_content = driver.page_source
    print(page_content)

    buttons = driver.find_elements(By.TAG_NAME, "button")

    # Print the attributes of each button
    for button in buttons:
        print("Button text:", button.text)
        print("Button class:", button.get_attribute("class"))

    # Wait until the button is present and clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Submit']]"))
    )

    # Click the button
    button.click()

finally:
    # Quit the browser
    driver.quit()

