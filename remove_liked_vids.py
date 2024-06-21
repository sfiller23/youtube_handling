import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#start chrome with remote debugging port:
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome #--remote-debugging-port=9222 --disable-web-security --user-data-dir=/#tmp/chrome_dev_test

# Get the current working directory
current_directory = os.getcwd()

# Path to your ChromeDriver in the current directory
chrome_driver_path = os.path.join(current_directory, 'chromedriver')  # Ensure 'chromedriver' is in the current directory

# Ensure ChromeDriver has execute permissions
if not os.access(chrome_driver_path, os.X_OK):
    os.chmod(chrome_driver_path, 0o755)

# Initialize the service for ChromeDriver
service = Service(chrome_driver_path)

# Chrome options to connect to the remote debugging port
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
chrome_options.add_argument("--disable-web-security")

# Initialize the browser
browser = webdriver.Chrome(service=service, options=chrome_options)

# Function to log in to YouTube
def login_youtube():
    browser.get('https://www.youtube.com')
    time.sleep(5)  # Wait for the page to load
    # Add your login steps here if not already logged in

# Function to clear the "Liked Videos" playlist
def clear_liked_videos():
    browser.get('https://www.youtube.com/playlist?list=LL')
    time.sleep(5)  # Wait for the page to load
    while True:
        try:
            remove_buttons = browser.find_elements(By.CSS_SELECTOR, 'button[aria-label="Remove from Liked videos"]')
            if not remove_buttons:
                break
            for button in remove_buttons:
                button.click()
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            break

# Login to YouTube
login_youtube()

# Clear the "Liked Videos" playlist
clear_liked_videos()

# Close the browser
browser.quit()