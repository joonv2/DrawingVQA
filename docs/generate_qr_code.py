import qrcode

# The data you want to encode
data = "https://joonv2.github.io/DrawingVQA/"

# Generate the QR code
img = qrcode.make(data)

# Save it as an image file
img.save("./docs/my_qrcode.png")