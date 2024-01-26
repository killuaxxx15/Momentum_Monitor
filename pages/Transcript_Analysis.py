import streamlit as st

def main():
    # Title of your app
    st.header("Analysis of Hyster-Yale Materials Handling Inc.'s Earnings Call Transcript")

    # Your link (replace with your actual link)
    link = "https://filecache.investorroom.com/mr5ir_hysteryale/942/hy-us-investor-day-transcript-20231116.pdf"
    st.markdown(f"[Click here for the link to the transcript]({link})", unsafe_allow_html=True)

    st.write('Background Information')
    st.text('Industry and Key Developments: Hyster-Yale Materials Handling Inc. operates in three main business segments: Lift Truck, Bolzoni attachment, and Nuvera fuel cell businesses. The Lift Truck business is the core, while Bolzoni is closely associated with lift trucks, and Nuvera focuses on decarbonization green power solutions for forklift trucks and related industries​​.')
    

if __name__ == "__main__":
    main()
