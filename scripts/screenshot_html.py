import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from bs4 import BeautifulSoup


def generate_html_element_tree(url):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    # Get the page source
    page_source = driver.page_source

    # Clean up
    driver.quit()

    # Parse HTML and generate element tree
    soup = BeautifulSoup(page_source, 'html.parser')
    element_tree = generate_element_tree(soup)

    return element_tree


def generate_element_tree(element):
    tree = []
    tree.append(f"<{element.name}>")
    for child in element.children:
        if child.name:
            child_tree = generate_element_tree(child)
            tree.extend(["  " + line for line in child_tree.splitlines()])
        else:
            tree.append(f"  {child.strip()}")

    return "\n".join(tree)


def take_element_screenshot(url, output_file, element_selector):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    try:
        element = driver.find_element(By.CSS_SELECTOR, element_selector)
        location = element.location
        size = element.size

        # Take a screenshot of the specific element
        driver.save_screenshot(output_file)

        # Crop the screenshot to the element's dimensions
        screenshot = Image.open(output_file)
        cropped_screenshot = screenshot.crop((location['x'], location['y'], location['x'] + size['width'],
                                              location['y'] + size['height']))
        cropped_screenshot.save(output_file)

        print(f"Screenshot of element '{element_selector}' saved as {output_file}")
    except Exception as e:
        print(f"Error: Failed to find the specified element '{element_selector}'.")
        print(e)

    # Clean up
    driver.quit()


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate HTML element tree and capture element screenshot.")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("--output", default="screenshot.png", help="Output file name (default: screenshot.png)")
    parser.add_argument("--element", help="CSS selector of the element")
    args = parser.parse_args()

    # Generate HTML element tree
    element_tree = generate_html_element_tree(args.url)
    print("HTML Element Tree:")
    print(element_tree)

    # Capture screenshot of the specific element if provided
    if args.element:
        take_element_screenshot(args.url, args.output, args.element)
