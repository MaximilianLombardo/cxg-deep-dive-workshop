import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, output_file):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the URL
    driver.get(url)
    
    # Take a screenshot
    driver.save_screenshot(output_file)
    
    # Clean up
    driver.quit()
    
    return output_file

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Capture a screenshot of a webpage using Selenium.")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("-o", "--output", default="screenshot.png", help="Output file name (default: screenshot.png)")
    args = parser.parse_args()
    
    # Take a screenshot
    screenshot = take_screenshot(args.url, args.output)
    print(f"Screenshot saved as {screenshot}")

