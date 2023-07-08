import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def list_element_ids(url):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    # Get all elements
    elements = driver.find_elements_by_css_selector("*")

    # Extract element IDs
    element_ids = [element.get_attribute("id") for element in elements if element.get_attribute("id")]

    # Clean up
    driver.quit()

    return element_ids


def take_element_screenshot(url, element_id, output_file):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    try:
        #element = driver.find_element_by_id(element_id)
        element = driver.find_element(By.XPATH, element_id);

        # Take a screenshot of the specific element
        element.screenshot(output_file)

        print(f"Screenshot of element '{element_id}' saved as {output_file}")
    except Exception as e:
        print(f"Error: Failed to find the specified element '{element_id}'.")
        print(e)

    # Clean up
    driver.quit()


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Capture a screenshot of a specific HTML element or list all element IDs using Selenium.")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("-l", "--list", action="store_true", help="List all element IDs on the webpage")
    parser.add_argument("-e", "--element", help="ID of the HTML element")
    parser.add_argument("-o", "--output", default="screenshot.png", help="Output file name (default: screenshot.png)")
    args = parser.parse_args()

    if args.list:
        # List all element IDs on the webpage
        element_ids = list_element_ids(args.url)
        print("Element IDs on the webpage:")
        for element_id in element_ids:
            print(element_id)
    elif args.element:
        # Take a screenshot of the specific element
        take_element_screenshot(args.url, args.element, args.output)
    else:
        print("Please specify either the '-l' option to list element IDs or provide the '-e' option with an element ID to capture a screenshot.")
