import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.exceptions import DataOverflowError


def main():
    data = input("What would you like to add to your Qrcode? ")
    code(data)


def code(s):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    try:
        qr.add_data(s)
        qr.make(fit=True)

        while True:
            quest = input("Do you want to add image? Y/Yes or N/No: ").capitalize()
            if quest in ["Y", "Yes"]:
                path = input("Image path: ")
                img = qr.make_image(
                    image_factory=StyledPilImage, embeded_image_path=path
                )

                return save_code(img)

            elif quest in ["N", "No"]:
                break

        col = custom_color(qr)
        save_code(col)
    except DataOverflowError as e:
        raise e
    except Exception as e:
        raise e


def custom_color(s):

    col1 = input("Enter the fill_color name or hex value of color(# RRGGBB): ")
    col2 = input("Enter the back_color name or hex value of color(# RRGGBB): ")
    img = s.make_image(fill_color=col1, back_color=col2)
    return img


def save_code(img):
    img.save("qrcode.png")


if __name__ == "__main__":
    main()