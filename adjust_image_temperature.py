import argparse
from PIL import Image

def adjust_temperature(image, adjustment):
    """
    Adjust the temperature of the image.
    :param image: PIL Image object
    :param adjustment: Temperature adjustment value (positive for warmer, negative for cooler)
    :return: Adjusted PIL Image object
    """
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Apply temperature adjustment
    # Enhance red for warmth and blue for coolness
    r, g, b = image.split()
    if adjustment > 0:
        # Enhance red for warmth
        r = r.point(lambda i: i + adjustment if i + adjustment <= 255 else 255)
    else:
        # Enhance blue for coolness
        b = b.point(lambda i: i - adjustment if i - adjustment >= 0 else 0)

    return Image.merge('RGB', (r, g, b))

def main():
    parser = argparse.ArgumentParser(description='Adjust image temperature.')
    parser.add_argument('input_path', type=str, help='Input JPEG image file path')
    parser.add_argument('output_path', type=str, help='Output JPEG image file path')
    parser.add_argument('temperature', type=int, help='Temperature adjustment value')
    
    args = parser.parse_args()

    try:
        # Open the image
        image = Image.open(args.input_path)
        
        # Check if the image is a JPEG
        if image.format != 'JPEG':
            raise ValueError("Input file is not a JPEG image.")

        # Adjust the temperature
        adjusted_image = adjust_temperature(image, args.temperature)

        # Save the image
        adjusted_image.save(args.output_path, 'JPEG')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()