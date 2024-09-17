import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

def check_url_status(url):
    try:
        response = requests.head(url, timeout=5)  # HEAD request to get just the status code
        return response.status_code
    except requests.RequestException as e:
        print(f"Failed to check URL {url}: {e}")
        return None



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.losheaven.com")
driver.maximize_window()

# Wait until the page is fully loaded
WebDriverWait(driver, 5).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

print("Page is fully loaded")

# Wait for all images to be loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

# Find all images on the page
banners = driver.find_elements(By.TAG_NAME, "img")

print(f"Found {len(banners)} total images")

# Loop through the images and click them one by one
for img_index in range(len(banners)):
    try:
        # Refetch images to avoid stale element reference
        banners = driver.find_elements(By.TAG_NAME, "img")
        print(f"Clicking on image {img_index + 1}")

        # Scroll the image into view (optional, depending on the page layout)
        driver.execute_script("arguments[0].scrollIntoView();", banners[img_index])

        # Click the image
        banners[img_index].click()
        print(f"Clicked on image {img_index + 1}")

        # Wait for 3 seconds to let the new page load (adjustable)
        time.sleep(3)

        # Go back to the previous page
        driver.back()

        # Wait for the page to load again after going back
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        print("Returned to the main page")

    except (ElementClickInterceptedException, StaleElementReferenceException) as e:
        print(f"Error clicking on image {img_index + 1}: {e}")
        continue


print("checking all the images on a page")

for index, image in enumerate(banners):
    img_url = image.get_attribute("src")
    if img_url:
        status = check_url_status(img_url)
        if status == 200:
            print(f"Image {index + 1}: {img_url} is valid (Status: {status})")
        else:
            print(f"Image {index + 1}: {img_url} is broken (Status: {status})")
    else:

        print(f"Image {index + 1} has no 'src' attribute.")

# Quit the browser at the end

print("checking that there is broken links or not ")

links = driver.find_elements(By.TAG_NAME, "a")
for index, link in enumerate(links):
    link_url = link.get_attribute("href")
    if link_url:
        status = check_url_status(link_url)
        if status == 200:
            print(f"link {index + 1}: {link_url} is valid (Status: {status})")
        else:
            print(f"link {index + 1}: {link_url} is broken (Status: {status})")
    else:

        print(f"link {index + 1} has no 'href' attribute.")
driver.quit()
