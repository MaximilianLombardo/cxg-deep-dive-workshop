import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

def take_full_page_screenshot(url, output_file):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the URL
    driver.get(url)
    
    # Set the dimensions of the browser window to match the height of the webpage
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.set_window_size(width, height)
    
    # Capture the full-length screenshot
    driver.save_screenshot(output_file)
    
    # Clean up
    driver.quit()

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Capture a full-length screenshot of a webpage using Selenium.")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("-o", "--output", default="screenshot.png", help="Output file name (default: screenshot.png)")
    args = parser.parse_args()
    
    # Take a full-length screenshot
    take_full_page_screenshot(args.url, args.output)
    print(f"Full-length screenshot saved as {args.output}")

