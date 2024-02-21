# Image Temperature Adjuster

## Overview

This tool is designed to adjust the temperature of JPEG images. By modifying the color balance, it can make images appear warmer or cooler.

## Technical Stack

- Python: The primary programming language used.
- Pillow (PIL fork): A Python Imaging Library used for opening, manipulating, and saving many different image file formats.
- argparse: A Python module for parsing command-line arguments.

## Goal

The primary goal of this tool is to provide an easy-to-use command-line interface for adjusting the color temperature of JPEG images. The approach involves manipulating the red and blue channels of the image to simulate a warmer or cooler temperature.

## Approach

The core functionality is encapsulated in the adjust_temperature function, which alters the image's temperature by adjusting its color channels:

### Function adjust_temperature

- Input: A PIL Image object and a temperature adjustment value.
- Process:
  1. RGB Conversion: Converts the image to RGB mode if not already in this mode.
  2. Channel Splitting: Splits the image into its red, green, and blue components.
  3. Temperature Adjustment:
  4. Warm Adjustment: Increases the intensity of the red channel for a warmer image.
  5. Cool Adjustment: Increases the intensity of the blue channel for a cooler image.
  6. Channel Merging: Re-merges the adjusted channels to form the final image.
- Output: Returns the temperature-adjusted image.

## Installation 🙌👨‍💻🚀

1. Clone the repository: `https://github.com/khalidalhabibie/adjust-image-temperature`
2. Install Python (If you already installed Python,skip this part) : Follow the instructions at [Python installation guide](https://wiki.python.org/moin/BeginnersGuide/Download).
3. Install Conda (If you already installed Conda,skip this part) : Follow the instructions at [Conda installation guide](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html).

4. Create a Conda Environment:

```bash
conda create --name image-temp-env python=3.x
```

5. Activate the Environment:

```bash
conda activate image-temp-env
```

6. Install Requirements:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the following command:

Command Format:

```bash
python adjust_image_temperature.py <input_path> <output_path> <temperature>
```

Example:

```bash
python adjust_image_temperature.py input.jpeg output.jpeg -100
```

- input_path: Path to the input JPEG image.
- output_path: Path for saving the output JPEG image.
- temperature: Temperature adjustment value (positive for warmer, negative for cooler).

## Limitations

- The script currently supports only JPEG images.
- Extreme temperature values might lead to unnatural colors.
