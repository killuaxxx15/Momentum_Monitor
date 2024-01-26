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
    st.write('**Revenue Trends & Financial Performance:** In the last 12 months, the company\'s revenues exceeded \$4 billion, with an operating profit of \$180 million and a net income of just over $100 million. This marks a significant recovery from a period affected by a large backlog and high inflation​​.')
    st.write('**Profit Margins & Key Indicators:** The company targets a top-quartile return in their industry, with a goal of greater than 20% return on total capital employed and a 7% operating profit. This is a key indicator of their financial health and strategic focus​​.')

    st.write('')
    st.write('**Guidance Evaluation**')
    st.write('**Future Performance Projections:** The company is focused on high return on capital deployed, efficient capital deployment, and high returns from capital invested in product development and infrastructure. These strategies, particularly in developing modular scalable platforms and optimizing their manufacturing footprint, are central to their future projections​​.')
    st.write('**Market Trends, Risks, and Opportunities:** They are adapting to market trends such as the search for productivity, labor shortages, electrification, and the rise of low-cost competitors. These trends shape their strategic focus on technology solutions, automation, and modular scalable platforms​​.')

    st.write('')
    st.write('**Business Prospects**')
    st.write('**Strategic Initiatives & Market Expansion Plans:** The company is innovating in areas like modular scalable platforms and partnering with suppliers and dealers to optimize manufacturing and distribution. Their focus on technology, particularly in areas like telemetry systems and operator assist systems, indicates a strong push towards modernization and efficiency​​.')
    st.write('**Impact of R&D and Partnerships:** R&D is heavily directed towards technology solutions like fuel cells, automation, and smart batteries, as well as the expansion of their product range to include electrified solutions​​.')

    st.write('')
    st.write('**Competition Analysiss**')
    st.write('**Comparison with Main Competitors:** The company\'s focus on modular scalable platforms provides a competitive edge. This system, which is unique and not easily replicable by competitors, allows for the efficient configuration of trucks to customer needs. They also focus on differentiating themselves through technology and customer service​​.')

    st.write('')
    st.write('**Capital Deployment**')
    st.write('**Use of Financial Resources:** Investments are strategically made in product development, technology, optimizing manufacturing footprint, and expanding their sales capabilities. The modular scalable platform is a significant area of investment, indicating the company’s focus on long-term sustainable growth and competitiveness​​.')

    st.write('')
    st.write('**Sentiment Assessment**')
    st.write('**Tone & Language of Management and Analysts:** The language and tone used by management reflect a strong focus on innovation, customer-centric solutions, and strategic growth. The emphasis is on leveraging technology, enhancing customer service, and expanding market presence​​.')
    st.write('**Overall Sentiment:** The sentiment is generally positive and forward-looking, with a clear emphasis on adapting to market changes, technological advancements, and improving customer service and product offerings​​.')

    st.write('')
    st.write('Overall, the company appears to be in a strong position with a clear focus on growth through technology, efficiency, and customer-centric strategies. Their recovery from past challenges and targeted strategies for future development indicate a solid path forward in a competitive market.')


if __name__ == "__main__":
    main()
