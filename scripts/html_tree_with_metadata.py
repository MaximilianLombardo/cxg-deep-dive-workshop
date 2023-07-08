import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def generate_html_tree(url):
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


def generate_element_tree(element, level=0):
    tree = ""
    indent = "  " * level
    tree += f"{indent}<{element.name}"

    # Get element attributes
    attrs = element.attrs
    if attrs:
        attr_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])
        tree += f" {attr_str}"

    # Get CSS tags
    css_tags = []
    if element.get("class"):
        css_tags.extend(element["class"])
    if element.get("id"):
        css_tags.append(f"#{element['id']}")
    if css_tags:
        tree += f"  [CSS: {', '.join(css_tags)}]"

    # Get pixel width and height
    style = element.get("style")
    if style:
        style_attrs = style.split(";")
        for attr in style_attrs:
            attr = attr.strip()
            if attr.startswith("width:"):
                width = attr.replace("width:", "").strip()
                tree += f"  [Width: {width}]"
            elif attr.startswith("height:"):
                height = attr.replace("height:", "").strip()
                tree += f"  [Height: {height}]"

    tree += ">"

    if element.name not in ["br", "hr"]:
        for child in element.children:
            if child.name:
                tree += "\n" + generate_element_tree(child, level + 1)
            else:
                if child.strip():
                    tree += f"\n{indent}  {child.strip()}"

    tree += f"\n{indent}</{element.name}>"

    return tree


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate HTML element tree with metadata using Selenium.")
    parser.add_argument("url", help="URL of the webpage")
    args = parser.parse_args()

    # Generate HTML element tree with metadata
    element_tree = generate_html_tree(args.url)
    print("HTML Element Tree:")
    print(element_tree)
