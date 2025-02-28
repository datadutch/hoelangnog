from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Load the image
image_path = 'your_image.jpg'  # Replace with your image file name
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Define fonts
font_path_regular = 'arial.ttf'  # Replace with the path to your regular font file
font_path_bold = 'arialbd.ttf'  # Replace with the path to your bold font file
font_regular = ImageFont.truetype(font_path_regular, 40)
font_bold = ImageFont.truetype(font_path_bold, 40)

# Define text and positions
first_line = "Kuurne Brussel Kuurne, 2 maart 11:00"

# Calculate the time difference
current_time = datetime.now()
event_time = datetime(current_time.year, 3, 2, 11, 0)
time_diff = event_time - current_time
hours_diff = time_diff.days * 24 + time_diff.seconds // 3600
minutes_diff = (time_diff.seconds % 3600) // 60

second_line = f"Nog {hours_diff} uren en {minutes_diff} minuten"

# Measure text size
first_line_width, first_line_height = draw.textbbox((0, 0), first_line, font=font_regular)[2:4]
second_line_width, second_line_height = draw.textbbox((0, 0), second_line, font=font_bold)[2:4]

# Render text on the image
text_color = "red"
text_offset = 50  # Adjust this value if you need the text more to the right
first_line_position = (image.width - first_line_width - text_offset, 50)
second_line_position = (image.width - second_line_width - text_offset, 110)

draw.text(first_line_position, first_line, font=font_regular, fill=text_color)
draw.text(second_line_position, second_line, font=font_bold, fill=text_color)

# Save the edited image
output_path = 'output_image.jpg'
image.save(output_path)

print(f"Image saved as {output_path}")
