import streamlit as st
from utils.progress_tracker import ProgressTracker
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Market Indices - Stock Market Academy",
    page_icon="📋",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Market Indices"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def create_class_performance_chart():
    """Create a chart showing class performance over years"""
    years = ['2020', '2021', '2022', '2023', '2024']
    class_averages = [75, 78, 72, 80, 82]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=class_averages,
        mode='lines+markers',
        name='Class Average',
        line=dict(color='blue', width=4),
        marker=dict(size=10, color='blue'),
        fill='tonexty'
    ))
    
    fig.update_layout(
        title="Class Average Performance Over Years (Like a Market Index)",
        xaxis_title="Year",
        yaxis_title="Average Score",
        showlegend=True,
        height=400,
        yaxis=dict(range=[65, 85])
    )
    
    return fig

def create_index_composition_chart():
    """Create a pie chart showing index composition"""
    sectors = ['Technology', 'Healthcare', 'Finance', 'Consumer', 'Energy', 'Others']
    percentages = [25, 18, 15, 12, 10, 20]
    
    fig = px.pie(
        values=percentages,
        names=sectors,
        title="Sample Market Index Composition"
    )
    
    return fig

def main():
    st.title("📋 Understanding Market Indices")
    st.markdown("### *Nifty 50, S&P 500, Sensex - Demystified!*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: Market Analogies"):
            st.switch_page("pages/6_☕_Market_Analogies.py")
    with col3:
        if st.button("Next: Search Topics →"):
            st.switch_page("pages/8_🔍_Search_Topics.py")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## 🤔 What Are Market Indices?
    
    You've probably heard of the **Nifty 50**, **S&P 500**, or **Sensex**. But what exactly are these?
    
    A **stock market index** is a group of selected stocks that represents a particular segment 
    of the market or the market as a whole. It tracks the combined performance of these stocks, 
    providing a simple way to see how that part of the market is doing overall.
    
    **Think of it as:** A report card for a group of companies! 📊
    """)
    
    # Class Average Analogy
    st.markdown("---")
    with st.expander("🎓 **The Classroom Analogy: Understanding Indices**", expanded=True):
        st.markdown("""
        ## 👨‍🎓 Stock Market Indices = Class Average
        
        Imagine a classroom where each student represents a company, and their exam marks 
        represent the stock prices of those companies.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📚 **How This Works:**
            
            **👨‍🎓 Students = Companies**
            - Each student represents a different company
            - Their exam scores = company stock prices
            - Some students are naturally better (larger companies)
            - Some struggle more (smaller companies)
            
            **📈 The Class Average = The Index**
            - Tracks overall performance of the group
            - Goes up when most students do well
            - Goes down when most students struggle
            - Quick way to judge the whole class
            """)
        
        with col2:
            st.plotly_chart(create_class_performance_chart(), use_container_width=True)
        
        st.markdown("""
        ### 📊 **What This Shows Us:**
        
        **📈 Yearly Changes:**
        - Each year, students take exams (companies report earnings)
        - Some improve, others might decline
        - The class average (index) reflects overall trend
        
        **⭐ Individual Impact:**
        - If the class's star student (like Apple in S&P 500) does really well → big positive impact
        - If they fail → brings down the whole average significantly
        - Weaker students have less impact on the overall average
        
        **📅 Comparing Years:**
        - Look at class average over time to see improvement/decline
        - Same way investors use indices to judge market performance
        """)
        
        if st.button("⭐ Bookmark Classroom Analogy", key="class_analogy"):
            add_to_bookmarks("Classroom Analogy", "Market indices work like class averages tracking student performance")
    
    # Major Indices
    st.markdown("---")
    st.markdown("## 🌍 Major Market Indices Around the World")
    
    # Create tabs for different regions
    tab1, tab2, tab3 = st.tabs(["🇺🇸 United States", "🇮🇳 India", "🌍 Global"])
    
    with tab1:
        st.markdown("""
        ### 📊 **S&P 500 (Standard & Poor's 500)**
        - 🏢 **Companies**: 500 largest US companies
        - 💰 **Market Cap**: Represents ~80% of US stock market
        - 🎯 **Purpose**: Broad US market performance
        - ⚖️ **Weighting**: Market cap weighted (bigger companies have more influence)
        - 🏆 **Famous Companies**: Apple, Microsoft, Amazon, Google, Tesla
        
        ### 💻 **NASDAQ Composite**
        - 🖥️ **Focus**: Technology and growth companies
        - 🏢 **Companies**: All companies listed on NASDAQ exchange
        - 🚀 **Character**: More volatile, tech-heavy
        - 📈 **Performance**: Often outperforms during tech booms
        
        ### 🏭 **Dow Jones Industrial Average (DJIA)**
        - 👥 **Companies**: Just 30 large US companies
        - 📊 **Weighting**: Price-weighted (unusual method)
        - 🏛️ **History**: Oldest US market index (since 1896)
        - 📰 **Media**: Most quoted in news
        """)
    
    with tab2:
        st.markdown("""
        ### 🇮🇳 **Nifty 50 (NSE)**
        - 🏢 **Companies**: 50 largest Indian companies
        - 📊 **Exchange**: National Stock Exchange (NSE)
        - 🎯 **Representation**: ~65% of Indian stock market
        - 🏆 **Top Companies**: Reliance, TCS, Infosys, HDFC Bank
        
        ### 🏛️ **Sensex (BSE)**
        - 👥 **Companies**: 30 largest Indian companies
        - 📊 **Exchange**: Bombay Stock Exchange (BSE)
        - 📅 **History**: India's oldest index (since 1986)
        - 🔢 **Base Value**: Started at 100 points
        
        ### 📈 **Other Indian Indices**
        - **Nifty 100**: Top 100 companies
        - **Nifty Bank**: Banking sector focus
        - **Nifty IT**: Information technology companies
        """)
    
    with tab3:
        st.markdown("""
        ### 🌏 **Major Global Indices**
        
        **🇬🇧 FTSE 100 (UK)**
        - 100 largest UK companies
        - London Stock Exchange
        
        **🇯🇵 Nikkei 225 (Japan)**
        - 225 Japanese companies
        - Tokyo Stock Exchange
        
        **🇩🇪 DAX (Germany)**
        - 40 largest German companies
        - Frankfurt Stock Exchange
        
        **🇨🇳 Shanghai Composite (China)**
        - All companies on Shanghai Exchange
        - Tracks Chinese market performance
        """)
    
    # Index Composition
    st.markdown("---")
    st.markdown("## 🥧 What's Inside an Index?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_index_composition_chart(), use_container_width=True)
    
    with col2:
        st.markdown("""
        ### 🏭 **Sector Diversification**
        
        **🎯 Why Mix Sectors?**
        - Different industries perform well at different times
        - Technology might boom while energy struggles
        - Diversification reduces overall risk
        
        **📊 Common Sectors:**
        - 💻 **Technology**: Apple, Microsoft, Google
        - 🏥 **Healthcare**: Johnson & Johnson, Pfizer
        - 🏦 **Finance**: JPMorgan, Bank of America
        - 🛒 **Consumer**: Amazon, Walmart, Coca-Cola
        - ⚡ **Energy**: ExxonMobil, Chevron
        """)
    
    # How to Invest in Indices
    st.markdown("---")
    with st.expander("💰 **Can I Buy an Index? Enter ETFs!**", expanded=True):
        st.markdown("""
        ## 🎯 Yes! Through ETFs (Exchange-Traded Funds)
        
        **🤔 The Challenge:**
        - You can't directly buy "the S&P 500"
        - Buying all 500 stocks individually would be expensive and complicated
        
        **✅ The Solution: ETFs**
        - **ETF** = Exchange-Traded Fund
        - Designed to track the performance of a specific index
        - You buy shares of the ETF, which owns all the index stocks
        
        ### 🛍️ **Popular Index ETFs:**
        
        **🇺🇸 US Market ETFs:**
        - **SPY**: Tracks S&P 500
        - **QQQ**: Tracks NASDAQ-100
        - **VTI**: Tracks entire US stock market
        
        **🇮🇳 Indian Market ETFs:**
        - **Nifty BeES**: Tracks Nifty 50
        - **SensexETF**: Tracks Sensex
        - **Bank BeES**: Tracks banking sector
        
        ### ✅ **Benefits of Index ETFs:**
        
        **🎯 Instant Diversification:**
        - One purchase = exposure to 50-500 companies
        - Reduces risk compared to individual stocks
        
        **💰 Low Costs:**
        - Management fees typically 0.1-0.5% per year
        - Much cheaper than actively managed funds
        
        **📈 Market Performance:**
        - You get the market's average return
        - No need to pick individual winning stocks
        
        **🔄 Easy Trading:**
        - Buy and sell like individual stocks
        - Available during market hours
        """)
        
        if st.button("⭐ Bookmark ETF Information", key="etf_info"):
            add_to_bookmarks("Index ETFs", "How to invest in market indices through Exchange-Traded Funds")
    
    # Index Performance Factors
    st.markdown("---")
    st.markdown("## 📈 What Makes Indices Move?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ### ⬆️ **What Pushes Indices UP:**
        
        - 💰 **Strong Earnings**: Companies beat profit expectations
        - 🌍 **Economic Growth**: GDP expansion, low unemployment
        - 🏦 **Monetary Policy**: Lower interest rates
        - 😊 **Positive Sentiment**: Investor optimism
        - 🏭 **Sector Rotation**: Money flows into index sectors
        - 📰 **Good News**: Positive economic or political developments
        """)
    
    with col2:
        st.error("""
        ### ⬇️ **What Pushes Indices DOWN:**
        
        - 📉 **Poor Earnings**: Companies miss expectations
        - 🌧️ **Economic Weakness**: Recession fears, high unemployment
        - 📈 **Rising Rates**: Higher interest rates
        - 😰 **Fear/Uncertainty**: Geopolitical tensions
        - 🏃 **Money Outflows**: Investors sell to move to bonds/cash
        - ⚠️ **Crisis Events**: Pandemics, wars, financial crises
        """)
    
    # Interactive Quiz
    st.markdown("---")
    st.markdown("## 🧠 Index Knowledge Challenge")
    
    with st.form("index_quiz"):
        q1 = st.radio(
            "What does a stock market index represent?",
            ["A single company's performance", "A group of selected stocks representing market segments", "Government economic policy", "Currency exchange rates"],
            key="index_q1"
        )
        
        q2 = st.radio(
            "In the classroom analogy, what does the class average represent?",
            ["Individual student performance", "The market index", "The teacher's evaluation", "School administration"],
            key="index_q2"
        )
        
        q3 = st.multiselect(
            "Which of these are actual market indices?",
            ["S&P 500", "Nifty 50", "NASDAQ", "Sensex", "Apple Index", "Facebook 100"],
            key="index_q3"
        )
        
        q4 = st.radio(
            "How can regular investors buy an entire index?",
            ["Buy each stock individually", "Through ETFs (Exchange-Traded Funds)", "Contact the stock exchange directly", "It's not possible"],
            key="index_q4"
        )
        
        submitted = st.form_submit_button("Test My Index Knowledge")
        
        if submitted:
            score = 0
            
            if q1 == "A group of selected stocks representing market segments":
                st.success("✅ Correct! Indices represent groups of stocks from market segments.")
                score += 1
            else:
                st.error("❌ Market indices represent groups of selected stocks, not individual companies.")
            
            if q2 == "The market index":
                st.success("✅ Right! The class average represents the market index.")
                score += 1
            else:
                st.error("❌ In the analogy, the class average represents the market index.")
            
            correct_indices = {"S&P 500", "Nifty 50", "NASDAQ", "Sensex"}
            selected_indices = set(q3)
            
            if correct_indices.issubset(selected_indices) and not {"Apple Index", "Facebook 100"}.intersection(selected_indices):
                st.success("✅ Perfect! You identified all real market indices.")
                score += 1
            else:
                st.error("❌ S&P 500, Nifty 50, NASDAQ, and Sensex are real indices. Apple Index and Facebook 100 don't exist!")
            
            if q4 == "Through ETFs (Exchange-Traded Funds)":
                st.success("✅ Excellent! ETFs allow you to buy entire indices easily.")
                score += 1
            else:
                st.error("❌ ETFs (Exchange-Traded Funds) are the best way to invest in entire indices.")
            
            st.info(f"Your Score: {score}/4")
            
            if score == 4:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("7_📋_Market_Indices")
                st.success("🎉 Outstanding! You've mastered market indices!")
            elif score >= 3:
                st.info("Great job! You have a solid understanding of indices.")
            else:
                st.warning("Keep studying! Understanding indices is crucial for investing.")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Essential Index Takeaways")
    
    st.info("""
    **🧠 Master These Index Concepts:**
    
    1. 📊 **Group Performance**: Indices track groups of stocks, not individual companies
    2. 🎓 **Class Average**: Like tracking a classroom's average performance over time  
    3. 🌍 **Market Representation**: Major indices represent significant portions of their markets
    4. ⚖️ **Weighted Impact**: Larger companies have more influence on index movement
    5. 💰 **ETF Access**: You can invest in entire indices through Exchange-Traded Funds
    6. 📈 **Economic Barometer**: Indices reflect overall economic and market health
    """)
    
    if st.button("⭐ Bookmark Essential Takeaways", key="essential_takeaways"):
        add_to_bookmarks("Market Indices - Essential Takeaways", "Key concepts about how market indices work and why they matter")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/6_☕_Market_Analogies.py")
    
    with col3:
        if st.button("Next: Search Topics →", use_container_width=True):
            st.switch_page("pages/8_🔍_Search_Topics.py")

if __name__ == "__main__":
    main()
