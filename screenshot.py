#10.	How to select an element, highlight it with the colour with specific set of square
# box and then take a screenshot?

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup driver (Chrome example)
driver = webdriver.Chrome()
driver.get("https://example.com")  # Change to your target URL
driver.maximize_window()

# Step 1: Locate the element
element = driver.find_element(By.XPATH, "//h1")  # Replace with your target element

# Step 2: Highlight the element with a red square box (using JS)
driver.execute_script("""
    arguments[0].style.border = '4px solid red';
    arguments[0].style.padding = '4px';
    arguments[0].style.background = '#ffeeee';
""", element)

time.sleep(1)  # Optional: wait to visually see it before screenshot

# Step 3: Take screenshot
driver.save_screenshot("full_page_with_highlight.png")

# Or just the element
element.screenshot("highlighted_element.png")

driver.quit()
