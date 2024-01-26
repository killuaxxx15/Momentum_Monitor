import streamlit as st

def main():
    # Title of your app
    st.title("Analysis of Hyster-Yale Materials Handling Inc.'s Earnings Call Transcript")

    # Your link (replace with your actual link)
    link = "https://filecache.investorroom.com/mr5ir_hysteryale/942/hy-us-investor-day-transcript-20231116.pdf"
    st.markdown(f"[Click here for the link to the transcript]({link})", unsafe_allow_html=True)

    # Your long text
    long_text = """
    Background Information
    Industry and Key Developments: Hyster-Yale Materials Handling Inc. operates in three main business segments: Lift Truck, Bolzoni attachment, and Nuvera fuel cell businesses. The Lift Truck business is the core, while Bolzoni is closely associated with lift trucks, and Nuvera focuses on decarbonization green power solutions for forklift trucks and related industries​​.
    Growth Analysis
    Revenue Trends: In the last 12 months, Hyster-Yale reported revenues just over $4 billion, indicating significant business scale and market presence.
    Profit Margins and Financial Performance Indicators: The company achieved an operating profit of $180 million and a net income of just over $100 million. This performance marks a recovery from previous years impacted by high inflation and backlog issues​​.
    Comparison and Industry Benchmarks: While specific industry benchmarks aren't mentioned, the recovery from backlog and inflation issues suggests a positive trend compared to previous challenging periods.
    Margin Discussions: The company is targeting more than 20% return on total capital employed and a 7% operating profit, indicating a focus on efficient capital deployment and profitability​​.
    Guidance Evaluation
    Future Performance Projections: Management's strategy involves continued focus on efficient capital deployment, development of modular scalable platforms, optimization of manufacturing footprint, and leveraging partnerships and joint ventures. The emphasis on modular scalability suggests agility and adaptability in product offerings​​.
    Business Prospects
    Strategic Initiatives and Market Expansion Plans: Hyster-Yale's vision includes transforming the material movement from port to home, aiming to reduce the impact on people, the environment, and the economy. The company is looking to address customer needs with optimal solutions and reliable service throughout the product ownership cycle​​.
    Impact of Research and Development: The focus on modular scalable platforms and automation indicates a strong commitment to R&D, aimed at enhancing productivity and addressing labor shortages​​.
    Competition Analysis
    Competitive Positioning: The company's unique approach, which includes a focus on modular scalable platforms, positions it well against low-cost competitors, particularly from China​​.
    Capital Deployment
    Financial Resource Management: Hyster-Yale is focusing on optimizing its manufacturing footprint, investing in sales, and consolidating operations in key regions like the JAPIC region. The company has taken steps to make its operation more robust against market dynamics and improve pricing strategies​​.
    Sentiment Assessment
    Management and Analysts Tone: The tone is optimistic and focused on growth, with an emphasis on innovation and strategic market positioning. Management displays confidence in their business model and future prospects​​.
    Conclusion
    Hyster-Yale Materials Handling Inc. demonstrates a strong and recovering financial performance with strategic initiatives geared towards innovation, market expansion, and competitive positioning. The focus on modular scalable platforms, efficient capital deployment, and market-responsive pricing strategies positions the company favorably for future growth and resilience against market fluctuations. Management's tone and strategic direction reflect confidence in the company's ability to navigate challenges and capitalize on emerging market opportunities.

    """  # Replace with your 1000-word text

    # Displaying the text
    st.write(long_text)

if __name__ == "__main__":
    main()
