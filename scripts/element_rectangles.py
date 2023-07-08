import cv2
import argparse


def find_element_rectangles(image_path, output_file):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find bounding rectangles for each contour
    rectangles = [cv2.boundingRect(cnt) for cnt in contours]

    # Save the cropping parameters for each rectangle
    with open(output_file, "w") as file:
        for rect in rectangles:
            x, y, width, height = rect
            file.write(f"{x},{y},{width},{height}\n")

    print(f"Cropping parameters for each rectangle saved in {output_file}")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Find cropping parameters for rectangular elements in an image.")
    parser.add_argument("image", help="Input image path")
    parser.add_argument("output", help="Output file to save cropping parameters")
    args = parser.parse_args()

    # Call the find_element_rectangles function with provided arguments
    find_element_rectangles(args.image, args.output)
