# Simple QR Code Generator
# Install: pip install qrcode[pil]

import qrcode

# Create QR code
data = "https://github.com/DeveloperSayantika?tab=repositories"  # Change this to your data
qr = qrcode.make(data)

# Save image
qr.save("my_qr_code.png")
print("QR code saved as my_qr_code.png")
