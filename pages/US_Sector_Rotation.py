import streamlit as st
from PIL import Image
import os
import base64

# Set Streamlit page configuration
st.set_page_config(page_title='US Sector Rotation', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('US Sector Rotation')

def main():
    # Get list of image files
    image_files = [f for f in os.listdir() if f.endswith('.jpg')]
    image_files.sort()  # Sort the files to ensure they're in order
    image_files = image_files[:8]  # Limit to first 8 images

    if not image_files:
        st.error("No JPG images found in the current directory.")
        return

    # Create a slider to select the image
    selected_image_index = st.slider(" ", 0, len(image_files) - 1)

    # Display the selected image
    image_path = image_files[selected_image_index]
    image = Image.open(image_path)
    st.image(image, caption=f"Image {selected_image_index + 1}: {image_path}")


if __name__ == "__main__":
    main()
