from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://artio.faucet.berachain.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Wallet Address"))
    )

    button = driver.find_element(By.ID, "Click here to prove you are not a bot")
    button.click()

finally:
    driver.quit()
