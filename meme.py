import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Meme Generator", page_icon=":laughing:")
# Function to generate a meme
def generate_meme(image, top_text, bottom_text):
    # Load the image
    img = Image.open(image)

    # Add text to the image
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load a font for the text
    font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(top_text, font)
    x = (width - text_width) / 2
    y = 10

    # Add top text
    draw.text((x, y), top_text, fill="white", font=font)

    text_width, text_height = draw.textsize(bottom_text, font)
    x = (width - text_width) / 2
    y = height - text_height - 10

    # Add bottom text
    draw.text((x, y), bottom_text, fill="white", font=font)

    return img

# Streamlit UI
st.title("Meme Generator")
st.sidebar.title("Generate Your Meme")

# Upload an image
uploaded_image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

# Input for top and bottom text
top_text = st.sidebar.text_input("Top Text", "")
bottom_text = st.sidebar.text_input("Bottom Text", "")

# Display the meme
if uploaded_image is not None and top_text != "" and bottom_text != "":
    meme = generate_meme(uploaded_image, top_text, bottom_text)
    st.image(meme, use_container_width=True, caption="Your Meme")

# Add a footer
st.sidebar.markdown("Created by Your Name")

# Run the app
if __name__ == '__main__':
    st.write("Welcome to the Meme Generator!")
