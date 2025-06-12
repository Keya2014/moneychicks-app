import streamlit as st
from utils.progress_tracker import ProgressTracker

st.set_page_config(
    page_title="Stock Exchanges - Stock Market Academy",
    page_icon="📊",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Stock Exchanges"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def main():
    st.title("📊 How Do Stock Exchanges Work?")
    st.markdown("### *The Organized Marketplaces Where Stocks Trade*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: Where to Buy"):
            st.switch_page("pages/3_🛒_Where_to_Buy_Stocks.py")
    with col3:
        if st.button("Next: Stock Pricing →"):
            st.switch_page("pages/5_💰_Stock_Pricing.py")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## 🏢 What Are Stock Exchanges?
    
    Stock exchanges are **organized marketplaces** where buying and selling of stocks happens. 
    Think of them as giant, sophisticated shopping centers for investments!
    
    **Famous Examples:**
    - 🇺🇸 **NYSE** (New York Stock Exchange) - USA
    - 🇺🇸 **NASDAQ** - USA (tech-heavy)
    - 🇮🇳 **NSE** (National Stock Exchange) - India
    - 🇮🇳 **BSE** (Bombay Stock Exchange) - India
    """)
    
    # Mall Analogy
    st.markdown("---")
    with st.expander("🛍️ **The Mall Analogy: Understanding Stock Exchanges**", expanded=True):
        st.markdown("""
        ### 🏬 Stock Market = Shopping Mall
        
        **The Mall Structure:**
        - 🏢 **The Mall Building**: The stock exchange (NYSE, NASDAQ, etc.)
        - 🏪 **Individual Shops**: Different companies listed on the exchange
        - 👥 **Shoppers**: Investors looking to buy shares
        - 🛒 **Shopping**: Buying and selling stocks
        - 🏢 **Mall Management**: Exchange operators ensuring fair trading
        
        **How It Works:**
        
        **🏪 The Shops (Companies):**
        - Each company is like a shop in the mall
        - When a shop wants to expand, it can "sell shares" (pieces of ownership)
        - Popular shops attract more shoppers (investors)
        
        **👥 The Shoppers (Investors):**
        - Walk around looking for good shops (companies) to invest in
        - Buy pieces of shops they believe will become successful
        - Can sell their pieces to other shoppers later
        
        **🏢 Mall Management (Exchange):**
        - Ensures all transactions are fair and transparent
        - Keeps detailed records of all trades
        - Makes sure everyone follows the rules
        - Provides security and infrastructure
        """)
        
        if st.button("⭐ Bookmark Mall Analogy", key="mall_analogy"):
            add_to_bookmarks("Mall Analogy", "Stock exchanges work like shopping malls with shops (companies) and shoppers (investors)")
    
    # How Companies Join
    st.markdown("---")
    st.markdown("## 🎪 How Companies Join Stock Exchanges")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📋 **The Listing Process**
        
        **Step 1: Meet Requirements**
        - Minimum company size and revenue
        - Financial transparency standards
        - Corporate governance rules
        
        **Step 2: Initial Public Offering (IPO)**
        - Company offers shares to the public
        - Investment banks help with the process
        - Regulatory approval required
        """)
    
    with col2:
        st.markdown("""
        **Step 3: Official Listing**
        - Company gets a stock ticker symbol (like AAPL for Apple)
        - Shares begin trading on the exchange
        - Company must continue meeting requirements
        
        **Step 4: Ongoing Obligations**
        - Regular financial reporting
        - Compliance with exchange rules
        - Maintaining listing standards
        """)
    
    # Major Stock Exchanges
    st.markdown("---")
    st.markdown("## 🌍 Major Stock Exchanges Around the World")
    
    # Create tabs for different regions
    tab1, tab2, tab3 = st.tabs(["🇺🇸 United States", "🇮🇳 India", "🌍 Global"])
    
    with tab1:
        st.markdown("""
        ### 📍 **New York Stock Exchange (NYSE)**
        - 🏛️ **Founded**: 1792 (oldest in the US)
        - 💰 **Market Cap**: Largest stock exchange globally
        - 🏢 **Famous Companies**: Apple, Microsoft, Amazon, Google
        - 📍 **Location**: Wall Street, New York City
        
        ### 💻 **NASDAQ**
        - 🖥️ **Founded**: 1971 (first electronic exchange)
        - 🚀 **Focus**: Technology and growth companies
        - 🏢 **Famous Companies**: Tesla, Netflix, Facebook, Intel
        - ⚡ **Special**: Fully electronic trading system
        """)
    
    with tab2:
        st.markdown("""
        ### 🇮🇳 **National Stock Exchange (NSE)**
        - 📅 **Founded**: 1992
        - 📊 **Index**: Nifty 50
        - 💻 **Technology**: Modern electronic trading
        - 🏢 **Companies**: Reliance, TCS, Infosys, HDFC
        
        ### 🏛️ **Bombay Stock Exchange (BSE)**
        - 📅 **Founded**: 1875 (oldest in Asia)
        - 📊 **Index**: Sensex
        - 🏢 **Heritage**: Historic trading floor
        - 📍 **Location**: Mumbai, India
        """)
    
    with tab3:
        st.markdown("""
        ### 🌏 **Other Major Exchanges**
        
        **🇬🇧 London Stock Exchange (LSE)**
        - Historic European financial center
        - FTSE 100 index
        
        **🇯🇵 Tokyo Stock Exchange (TSE)**
        - Largest in Asia by market cap
        - Nikkei 225 index
        
        **🇨🇳 Shanghai Stock Exchange**
        - Major Chinese market
        - SSE Composite index
        """)
    
    # How Trading Works
    st.markdown("---")
    with st.expander("⚙️ **How Trading Actually Happens**", expanded=True):
        st.markdown("""
        ### 🔄 **The Trading Process:**
        
        **1. 📱 You Place an Order**
        - Use your broker's app or website
        - Specify: stock symbol, quantity, price type
        
        **2. 🏢 Broker Sends to Exchange**
        - Your broker forwards your order to the exchange
        - Order enters the exchange's electronic system
        
        **3. 🤝 Matching System**
        - Exchange computer matches buy and sell orders
        - Best prices get priority
        - Trade executes when buyer and seller agree
        
        **4. ✅ Confirmation**
        - Trade confirmation sent to both parties
        - Shares and money are transferred
        - Settlement usually takes 1-2 business days
        
        ### ⏰ **Trading Hours:**
        - **NYSE/NASDAQ**: 9:30 AM - 4:00 PM ET (Monday-Friday)
        - **NSE/BSE**: 9:15 AM - 3:30 PM IST (Monday-Friday)
        - **Pre-market and after-hours** trading also available
        """)
        
        if st.button("⭐ Bookmark Trading Process", key="trading_process"):
            add_to_bookmarks("Trading Process", "How stock trades are executed on exchanges")
    
    # Exchange Functions
    st.markdown("---")
    st.markdown("## 🛡️ What Stock Exchanges Do for You")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ### ✅ **Safety & Security**
        
        - 🔒 **Regulation**: Strict rules and oversight
        - 📋 **Transparency**: All trades are recorded
        - 💰 **Settlement**: Guaranteed trade completion
        - 🛡️ **Investor Protection**: Safeguards against fraud
        """)
    
    with col2:
        st.info("""
        ### 🚀 **Efficiency & Access**
        
        - ⚡ **Speed**: Near-instantaneous trade execution
        - 💧 **Liquidity**: Easy to buy and sell
        - 📊 **Price Discovery**: Fair market pricing
        - 🌐 **Access**: Global reach for investors
        """)
    
    # Interactive Quiz
    st.markdown("---")
    st.markdown("## 🧠 Exchange Knowledge Check")
    
    with st.form("exchange_quiz"):
        q1 = st.radio(
            "In the mall analogy, what do the individual shops represent?",
            ["Stock exchanges", "Companies listed on the exchange", "Investors", "Brokers"],
            key="exchange_q1"
        )
        
        q2 = st.radio(
            "What is the primary role of stock exchange management?",
            ["To set stock prices", "To ensure fair trading and maintain records", "To give investment advice", "To guarantee profits"],
            key="exchange_q2"
        )
        
        q3 = st.multiselect(
            "Which of these are major stock exchanges?",
            ["NYSE", "NASDAQ", "BSE", "NSE", "McDonald's", "Apple Store"],
            key="exchange_q3"
        )
        
        submitted = st.form_submit_button("Check My Knowledge")
        
        if submitted:
            score = 0
            
            if q1 == "Companies listed on the exchange":
                st.success("✅ Correct! Individual shops represent companies.")
                score += 1
            else:
                st.error("❌ In the mall analogy, shops represent companies listed on the exchange.")
            
            if q2 == "To ensure fair trading and maintain records":
                st.success("✅ Correct! Exchanges ensure fair, transparent trading.")
                score += 1
            else:
                st.error("❌ Exchange management ensures fair trading and keeps records.")
            
            correct_exchanges = {"NYSE", "NASDAQ", "BSE", "NSE"}
            selected_exchanges = set(q3)
            
            if correct_exchanges.issubset(selected_exchanges) and not {"McDonald's", "Apple Store"}.intersection(selected_exchanges):
                st.success("✅ Perfect! You identified all the stock exchanges correctly.")
                score += 1
            else:
                st.error("❌ NYSE, NASDAQ, BSE, and NSE are stock exchanges. McDonald's and Apple Store are not!")
            
            st.info(f"Your Score: {score}/3")
            
            if score == 3:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("4_📊_Stock_Exchanges")
                st.success("🎉 Excellent! You understand how stock exchanges work!")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways")
    
    st.info("""
    **Remember These Essentials:**
    
    1. 🏬 **Organized Marketplaces**: Stock exchanges are like sophisticated malls for trading
    2. 🛡️ **Safety First**: Exchanges ensure fair, transparent, and secure trading
    3. 🌍 **Global Network**: Major exchanges connect investors worldwide
    4. ⚡ **Efficiency**: Electronic systems enable fast, accurate trade execution
    5. 📋 **Listing Requirements**: Companies must meet standards to trade on exchanges
    """)
    
    if st.button("⭐ Bookmark Key Takeaways", key="takeaways"):
        add_to_bookmarks("Stock Exchanges - Key Takeaways", "How exchanges work as organized marketplaces")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/3_🛒_Where_to_Buy_Stocks.py")
    
    with col3:
        if st.button("Next: Stock Pricing →", use_container_width=True):
            st.switch_page("pages/5_💰_Stock_Pricing.py")

if __name__ == "__main__":
    main()
