import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

def get_full_screenshot_dimensions(url):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the URL
    driver.get(url)
    
    # Get the dimensions of the entire webpage
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    
    # Clean up
    driver.quit()
    
    return width, height

def take_screenshot(url, output_file, width=None, height=None, crop_x=None, crop_y=None, crop_width=None, crop_height=None):
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    # Set window size
    if width and height:
        driver.set_window_size(width, height)
    else:
        # Get the full screenshot dimensions if width and height are not provided
        full_width, full_height = get_full_screenshot_dimensions(url)
        driver.set_window_size(full_width, full_height)
    
    # Navigate to the URL
    driver.get(url)
    
    # Take a screenshot
    driver.save_screenshot(output_file)
    
    # Crop the screenshot if crop coordinates and dimensions are provided
    if crop_x is not None and crop_y is not None and crop_width is not None and crop_height is not None:
        # Open the screenshot
        screenshot = Image.open(output_file)
        
        # Crop the image
        cropped_screenshot = screenshot.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))
        
        # Save the cropped image
        cropped_screenshot.save(output_file)
    
    # Clean up
    driver.quit()
    
    return output_file

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Capture a screenshot of a webpage using Selenium.")
    parser.add_argument("url", help="URL of the webpage")
    parser.add_argument("-o", "--output", default="screenshot.png", help="Output file name (default: screenshot.png)")
    parser.add_argument("--width", type=int, help="Width of the browser window")
    parser.add_argument("--height", type=int, help="Height of the browser window")
    parser.add_argument("--crop-x", type=int, help="X-coordinate of the crop area")
    parser.add_argument("--crop-y", type=int, help="Y-coordinate of the crop area")
    parser.add_argument("--crop-width", type=int, help="Width of the crop area")
    parser.add_argument("--crop-height", type=int, help="Height of the crop area")
    args = parser.parse_args()
    
    # Take a screenshot
    screenshot = take_screenshot(args.url, args.output, args.width, args.height, args.crop_x, args.crop_y, args.crop_width, args.crop_height)
    print(f"Screenshot saved as {screenshot}")

