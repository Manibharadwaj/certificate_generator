from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Load student names from CSV
df = pd.read_csv("students.csv")  # CSV file should have a 'names' column

# Template and font settings
template_path = "certificate_template.jpg"    # Your certificate background
# font_path = "times.ttf"                       # Make sure this font file is in the same folder
font_path = "timesbd.ttf"
font_size = 60
font_color = "black"

# Create output folder for certificates
output_folder = "certificates"
os.makedirs(output_folder, exist_ok=True)

# Generate certificates
for name in df['names']:
    # Load the certificate template
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Name text
    text = name

    # Calculate text size and position using textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (image.width - text_width) / 2
    y = 600  # Adjust this Y-coordinate based on where the name should appear

    # Draw the name on the certificate
    draw.text((x, y), text, font=font, fill=font_color)

    # Save as JPG (convert RGBA to RGB)
    output_path = os.path.join(output_folder, f"Certificate_{name.replace(' ', '_')}.jpg")
    image.convert("RGB").save(output_path)

    print(f"✅ Generated certificate for {name}")

print("\n🎉 All certificates have been saved in the 'certificates' folder.")
