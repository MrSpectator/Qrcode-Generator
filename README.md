# QR Code Generator

## Video Demo:  <(https://youtu.be/ZRsmkjktYNE)>
## Description:

This project provides a simple script for generating QR codes with customizable colors and optional embedded images. The QR codes can be saved as PNG files.

## Features

- Generate QR codes with custom data.
- Customize the fill and background colors of the QR code.
- Optionally embed an image in the QR code.
- Save the generated QR code as a PNG file.

## Requirements

- Python 3.0
- qrcode library
- Pillow library
- pytest (for testing)

## Installation

1. Clone the repository or download the script files.

2. Install the required libraries:

```bash
> pip install qrcode[pil]
> pip install pillow
> pip install pytest
```

## Usage

1. Run the scripts
```
> python project.py
```

*2. Follow the prompts to enter the data, fill color, background color, and optional image path.
```
What would you like to add to your Qrcode? Hello, QR Code!
Enter the fill_color name or hex value of color (#RRGGBB): #FF0000
Enter the back_color name or hex value of color (#RRGGBB): #00FF00
Do you want to add image? Y/Yes or N/No: ["Y", "Yes", "N", "No"]
Image path (doesn't prompt if not using an image): path/to/your/image.png
```

## Functions

1. code(data, fill_color="#000000", back_color="#FFFFFF", image_path=None): Generates a QR code with the given data and optional custom colors and embedded image.
2. save_code(img, file_path="qrcode.png"): Saves the generated QR code image to the specified file path.

## Running tests

1. Ensure pytest is installed.

```
> pip install pytest
```

2. Run the tests.

```
> pytest "project.py"
```

## Example Test File

Here is an example of the test file (test_project.py) to test the functionality of the QR code generator:

```
import pytest
import qrcode

from project import code, custom_color, save_code

def test_code():
    data = "Hello, QR Code!"
    with pytest.raises(Exception):
        code("1 inincinco" * 10000000000000000000000)

def test_custom_color(monkeypatch):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data("Test")
    qr.make(fit=True)

    # Mock inputs
    monkeypatch.setattr('builtins.input', lambda _: '#FF0000')

    img = custom_color(qr)
    assert img is not None

def test_save_code():
    img = qrcode.make("Test")
    try:
        save_code(img)
    except Exception:
        pytest.fail("showcode raised an exception unexpectedly!")




```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Contact
For any questions or issues, please contact [sobandeoluwatonie@gmail.com].

```
This README provides a comprehensive guide on how to set up, use, and test your QR code generation project.
```
