import qrcode
import sys
import re

# Check if data is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python qrcodegenerator.py [data]")
    sys.exit(1)

# Data to be encoded (first command-line argument)
data = sys.argv[1]

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Sanitize data to create a valid filename
# Replace invalid filename characters with underscores
safe_filename = re.sub(r'[^\w_.)( -]', '_', data)[:50]  # Limiting filename length to 50 characters

# Save it to a file (filename based on sanitized data)
filename = f"qr_{safe_filename}.png"
img.save(filename)

print(f"QR Code generated successfully! File saved as: {filename}")
