import streamlit as st
from utils.progress_tracker import ProgressTracker
from utils.content_data import get_welcome_content

# Configure page
st.set_page_config(
    page_title="Stock Market Academy for Women",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize progress tracker
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

# Initialize bookmarks
if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def main():
    # Header
    st.title("📈 Stock Market Academy for Women")
    st.markdown("### *Empowering Financial Independence Through Education*")
    
    # Welcome section
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Welcome to Your Financial Journey! 🌟
        
        Learning about the stock market doesn't have to be intimidating. This academy is designed 
        specifically for women who want to understand investing and build their financial confidence.
        
        **What you'll learn:**
        - 📊 Stock market fundamentals in simple terms
        - 💡 Real-world analogies that make complex concepts clear
        - 🎯 Practical knowledge for making informed investment decisions
        - 📈 How to read market trends and indices
        """)
        
        # Quick start buttons
        st.markdown("### 🚀 Quick Start Options")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🔰 Start with Basics", use_container_width=True):
                st.switch_page("pages/1_📈_What_is_a_Stock.py")
        
        with col_b:
            if st.button("🔍 Search Topics", use_container_width=True):
                st.switch_page("pages/8_🔍_Search_Topics.py")
        
        with col_c:
            if st.button("⭐ My Bookmarks", use_container_width=True):
                st.switch_page("pages/9_⭐_Bookmarks.py")
    
    with col2:
        # Progress overview
        st.markdown("### 📊 Your Progress")
        progress = st.session_state.progress_tracker.get_overall_progress()
        st.progress(progress / 100)
        st.write(f"**{progress:.0f}% Complete**")
        
        # Learning path
        st.markdown("### 📚 Learning Path")
        learning_modules = [
            ("📈 What is a Stock", "1_📈_What_is_a_Stock"),
            ("🏢 Why Companies Go Public", "2_🏢_Why_Companies_Go_Public"),
            ("🛒 Where to Buy Stocks", "3_🛒_Where_to_Buy_Stocks"),
            ("📊 Stock Exchanges", "4_📊_Stock_Exchanges"),
            ("💰 Stock Pricing", "5_💰_Stock_Pricing"),
            ("☕ Market Analogies", "6_☕_Market_Analogies"),
            ("📋 Market Indices", "7_📋_Market_Indices")
        ]
        
        for title, page_key in learning_modules:
            completed = st.session_state.progress_tracker.is_completed(page_key)
            if completed:
                st.success(f"✅ {title}")
            else:
                st.info(f"⏳ {title}")
    
    # Featured content section
    st.markdown("---")
    st.markdown("## 🌟 Featured Learning Modules")
    
    # Create cards for featured modules
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown("""
            <div style="padding: 1rem; border-radius: 10px; border: 1px solid #e0e0e0;">
            <h4>📈 Stock Basics</h4>
            <p>Start with the fundamentals - learn what stocks are and why they matter for your financial future.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Start Learning", key="basics", use_container_width=True):
                st.switch_page("pages/1_📈_What_is_a_Stock.py")
    
    with col2:
        with st.container():
            st.markdown("""
            <div style="padding: 1rem; border-radius: 10px; border: 1px solid #e0e0e0;">
            <h4>☕ Fun Analogies</h4>
            <p>Understand complex market concepts through relatable analogies like coffee trends and beauty products.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Explore Analogies", key="analogies", use_container_width=True):
                st.switch_page("pages/6_☕_Market_Analogies.py")
    
    with col3:
        with st.container():
            st.markdown("""
            <div style="padding: 1rem; border-radius: 10px; border: 1px solid #e0e0e0;">
            <h4>📋 Market Indices</h4>
            <p>Demystify market indices like Nifty 50 and S&P 500 with easy-to-understand explanations.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Learn Indices", key="indices", use_container_width=True):
                st.switch_page("pages/7_📋_Market_Indices.py")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
    <h4>💪 Building Financial Confidence, One Lesson at a Time</h4>
    <p>Remember: Every expert was once a beginner. Your financial journey starts here!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

