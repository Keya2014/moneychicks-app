import streamlit as st
from utils.progress_tracker import ProgressTracker

st.set_page_config(
    page_title="Why Companies Go Public - Stock Market Academy",
    page_icon="🏢",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Why Companies Go Public"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def main():
    st.title("🏢 Why Would Companies Sell Their Stocks?")
    st.markdown("### *Understanding the Journey from Private to Public*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: What is a Stock?"):
            st.switch_page("pages/1_📈_What_is_a_Stock.py")
    with col3:
        if st.button("Next: Where to Buy →"):
            st.switch_page("pages/3_🛒_Where_to_Buy_Stocks.py")
    
    st.markdown("---")
    
    # Main concept
    with st.container():
        st.markdown("""
        ## 💡 The Big Question: Why Share Ownership?
        
        You might wonder: *"If I owned a successful business, why would I want to share it with strangers?"*
        
        The answer is simple: **Money for Growth** 💰
        """)
    
    # Going Public Explanation
    st.markdown("---")
    with st.expander("🚀 **What Does 'Going Public' Mean?**", expanded=True):
        st.markdown("""
        **Going Public** (also called "listing") is when a private company decides to sell shares 
        to the general public for the first time.
        
        **Think of it like this:**
        - 🏠 **Before**: Your family business run from your garage
        - 🏢 **After**: Your business opens stores nationwide and anyone can become a part-owner
        """)
        
        if st.button("⭐ Bookmark Going Public Definition", key="public_def"):
            add_to_bookmarks("Going Public", "When a private company sells shares to the public for the first time")
    
    # Reasons for Going Public
    st.markdown("## 🎯 Why Companies Choose to Go Public")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💰 **Primary Reasons:**
        
        **1. Raise Capital for Growth**
        - Fund new projects and expansion
        - Enter new markets globally
        - Develop new products or services
        
        **2. Pay Off Existing Debt**
        - Reduce financial burden
        - Improve company stability
        - Lower interest payments
        """)
    
    with col2:
        st.markdown("""
        **3. Acquire Other Businesses**
        - Buy competitors or complementary companies
        - Expand market share quickly
        - Gain new technologies or expertise
        
        **4. Provide Exit Strategy**
        - Early investors can sell their shares
        - Founders can realize their investment
        - Employees with stock options benefit
        """)
    
    # Real-world analogy
    st.markdown("---")
    with st.expander("🍕 **Real-World Analogy: The Pizza Shop Story**", expanded=True):
        st.markdown("""
        **Meet Sarah's Pizza Shop:**
        
        **Stage 1 - Private Business** 🏪
        - Sarah owns a successful local pizza shop
        - She wants to open 50 locations across the country
        - Problem: She needs $5 million but only has $500,000
        
        **Stage 2 - Going Public Decision** 💭
        - Bank loan would cost too much in interest
        - She decides to sell 30% of her business to the public
        - 1,000 people each invest $5,000 to own shares
        
        **Stage 3 - After Going Public** 🚀
        - Sarah raises her $5 million
        - She keeps 70% ownership and control
        - 1,000 shareholders own the remaining 30%
        - Everyone benefits if the pizza chain succeeds!
        
        **The Win-Win:**
        - 📈 Sarah: Gets money to expand her dream
        - 💰 Investors: Own part of a potentially profitable business
        """)
        
        if st.button("⭐ Bookmark Pizza Shop Story", key="pizza_story"):
            add_to_bookmarks("Pizza Shop Analogy", "How Sarah's pizza shop went public to fund expansion")
    
    # Benefits and Trade-offs
    st.markdown("---")
    st.markdown("## ⚖️ The Trade-offs of Going Public")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ### ✅ **Benefits for Companies:**
        
        - 💰 Access to large amounts of capital
        - 📈 Increased company visibility and credibility
        - 💼 Ability to attract top talent with stock options
        - 🔄 Liquidity for early investors and employees
        - 🏆 Enhanced brand recognition and prestige
        """)
    
    with col2:
        st.warning("""
        ### ⚠️ **Challenges They Face:**
        
        - 📊 Must share financial information publicly
        - 👥 Pressure from shareholders for short-term profits
        - 📋 Increased regulatory requirements and costs
        - ⏰ Time-consuming reporting obligations
        - 🎯 Less control over business decisions
        """)
    
    # Interactive section
    st.markdown("---")
    st.markdown("## 🧠 Test Your Understanding")
    
    with st.form("public_quiz"):
        st.markdown("**Quick Check:** Why might a company choose to go public?")
        
        reasons = st.multiselect(
            "Select all correct reasons:",
            [
                "To raise money for expansion",
                "To pay off existing debt", 
                "To acquire other businesses",
                "To avoid paying taxes",
                "To provide exit opportunities for early investors",
                "To increase company visibility"
            ]
        )
        
        submitted = st.form_submit_button("Check My Answer")
        
        if submitted:
            correct_reasons = {
                "To raise money for expansion",
                "To pay off existing debt", 
                "To acquire other businesses",
                "To provide exit opportunities for early investors",
                "To increase company visibility"
            }
            
            selected_set = set(reasons)
            
            if "To avoid paying taxes" in selected_set:
                st.error("❌ Going public doesn't help avoid taxes - that's incorrect!")
            
            correct_selected = selected_set.intersection(correct_reasons)
            score = len(correct_selected)
            
            if score >= 4:
                st.success(f"🎉 Excellent! You selected {score} correct reasons!")
                st.balloons()
                st.session_state.progress_tracker.mark_completed("2_🏢_Why_Companies_Go_Public")
            elif score >= 2:
                st.info(f"Good job! You got {score} correct reasons. Review the content for the ones you missed.")
            else:
                st.warning("Keep learning! Review the reasons why companies go public.")
    
    # Key takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways")
    
    st.info("""
    **Remember:**
    
    1. 🚀 **Growth Needs Money**: Companies go public primarily to raise capital for expansion
    2. 🤝 **Shared Success**: When you buy stocks, you're helping companies grow while potentially profiting
    3. ⚖️ **Trade-offs Exist**: Companies gain money but lose some privacy and control
    4. 🌟 **Opportunity for You**: Public companies create investment opportunities for regular people
    5. 💡 **Win-Win Scenario**: Both companies and investors can benefit from this arrangement
    """)
    
    if st.button("⭐ Bookmark Key Takeaways", key="takeaways"):
        add_to_bookmarks("Going Public - Key Takeaways", "5 essential points about why companies go public")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/1_📈_What_is_a_Stock.py")
    
    with col3:
        if st.button("Next: Where to Buy →", use_container_width=True):
            st.switch_page("pages/3_🛒_Where_to_Buy_Stocks.py")

if __name__ == "__main__":
    main()
