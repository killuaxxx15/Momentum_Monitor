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

    if not image_files:
        st.error("No JPG images found in the current directory.")
        return

    # Create a slider to select the image
    selected_image_index = st.slider(" ", 0, len(image_files) - 1)

    # Display the selected image
    image_path = image_files[selected_image_index]
    image = Image.open(image_path)
    st.image(image, caption=f"Image {selected_image_index + 1}: {image_path}")


    gif_file = "By Sector MA Plot_(MA=50_200)_10days from_2024-08-30_.gif"

    # Open the GIF file
    image = Image.open(gif_file)
        
    # Function to load and encode the GIF file
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

        # Get the base64 encoded string of the GIF
    img_str = get_img_as_base64(gif_file)
        
        # Display the animated GIF using HTML
    st.markdown(f'<img src="data:image/gif;base64,{img_str}" alt="Animated GIF">', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
