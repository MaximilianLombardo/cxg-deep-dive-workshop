import argparse
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


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Crop an image using specified coordinates.")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("x", type=int, help="X-coordinate for cropping")
    parser.add_argument("y", type=int, help="Y-coordinate for cropping")
    parser.add_argument("width", type=int, help="Width of the crop rectangle")
    parser.add_argument("height", type=int, help="Height of the crop rectangle")
    parser.add_argument("output", help="Output image path")
    args = parser.parse_args()

    # Call the crop_image function with provided arguments
    crop_image(args.input, args.x, args.y, args.width, args.height, args.output)
