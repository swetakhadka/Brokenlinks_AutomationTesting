import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Open the website
print('here')
driver.get("https://www.siam99.com/")
driver.maximize_window()

# Define the scroll pause time
time.sleep(3)

# Initialize a variable to store the last height of the page
page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 100
scroll_iteration = int(page_height / scroll_speed)
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(0.1)

time.sleep(2)

def scroll_up():
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, -{scroll_speed});")
        time.sleep(0.1)

scroll_up()





time.sleep(3)
# threebar_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/span")
# threebar_button.click()
# time.sleep(2)

# promotion_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div[2]/div[2]/a[2]/span[2]")
# promotion_btn.click()
# time.sleep(2)
# WebDriverWait(driver, 30 ).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/button[1]/span")))
#
# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
# banners = soup.find_all('div', attrs={'class': 'promotion-card-wrapper'})
#
# time.sleep(4)
# for index, banner in enumerate(banners):
#     link = banner.find('a')['href'] if banner.find('a') else None
#     image = banner.find('img')['src'] if banner.find('img') else None
#     title = banner.find('div', class_='promotion-card-wrapper').text.strip() if banner.find('div', class_='promotion-card-wrapper') else None
#     print(f"Banner {index + 1}:")
#     print(f"Title: {title}")
#     print(f"Link: {link}")
#     print(f"Image: {image}")
#     print()
#     current_index = index + 1
#
#     banner_xpath = "(//div[@class='promotion-card-wrapper'])[" + str(current_index) + "]"
#
#
#
#     # Perform any actions on the new page
#     time.sleep(3)
#
#     # Go back to the promotions page
#     driver.back()
#     time.sleep(9)

# Close the browser after finishing
login_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/a[1]")
login_button.click()
time.sleep(2)




username_button = driver.find_element(By.XPATH, " //input[@id='nK7dDJpdOWE_8']")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
password_button = driver.find_element(By.XPATH, " //input[@id='nK7dDJpdOWE_9']")

usernamearr = ["thb001"]
passwordarr = ["Welcome1"]
for username, password in zip(usernamearr, passwordarr):

    username_button.click()
    username_button.send_keys(Keys.CONTROL + "a")
    username_button.send_keys(Keys.DELETE)
    time.sleep(1)
    password_button.click()
    password_button.send_keys(Keys.CONTROL + "a")  # Select all text
    password_button.send_keys(Keys.DELETE)

    username_button.send_keys(username)
    time.sleep(0.1)  # Short delay to mimic human typing
    password_button.send_keys(password)
    time.sleep(2)

    submit_button.click()

    time.sleep(1)


try:
     home_page_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='focus:outline-none focus-visible:outline-0 disabled:cursor-not-allowed disabled:opacity-75 flex-shrink-0 min-w-//span[@class='text-[14px] md:text-[1rem]'][normalize-space()='13,045.00']"))
    )
     print("Successfully navigated to the home page!")
except Exception as e:
     print("Failed to navigate to the home page:", e)
driver.implicitly_wait(10)
banners = driver.find_elements(By.CLASS_NAME, "game-holder")
print(f"Found {len(banners)} game holders.")

for index in range(len(banners)):
    banners = driver.find_elements(By.CLASS_NAME, "game-holder")

    driver.execute_script("arguments[0].scrollIntoView();", banners[index])
    # Click on the banner
    banners[index].click()
    print(f"Clicked on game holder {index + 1}")

    time.sleep(3)

    driver.back()
    time.sleep(3)

time.sleep(4)
driver.quit()


