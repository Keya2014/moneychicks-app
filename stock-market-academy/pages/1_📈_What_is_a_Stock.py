import streamlit as st
from utils.progress_tracker import ProgressTracker

st.set_page_config(
    page_title="What is a Stock? - Stock Market Academy",
    page_icon="📈",
    layout="wide"
)

# Initialize progress tracker
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

# Initialize bookmarks
if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "What is a Stock"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def main():
    st.title("📈 What is a Stock?")
    st.markdown("### *Understanding the Building Blocks of Investment*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Back to Home"):
            st.switch_page("app.py")
    with col3:
        if st.button("Next: Why Companies Go Public →"):
            st.switch_page("pages/2_🏢_Why_Companies_Go_Public.py")
    
    st.markdown("---")
    
    # Main content
    with st.container():
        st.markdown("""
        ## 🤔 The Simple Definition
        
        A **stock** is a type of investment that represents **partial ownership** in a company. 
        When you buy a stock, you are essentially buying a "share" of that company, which means 
        you own a small piece of it.
        """)
        
        # Bookmark button for definition
        if st.button("⭐ Bookmark Definition", key="def_bookmark"):
            add_to_bookmarks("Stock Definition", "A stock represents partial ownership in a company")
    
    st.markdown("---")
    
    # Everyday Analogy Section
    with st.expander("👜 **Everyday Analogy: The Designer Handbag**", expanded=True):
        st.markdown("""
        Think of buying a stock like **joining a group of friends to buy a designer handbag together**.
        
        **Here's how it works:**
        - 🛍️ **The Purchase**: You and your friends pool money to buy an expensive designer bag
        - 📈 **Value Increases**: If the handbag's value increases over time, you all benefit when it's sold
        - 📉 **Value Decreases**: If the value drops, you share in that loss
        - 💰 **Your Share**: The more you invest, the bigger your share of the profits (or losses)
        
        **In Stock Terms:**
        - The handbag = The company
        - Your contribution = Your investment
        - Your friends = Other shareholders
        - The bag's changing value = The stock price movement
        """)
        
        if st.button("⭐ Bookmark Handbag Analogy", key="handbag_bookmark"):
            add_to_bookmarks("Handbag Analogy", "Buying stocks is like joining friends to buy a designer handbag together")
    
    # Visual representation
    st.markdown("---")
    st.markdown("## 🏢 What Does Stock Ownership Really Mean?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 **As a Shareholder, You Get:**
        
        - **Voting Rights**: Say in major company decisions
        - **Dividend Potential**: Share of company profits (if paid)
        - **Growth Participation**: Benefit from company success
        - **Ownership Stake**: Actual piece of the business
        """)
    
    with col2:
        st.markdown("""
        ### ⚠️ **Important to Remember:**
        
        - **Risk Involved**: You can lose money if company struggles
        - **No Guarantees**: Past performance doesn't predict future
        - **Market Fluctuations**: Stock prices go up and down daily
        - **Research Needed**: Understanding the company is crucial
        """)
    
    # Interactive Quiz Section
    st.markdown("---")
    st.markdown("## 🧠 Quick Knowledge Check")
    
    with st.form("stock_quiz"):
        st.markdown("**Test your understanding:**")
        
        q1 = st.radio(
            "When you buy a stock, you become:",
            ["A lender to the company", "A partial owner of the company", "An employee of the company", "A customer of the company"],
            key="q1"
        )
        
        q2 = st.radio(
            "In the handbag analogy, what does your investment amount represent?",
            ["The price of the handbag", "Your share of ownership", "The store where you buy", "The friends you're with"],
            key="q2"
        )
        
        submitted = st.form_submit_button("Check My Answers")
        
        if submitted:
            score = 0
            if q1 == "A partial owner of the company":
                st.success("✅ Correct! You become a partial owner.")
                score += 1
            else:
                st.error("❌ Not quite. When you buy stock, you become a partial owner of the company.")
            
            if q2 == "Your share of ownership":
                st.success("✅ Correct! Your investment determines your ownership share.")
                score += 1
            else:
                st.error("❌ Not quite. Your investment amount determines your share of ownership.")
            
            st.info(f"Your Score: {score}/2")
            
            if score == 2:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("1_📈_What_is_a_Stock")
                st.success("🎉 Perfect! You've mastered the basics of what a stock is!")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways")
    
    with st.container():
        st.info("""
        **Remember These Important Points:**
        
        1. 🏢 **Stocks = Ownership**: You're buying a piece of a real business
        2. 💰 **Risk & Reward**: Higher potential returns come with higher risk
        3. 🤝 **Shared Journey**: You succeed or struggle along with the company
        4. 📚 **Knowledge is Power**: Understanding the business is crucial for success
        5. ⏰ **Long-term Perspective**: Stock investing works best over time
        """)
        
        if st.button("⭐ Bookmark Key Takeaways", key="takeaways_bookmark"):
            add_to_bookmarks("Stock Basics - Key Takeaways", "5 essential points about stock ownership")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("🔍 Search Topics", use_container_width=True):
            st.switch_page("pages/8_🔍_Search_Topics.py")
    
    with col3:
        if st.button("Next: Why Go Public? →", use_container_width=True):
            st.switch_page("pages/2_🏢_Why_Companies_Go_Public.py")

if __name__ == "__main__":
    main()
