from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up headless browser options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Automatically download and manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://github.com/aayushker"
driver.get(url)

# Extract full page HTML after JavaScript loads
html = driver.page_source
print(html)

driver.quit()
