
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

# Create ChromeOptions instance and enable performance logging
options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Initialize WebDriver with the configured options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Open the homepage
driver.get("https://web.apehoops.com/")  # Replace with your homepage URL

# Retrieve network logs
logs = driver.get_log('performance')

# Set to store image URLs from the network logs
network_image_urls = set()

# Process the logs to find image URLs
for log in logs:
    message = json.loads(log['message'])  # Parse the JSON message
    method = message['message']['method']  # Get the method from the log

    # Check for the 'responseReceived' event
    if method == "Network.responseReceived":
        params = message['message']['params']
        response = params.get('response', {})
        url = response.get('url')

        # Check if the URL is an image
        if url and (url.endswith('.jpg') or url.endswith('.png') or url.endswith('.gif') or url.endswith('.jpeg')):
            network_image_urls.add(url)  # Add the URL to the set

# Get all image elements from the webpage
elements_image_urls = set()
image_elements = driver.find_elements(By.TAG_NAME, 'img')

# Extract the src attribute from each image element
for img in image_elements:
    src = img.get_attribute('src')
    if src:
        elements_image_urls.add(src)

box_find

# Compare the two sets of URLs
missing_in_elements = network_image_urls - elements_image_urls
missing_in_network = elements_image_urls - network_image_urls

# Print the results
if not missing_in_elements and not missing_in_network:
    print("All image URLs match between the network tab and the webpage elements.")

else:
    if missing_in_elements:
        print("These image URLs are found in the network logs but not in the webpage elements:")
        print(missing_in_elements)
        for url in missing_in_elements:
            print(url)
    if missing_in_network:
        print("These image URLs are found in the webpage elements but not in the network logs:")
        for url in missing_in_network:
            print(url)

# Close the driver
driver.quit()

