import cv2
import argparse


def detect_sections(image_path, output_file):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a list to store the cropping coordinates
    coordinates = []

    # Find bounding rectangles for each contour
    for cnt in contours:
        # Calculate the contour area
        area = cv2.contourArea(cnt)

        # Check if the contour area meets the criteria
        if area > 1000:
            # Get the bounding rectangle
            x, y, width, height = cv2.boundingRect(cnt)

            # Add the cropping coordinates to the list
            coordinates.append((x, y, width, height))

    # Save the cropping coordinates to the output file
    with open(output_file, "w") as file:
        for coord in coordinates:
            x, y, width, height = coord
            file.write(f"{x},{y},{width},{height}\n")

    print(f"Cropping coordinates saved in {output_file}")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Detect sections in an image and save the cropping coordinates.")
    parser.add_argument("image", help="Input image path")
    parser.add_argument("output", help="Output file to save cropping coordinates")
    args = parser.parse_args()

    # Call the detect_sections function with provided arguments
    detect_sections(args.image, args.output)

