import streamlit as st
from utils.progress_tracker import ProgressTracker

st.set_page_config(
    page_title="Where to Buy Stocks - Stock Market Academy",
    page_icon="🛒",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Where to Buy Stocks"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def main():
    st.title("🛒 Where Can I Buy These Stocks?")
    st.markdown("### *Understanding Primary vs Secondary Markets*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: Why Go Public?"):
            st.switch_page("pages/2_🏢_Why_Companies_Go_Public.py")
    with col3:
        if st.button("Next: Stock Exchanges →"):
            st.switch_page("pages/4_📊_Stock_Exchanges.py")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## 🤔 The Simple Answer
    
    You can buy stocks through **two main markets**: the Primary Market and the Secondary Market.
    Think of it like buying a car - you can either buy it brand new from the dealership (primary) 
    or from someone who already owns it (secondary).
    """)
    
    # Primary Market Section
    st.markdown("---")
    with st.expander("🆕 **Primary Market: Brand New Shares**", expanded=True):
        st.markdown("""
        ### What is the Primary Market?
        
        The **Primary Market** is where a company sells its shares **for the first time** to raise capital.
        This typically happens through an **Initial Public Offering (IPO)**.
        
        **Key Points:**
        - 🎯 **Direct from Company**: You buy shares directly from the company
        - 💰 **Company Gets Money**: Your money goes straight to the company
        - 🆕 **Brand New Shares**: These are newly created shares
        - 🎪 **Special Event**: IPOs are rare, one-time events for each company
        
        ### After the IPO
        - Companies can issue more shares later through **Follow-On Public Offerings (FPO)**
        - These are NOT IPOs, but allow companies to raise additional money
        """)
        
        if st.button("⭐ Bookmark Primary Market Info", key="primary_bookmark"):
            add_to_bookmarks("Primary Market", "Where companies sell shares for the first time through IPOs")
    
    # Secondary Market Section
    with st.expander("🔄 **Secondary Market: Trading Among Investors**", expanded=True):
        st.markdown("""
        ### What is the Secondary Market?
        
        The **Secondary Market** is where investors buy and sell **existing shares** with each other 
        on stock exchanges like NYSE, NASDAQ, NSE, or BSE.
        
        **Key Points:**
        - 👥 **Investor to Investor**: You buy from other investors, not the company
        - 🚫 **Company Gets Nothing**: The company doesn't receive money from these trades
        - 🔄 **Continuous Trading**: Markets are open for trading most business days
        - 💧 **Provides Liquidity**: Makes it easy to buy and sell shares anytime
        
        ### Why This Matters for Companies
        Even though companies don't get money from secondary market trades:
        - 📈 **Increases Confidence**: Liquid markets make investors more willing to buy IPOs
        - 🚀 **Future Fundraising**: Strong secondary market performance helps with future offerings
        """)
        
        if st.button("⭐ Bookmark Secondary Market Info", key="secondary_bookmark"):
            add_to_bookmarks("Secondary Market", "Where investors trade existing shares among themselves")
    
    # Visual Comparison
    st.markdown("---")
    st.markdown("## 📊 Primary vs Secondary Market Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        ### 🆕 PRIMARY MARKET
        
        **When:** During IPO or FPO
        **Who:** Company → You
        **Purpose:** Company raises money
        **Frequency:** Rare events
        **Price:** Set by company/underwriters
        **Example:** Buying Tesla stock during its IPO
        """)
    
    with col2:
        st.success("""
        ### 🔄 SECONDARY MARKET
        
        **When:** Every trading day
        **Who:** Investor → You
        **Purpose:** Trading existing shares
        **Frequency:** Continuous
        **Price:** Set by supply & demand
        **Example:** Buying Tesla stock on NASDAQ today
        """)
    
    # Real-world Analogy
    st.markdown("---")
    with st.expander("🏠 **House Buying Analogy**", expanded=True):
        st.markdown("""
        **Think of Stock Markets Like Real Estate:**
        
        ### 🏗️ Primary Market = New Construction
        - Builder (company) constructs new houses (issues new shares)
        - You buy directly from the builder (IPO)
        - Builder gets your money to build more houses
        - Limited availability - only when builder has new houses
        
        ### 🏠 Secondary Market = Existing Homes
        - Homeowners (current investors) sell to new buyers (you)
        - You buy from current owner, not the original builder
        - Builder doesn't get money from this sale
        - Available anytime someone wants to sell
        
        **The Key Insight:**
        Just like most house purchases happen in the existing home market, 
        most stock purchases happen in the secondary market!
        """)
        
        if st.button("⭐ Bookmark House Analogy", key="house_analogy"):
            add_to_bookmarks("House Buying Analogy", "Primary market = new construction, Secondary market = existing homes")
    
    # How to Actually Buy Stocks
    st.markdown("---")
    st.markdown("## 💻 How to Actually Buy Stocks Today")
    
    st.markdown("""
    ### 🔍 For Most Investors (Secondary Market):
    
    **Step 1: Choose a Broker**
    - Online brokers (like Robinhood, E*TRADE, Zerodha)
    - Traditional brokers with physical locations
    - Robo-advisors for automated investing
    
    **Step 2: Open an Account**
    - Provide identification and financial information
    - Fund your account (bank transfer, check, etc.)
    - Complete any required paperwork
    
    **Step 3: Research and Buy**
    - Search for the stock you want
    - Place your order (market order, limit order, etc.)
    - Confirm your purchase
    
    **Step 4: Monitor Your Investment**
    - Track performance over time
    - Make decisions about buying more or selling
    """)
    
    # Interactive Quiz
    st.markdown("---")
    st.markdown("## 🧠 Test Your Market Knowledge")
    
    with st.form("market_quiz"):
        q1 = st.radio(
            "When you buy Apple stock today on the stock exchange, who receives your money?",
            ["Apple Inc. (the company)", "Another investor selling their Apple shares", "The stock exchange", "The government"],
            key="market_q1"
        )
        
        q2 = st.radio(
            "What is an IPO?",
            ["A way to buy stocks cheaply", "When a company sells shares to the public for the first time", "A type of stock exchange", "When stock prices go up"],
            key="market_q2"
        )
        
        q3 = st.radio(
            "Which market provides more buying opportunities for regular investors?",
            ["Primary Market", "Secondary Market", "Both are equal", "Neither"],
            key="market_q3"
        )
        
        submitted = st.form_submit_button("Check My Understanding")
        
        if submitted:
            score = 0
            
            if q1 == "Another investor selling their Apple shares":
                st.success("✅ Correct! In secondary market trading, you buy from other investors.")
                score += 1
            else:
                st.error("❌ When buying on exchanges, you're buying from other investors, not the company.")
            
            if q2 == "When a company sells shares to the public for the first time":
                st.success("✅ Correct! IPO = Initial Public Offering.")
                score += 1
            else:
                st.error("❌ IPO stands for Initial Public Offering - the first time a company sells shares publicly.")
            
            if q3 == "Secondary Market":
                st.success("✅ Correct! Secondary markets are open daily for trading.")
                score += 1
            else:
                st.error("❌ Secondary markets provide more opportunities since they're open for trading every business day.")
            
            st.info(f"Your Score: {score}/3")
            
            if score == 3:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("3_🛒_Where_to_Buy_Stocks")
                st.success("🎉 Perfect! You understand how stock markets work!")
            elif score >= 2:
                st.info("Great job! Review the areas you missed.")
            else:
                st.warning("Keep studying! Understanding markets is crucial for investing.")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways")
    
    st.info("""
    **Essential Points to Remember:**
    
    1. 🆕 **Primary Market**: Company sells new shares directly (IPO/FPO) - rare events
    2. 🔄 **Secondary Market**: Investors trade existing shares daily - where most buying happens
    3. 💰 **Money Flow**: Primary market money goes to company, secondary market money goes to selling investor
    4. 🌊 **Liquidity**: Secondary markets make it easy to buy/sell anytime
    5. 🏠 **Think Real Estate**: New construction vs existing homes market
    """)
    
    if st.button("⭐ Bookmark Key Takeaways", key="takeaways"):
        add_to_bookmarks("Stock Markets - Key Takeaways", "Understanding primary vs secondary markets")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/2_🏢_Why_Companies_Go_Public.py")
    
    with col3:
        if st.button("Next: Stock Exchanges →", use_container_width=True):
            st.switch_page("pages/4_📊_Stock_Exchanges.py")

if __name__ == "__main__":
    main()
