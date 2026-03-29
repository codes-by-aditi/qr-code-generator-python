import qrcode
import random

# Generate random color
def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

# Take input
data = input("Enter the link or text: ")

# Create QR object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Generate random colors
fill = random_color()
bg = random_color()

# Create image
img = qr.make_image(fill_color=fill, back_color=bg)

# Save image
img.save("colorful_qr.png")

print(f"QR Code generated with colors: Fill={fill}, Background={bg}")