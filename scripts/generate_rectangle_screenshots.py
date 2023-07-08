import argparse
import os
from PIL import Image


def crop_image(input_path, x, y, width, height, output_path):
    try:
        # Open the image
        image = Image.open(input_path)

        # Calculate crop boundaries
        left = int(x)
        top = int(y)
        right = int(x + width)
        bottom = int(y + height)

        # Perform the crop
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image
        cropped_image.save(output_path)

        print(f"Cropped image saved as {output_path}")
    except Exception as e:
        print("Error: Failed to crop the image.")
        print(e)


def generate_screenshots(image_path, coordinates_file, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the cropping coordinates from the file
    with open(coordinates_file, "r") as file:
        for i, line in enumerate(file):
            # Extract the cropping parameters
            x, y, width, height = map(int, line.strip().split(","))

            # Generate the output file path
            output_file = os.path.join(output_dir, f"rectangle_{i+1}.png")

            # Call the crop_image function to generate the screenshot
            crop_image(image_path, x, y, width, height, output_file)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate screenshots of detected rectangles using cropping coordinates.")
    parser.add_argument("image", help="Input image path")
    parser.add_argument("coordinates", help="Cropping coordinates file")
    parser.add_argument("output_dir", help="Output directory for screenshots")
    args = parser.parse_args()

    # Call the generate_screenshots function with provided arguments
    generate_screenshots(args.image, args.coordinates, args.output_dir)
