import streamlit as st
from utils.progress_tracker import ProgressTracker
import plotly.graph_objects as go

st.set_page_config(
    page_title="Market Analogies - Stock Market Academy",
    page_icon="☕",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Market Analogies"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def create_trend_chart():
    """Create a chart showing coffee vs matcha popularity over time"""
    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    coffee_popularity = [100, 102, 105, 108, 110, 112, 115]
    matcha_popularity = [15, 20, 35, 55, 80, 120, 150]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=coffee_popularity,
        mode='lines+markers',
        name='Coffee (Blue-Chip)',
        line=dict(color='brown', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=matcha_popularity,
        mode='lines+markers',
        name='Matcha (Growth Stock)',
        line=dict(color='green', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Coffee vs Matcha Popularity Trend",
        xaxis_title="Year",
        yaxis_title="Popularity Index",
        showlegend=True,
        height=400
    )
    
    return fig

def main():
    st.title("☕ Understanding Markets Through Fun Analogies")
    st.markdown("### *Making Complex Concepts Simple and Relatable*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: Stock Pricing"):
            st.switch_page("pages/5_💰_Stock_Pricing.py")
    with col3:
        if st.button("Next: Market Indices →"):
            st.switch_page("pages/7_📋_Market_Indices.py")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## 🎭 Why Analogies Matter
    
    Stock market concepts can seem abstract and intimidating. But when we compare them to 
    everyday experiences - like coffee trends or beauty shopping - they become much clearer!
    
    Let's explore some powerful analogies that will help you understand market dynamics.
    """)
    
    # Coffee and Matcha Analogy
    st.markdown("---")
    with st.expander("☕ **Coffee vs Matcha: The Ultimate Stock Market Story**", expanded=True):
        st.markdown("""
        ## ☕ vs 🍵 Coffee and Matcha: A Stock Market Analogy
        
        This analogy perfectly explains different types of stocks and market dynamics!
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### ☕ **Coffee = Blue-Chip Stock**
            
            **📊 Characteristics:**
            - 🌍 **Ubiquitous**: Consumed worldwide daily
            - 🏛️ **Established**: Long history of reliability
            - 📈 **Steady Growth**: Consistent, predictable demand
            - 💪 **Stable**: Trusted by millions of people
            - 🔄 **Consistent**: People depend on it daily
            
            **💰 Investment Parallel:**
            - Think companies like Coca-Cola, Microsoft, or Johnson & Johnson
            - Reliable returns over time
            - Less exciting but more predictable
            - Good for long-term wealth building
            """)
        
        with col2:
            st.markdown("""
            ### 🍵 **Matcha = Growth Stock**
            
            **🚀 Characteristics:**
            - ⭐ **Trendy**: Recently surged in popularity
            - 💊 **Health Focus**: Rides wellness trends
            - 📈 **Rapid Growth**: Market value growing fast
            - 🎯 **Targeted**: Appeals to specific demographics
            - 📱 **Social Media**: Driven by influencers
            
            **💰 Investment Parallel:**
            - Think companies like Tesla, Zoom, or TikTok
            - High potential returns
            - More volatile and risky
            - Can make or lose money quickly
            """)
        
        st.markdown("---")
        
        # Trend visualization
        st.plotly_chart(create_trend_chart(), use_container_width=True)
        
        if st.button("⭐ Bookmark Coffee vs Matcha", key="coffee_matcha"):
            add_to_bookmarks("Coffee vs Matcha Analogy", "Blue-chip stocks (coffee) vs growth stocks (matcha)")
    
    # Investment Strategy Lessons
    st.markdown("---")
    with st.expander("🎯 **Investment Strategy Lessons from Beverages**", expanded=True):
        st.markdown("""
        ## 💡 What This Teaches Us About Investing
        
        ### 🔮 **Foresight and Early Investment**
        
        **🏆 The Early Winners:**
        - People who spotted the matcha trend early made big profits
        - They noticed health trends, influencer endorsements, new products
        - "Bought in" early when matcha was still niche
        - Reaped rewards as popularity and prices soared
        
        **📈 Stock Market Parallel:**
        - Early Tesla investors saw the electric vehicle trend
        - Early Amazon investors recognized e-commerce potential
        - Early Apple investors understood smartphone revolution
        
        ### 🤔 **The Skeptics and Long-Term Holders**
        
        **☕ Coffee Loyalists Say:**
        - "Matcha is just a fad - coffee will always dominate"
        - "I'll stick with my reliable, steady coffee investment"
        - "Coffee has global appeal and staying power"
        
        **📊 Stock Market Parallel:**
        - Value investors stick with established companies
        - They believe proven businesses will outlast trendy newcomers
        - Focus on long-term stability over short-term excitement
        
        ### 🔄 **Market Adaptation**
        
        **🏢 Smart Companies Adapt:**
        - Coffee companies started offering matcha products
        - Starbucks added matcha lattes to compete
        - Diversification helped them capture both trends
        
        **💼 Business Parallel:**
        - Microsoft adapted from software to cloud services
        - Netflix shifted from DVDs to streaming
        - Companies that adapt survive and thrive
        """)
        
        if st.button("⭐ Bookmark Investment Lessons", key="investment_lessons"):
            add_to_bookmarks("Investment Strategy Lessons", "What coffee vs matcha teaches about investment timing and strategy")
    
    # Beauty Products Analogy
    st.markdown("---")
    with st.expander("💄 **The Beauty Basket: Understanding Market Indices**", expanded=True):
        st.markdown("""
        ## 💄 Beauty Products Analogy: The Beauty Basket
        
        Want to understand how market indices work? Let's go shopping! 🛍️
        
        ### 🧺 **Creating Your Beauty Basket**
        
        Imagine you want to track how the entire beauty industry is performing, but you don't have time 
        to check every single product. So you create a "Beauty Basket" with key products:
        
        **🛍️ Your Beauty Basket Contains:**
        - 💋 **Famous Lipstick** (represents makeup category)
        - 🧴 **Trending Moisturizer** (represents skincare)
        - 🧴 **Top Shampoo** (represents hair care)
        - 🌸 **Bestselling Perfume** (represents fragrance)
        - 😌 **Cult-Favorite Face Mask** (represents treatments)
        
        ### 📊 **How This Works Like a Stock Index**
        
        **📈 Tracking Performance:**
        - Every week, check if basket prices went up or down
        - If most products get more expensive → Beauty industry is booming! 📈
        - If prices drop → Industry might be struggling 📉
        
        **🎯 Why Use a Beauty Basket?**
        - **Quick Snapshot**: No need to track every beauty product
        - **Representative**: Key items reflect overall market health
        - **Efficient**: One number tells the whole story
        
        **📊 Stock Market Parallel:**
        - **S&P 500**: Basket of 500 major US companies
        - **Nifty 50**: Basket of 50 top Indian companies
        - **NASDAQ**: Basket focused on technology companies
        
        ### 💡 **Key Insights**
        
        **🔍 Just like your beauty basket:**
        - Stock indices give you a quick market overview
        - You don't need to analyze every individual stock
        - One index number tells you if the market is up or down
        - Different indices focus on different market segments
        """)
        
        if st.button("⭐ Bookmark Beauty Basket", key="beauty_basket"):
            add_to_bookmarks("Beauty Basket Analogy", "How market indices work like tracking a basket of beauty products")
    
    # Weighted Analogy
    st.markdown("---")
    with st.expander("⚖️ **The Seesaw Effect: Why All Stocks Aren't Equal**", expanded=True):
        st.markdown("""
        ## ⚖️ Understanding Index Weighting
        
        **🤔 The Question:** "In a 50-company index, does each company have a 2% effect?"
        
        **❌ Answer: NO!** Here's why using a seesaw analogy:
        
        ### 🎪 **The Seesaw Playground**
        
        **👥 Imagine a seesaw with 5 people:**
        - 🏋️ **Big Person (200 lbs)**: Represents large companies like Apple, Microsoft
        - 👤 **Medium Person (150 lbs)**: Represents mid-size companies
        - 👦 **Small Person (100 lbs)**: Represents smaller companies
        - 👧 **Child (75 lbs)**: Represents even smaller companies
        - 👶 **Toddler (25 lbs)**: Represents tiny companies
        
        ### ⚖️ **How Weight Affects the Seesaw**
        
        **🏋️ The Big Person's Impact:**
        - Can tip the entire seesaw by themselves
        - Their movement affects everyone else
        - Has much more influence than the toddler
        
        **👶 The Toddler's Impact:**
        - Barely affects the seesaw's balance
        - Could jump up and down with minimal effect
        - Needs help from others to make a difference
        
        ### 📊 **Stock Market Translation**
        
        **🏢 Large Companies (High Weight):**
        - Apple might be 7% of the S&P 500
        - Microsoft might be 6% of the index
        - Their price movements have huge impact
        
        **🏬 Small Companies (Low Weight):**
        - Might only be 0.1% of the index
        - Price changes barely affect the overall index
        - Need many small companies to move together for impact
        
        ### 💡 **The Key Insight**
        
        **📊 All weights add up to 100%:**
        - Just like everyone on the seesaw contributes to total weight
        - But bigger companies have much more influence
        - The index reflects combined effect, but not equally!
        """)
        
        # Interactive weight demonstration
        st.markdown("#### 🎮 Interactive Weight Demo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🏢 Company Weights in Index:**")
            companies = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Tesla', '45 Other Companies']
            weights = [7.0, 6.5, 3.2, 4.1, 2.2, 77.0]
            
            for company, weight in zip(companies, weights):
                st.progress(weight/100, text=f"{company}: {weight}%")
        
        with col2:
            st.info("""
            **🎯 Notice:**
            
            - Top 5 companies = 23% of index
            - Remaining 45 companies = 77% of index  
            - Apple alone has 35x more impact than average small company
            - This is why big tech companies can move entire markets!
            """)
        
        if st.button("⭐ Bookmark Seesaw Weighting", key="seesaw_weight"):
            add_to_bookmarks("Seesaw Index Weighting", "Why larger companies have more impact on market indices")
    
    # Quiz Section
    st.markdown("---")
    st.markdown("## 🧠 Analogy Knowledge Check")
    
    with st.form("analogy_quiz"):
        q1 = st.radio(
            "In the coffee vs matcha analogy, what type of stock does coffee represent?",
            ["Growth stock", "Blue-chip stock", "Penny stock", "International stock"],
            key="analogy_q1"
        )
        
        q2 = st.radio(
            "What does the 'Beauty Basket' analogy help explain?",
            ["How to buy beauty products", "How market indices work", "How to start a beauty business", "How to invest in beauty companies"],
            key="analogy_q2"
        )
        
        q3 = st.radio(
            "In the seesaw analogy, why don't all companies have equal impact on an index?",
            ["Some companies are older", "Larger companies have more weight/influence", "Some companies are more popular", "It's random"],
            key="analogy_q3"
        )
        
        submitted = st.form_submit_button("Test My Understanding")
        
        if submitted:
            score = 0
            
            if q1 == "Blue-chip stock":
                st.success("✅ Correct! Coffee represents stable, established blue-chip stocks.")
                score += 1
            else:
                st.error("❌ Coffee represents blue-chip stocks - stable and established.")
            
            if q2 == "How market indices work":
                st.success("✅ Right! The beauty basket shows how indices track market segments.")
                score += 1
            else:
                st.error("❌ The beauty basket analogy explains how market indices work.")
            
            if q3 == "Larger companies have more weight/influence":
                st.success("✅ Perfect! Larger companies have more impact, just like heavier people on a seesaw.")
                score += 1
            else:
                st.error("❌ Like a seesaw, larger companies have more weight and influence in indices.")
            
            st.info(f"Your Score: {score}/3")
            
            if score == 3:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("6_☕_Market_Analogies")
                st.success("🎉 Fantastic! You've mastered market analogies!")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways from Market Analogies")
    
    st.info("""
    **💡 What These Analogies Teach Us:**
    
    1. ☕ **Coffee vs Matcha**: Different stocks have different risk/reward profiles
    2. 🔮 **Timing Matters**: Early trend spotters can benefit significantly  
    3. 💄 **Beauty Basket**: Indices simplify complex market tracking
    4. ⚖️ **Seesaw Effect**: Not all companies have equal market impact
    5. 🧠 **Everyday Comparisons**: Complex concepts become clearer with relatable analogies
    """)
    
    if st.button("⭐ Bookmark All Key Takeaways", key="all_takeaways"):
        add_to_bookmarks("Market Analogies - All Takeaways", "Key lessons from coffee/matcha, beauty basket, and seesaw analogies")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/5_💰_Stock_Pricing.py")
    
    with col3:
        if st.button("Next: Market Indices →", use_container_width=True):
            st.switch_page("pages/7_📋_Market_Indices.py")

if __name__ == "__main__":
    main()
