import streamlit as st

def main():
    # Title of your app
    st.header("Analysis of Hyster-Yale Materials Handling Inc.'s Earnings Call Transcript")

    # Your link (replace with your actual link)
    link = "https://filecache.investorroom.com/mr5ir_hysteryale/942/hy-us-investor-day-transcript-20231116.pdf"
    st.markdown(f"[Click here for the link to the transcript]({link})", unsafe_allow_html=True)

    st.write('**Background Information**')
    st.write('The company in question, as outlined in the transcript of their investor day, operates in three key business areas: Lift Truck business (core), Bolzoni attachment business, and Nuvera fuel cell business. The Lift Truck business is their primary focus, with the other two closely related and supporting the main line of products and services. They operate globally, with a significant presence in the Americas and EMEA (Europe, Middle East, and Africa) regions, and also see growth opportunities in regions such as JAPIC (Japan, Asia-Pacific, and China)​​.')

    st.write('')
    st.write('**Growth Analysis**')
    st.write('**Revenue Trends & Financial Performance:** In the last 12 months, the company\'s revenues exceeded $4 billion, with an operating profit of $180 million and a net income of just over $100 million. This marks a significant recovery from a period affected by a large backlog and high inflation​​.')
    st.write('**Profit Margins & Key Indicators:** The company targets a top-quartile return in their industry, with a goal of greater than 20% return on total capital employed and a 7% operating profit. This is a key indicator of their financial health and strategic focus​​.')

    st.write('')
    st.write('**Guidance Evaluation**')
    st.write('**Future Performance Projections:** The company is focused on high return on capital deployed, efficient capital deployment, and high returns from capital invested in product development and infrastructure. These strategies, particularly in developing modular scalable platforms and optimizing their manufacturing footprint, are central to their future projections​​.')
    st.write('**Market Trends, Risks, and Opportunities:** They are adapting to market trends such as the search for productivity, labor shortages, electrification, and the rise of low-cost competitors. These trends shape their strategic focus on technology solutions, automation, and modular scalable platforms​​.')



if __name__ == "__main__":
    main()
