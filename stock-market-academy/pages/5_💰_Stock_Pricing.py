import streamlit as st
from utils.progress_tracker import ProgressTracker
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Stock Pricing - Stock Market Academy",
    page_icon="💰",
    layout="wide"
)

# Initialize progress tracker and bookmarks
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Stock Pricing"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def create_supply_demand_chart():
    """Create a simple supply and demand visualization"""
    fig = go.Figure()
    
    # Supply line (upward sloping)
    fig.add_trace(go.Scatter(
        x=[10, 30, 50, 70, 90],
        y=[20, 40, 60, 80, 100],
        mode='lines+markers',
        name='Supply',
        line=dict(color='red', width=3),
        marker=dict(size=8)
    ))
    
    # Demand line (downward sloping)
    fig.add_trace(go.Scatter(
        x=[10, 30, 50, 70, 90],
        y=[100, 80, 60, 40, 20],
        mode='lines+markers',
        name='Demand',
        line=dict(color='blue', width=3),
        marker=dict(size=8)
    ))
    
    # Equilibrium point
    fig.add_trace(go.Scatter(
        x=[50],
        y=[60],
        mode='markers',
        name='Market Price',
        marker=dict(size=15, color='green', symbol='star')
    ))
    
    fig.update_layout(
        title="How Supply and Demand Determine Stock Price",
        xaxis_title="Quantity of Shares",
        yaxis_title="Price ($)",
        showlegend=True,
        height=400
    )
    
    return fig

def main():
    st.title("💰 How Are Stock Prices Determined?")
    st.markdown("### *The Magic of Supply and Demand*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous: Stock Exchanges"):
            st.switch_page("pages/4_📊_Stock_Exchanges.py")
    with col3:
        if st.button("Next: Market Analogies →"):
            st.switch_page("pages/6_☕_Market_Analogies.py")
    
    st.markdown("---")
    
    # The Big Question
    st.markdown("""
    ## 🤔 Who Sets Stock Prices?
    
    You might wonder: *"Does someone like a boss or even the President decide stock prices?"*
    
    **The surprising answer: It's YOU - the general public!** 👥
    
    Stock prices are determined by the basic principle of **supply and demand** in the market.
    """)
    
    # Supply and Demand Visualization
    st.markdown("---")
    st.markdown("## 📊 Supply and Demand in Action")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.plotly_chart(create_supply_demand_chart(), use_container_width=True)
    
    with col2:
        st.markdown("""
        ### 📈 **How It Works:**
        
        **📊 High Demand + Low Supply = Price Goes UP** ⬆️
        - More people want to buy than sell
        - Buyers compete by offering higher prices
        - Stock price rises
        
        **📉 Low Demand + High Supply = Price Goes DOWN** ⬇️
        - More people want to sell than buy
        - Sellers compete by accepting lower prices
        - Stock price falls
        
        **⚖️ Equal Supply and Demand = Stable Price**
        - Market finds equilibrium
        - Price remains relatively steady
        """)
    
    # What Influences Stock Prices
    st.markdown("---")
    st.markdown("## 🎯 What Influences Stock Prices?")
    
    # Create tabs for different factors
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏢 Company Performance", "🌍 Economic Conditions", "🏭 Industry Trends", "😊 Market Sentiment", "📰 News & Events"])
    
    with tab1:
        st.markdown("""
        ### 🏢 **Company Performance**
        
        **📈 What Drives Prices UP:**
        - 💰 Strong profits and revenue growth
        - 🎯 Beating earnings expectations
        - 🚀 Successful product launches
        - 👥 Strong leadership and management
        - 📊 Positive future guidance
        
        **📉 What Drives Prices DOWN:**
        - 💸 Declining profits or losses
        - 😞 Missing earnings expectations
        - 🚫 Failed products or projects
        - 🔄 Management changes or scandals
        - ⚠️ Negative outlook or warnings
        """)
        
        if st.button("⭐ Bookmark Company Factors", key="company_factors"):
            add_to_bookmarks("Company Performance Factors", "How company results affect stock prices")
    
    with tab2:
        st.markdown("""
        ### 🌍 **Economic Conditions**
        
        **📊 Key Economic Factors:**
        - 📈 **Economic Growth (GDP)**: Strong economy = higher stock prices
        - 💸 **Inflation**: High inflation can hurt stock prices
        - 🏦 **Interest Rates**: Low rates = more attractive stocks
        - 👥 **Employment**: Low unemployment = confident consumers
        - 🏛️ **Government Policies**: Tax changes, regulations
        
        **💡 Why This Matters:**
        - Good economy = people have more money to invest
        - Bad economy = people sell stocks and save cash
        - Interest rates affect how attractive stocks are vs bonds
        """)
    
    with tab3:
        st.markdown("""
        ### 🏭 **Industry Trends**
        
        **🔄 Sector Movement:**
        - Stocks in the same industry often move together
        - New technology can boost entire sectors
        - Regulations can impact whole industries
        
        **📱 Examples:**
        - Tech boom → All tech stocks rise
        - Oil price spike → Energy stocks benefit
        - Health crisis → Healthcare stocks gain
        - Environmental focus → Green energy stocks rise
        """)
    
    with tab4:
        st.markdown("""
        ### 😊 **Market Sentiment**
        
        **🐂 Bull Markets (Optimistic):**
        - Investors feel confident about the future
        - People buy more, driving prices up
        - "Risk-on" mentality prevails
        
        **🐻 Bear Markets (Pessimistic):**
        - Investors feel worried or fearful
        - People sell more, driving prices down
        - "Risk-off" mentality dominates
        
        **🎭 Emotional Reactions:**
        - Fear and greed drive many decisions
        - Market psychology can override logic
        - Herd mentality creates momentum
        """)
    
    with tab5:
        st.markdown("""
        ### 📰 **News and Events**
        
        **⚡ Immediate Impact Events:**
        - Earnings announcements
        - Merger and acquisition news
        - CEO changes or scandals
        - Product recalls or launches
        - Analyst upgrades/downgrades
        
        **🌍 Global Events:**
        - Political instability
        - Natural disasters
        - Global health crises
        - Trade wars or agreements
        - Currency fluctuations
        """)
    
    # Volatility Section
    st.markdown("---")
    with st.expander("🎢 **Understanding Volatility**", expanded=True):
        st.markdown("""
        ## 🎭 What Causes Price Swings?
        
        **Volatility** refers to how much and how quickly stock prices move up and down.
        
        ### 🌪️ **Causes of High Volatility:**
        
        **📺 Breaking News:**
        - Sudden announcements can cause immediate price jumps
        - Rumors (even false ones) can move markets
        - Unexpected events create uncertainty
        
        **😰 Emotional Reactions:**
        - Fear causes panic selling
        - Excitement causes buying frenzies
        - Uncertainty makes prices swing wildly
        
        **📊 Market Structure:**
        - High-frequency trading amplifies movements
        - Low trading volume makes prices more sensitive
        - Options and derivatives can increase volatility
        
        ### 🧘 **Managing Volatility:**
        - Focus on long-term trends, not daily movements
        - Understand that volatility is normal
        - Don't make emotional decisions during swings
        """)
        
        if st.button("⭐ Bookmark Volatility Info", key="volatility_info"):
            add_to_bookmarks("Stock Volatility", "Understanding why stock prices swing up and down")
    
    # Interactive Price Simulation
    st.markdown("---")
    st.markdown("## 🎮 Interactive Price Simulation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 **Scenario Simulator**")
        
        scenario = st.selectbox(
            "Choose a scenario:",
            [
                "Company reports record profits",
                "Company misses earnings badly",
                "Industry gets positive regulation",
                "Market crash due to economic fears",
                "Celebrity endorses the company",
                "Product recall announced"
            ]
        )
        
        if st.button("See Price Impact"):
            impact_map = {
                "Company reports record profits": ("📈 Stock price jumps 15%!", "success"),
                "Company misses earnings badly": ("📉 Stock price drops 20%", "error"),
                "Industry gets positive regulation": ("🚀 Sector-wide rally, +8%", "success"),
                "Market crash due to economic fears": ("💥 Everything falls, -25%", "error"),
                "Celebrity endorses the company": ("⭐ Social media buzz, +5%", "info"),
                "Product recall announced": ("⚠️ Safety concerns, -12%", "warning")
            }
            
            message, alert_type = impact_map[scenario]
            
            if alert_type == "success":
                st.success(message)
            elif alert_type == "error":
                st.error(message)
            elif alert_type == "warning":
                st.warning(message)
            else:
                st.info(message)
    
    with col2:
        st.markdown("### 💡 **Key Insights**")
        st.info("""
        **What This Shows:**
        
        1. 📊 **Company news** has the biggest impact
        2. 🌍 **Market-wide events** affect all stocks
        3. 📱 **Social media** can move prices quickly
        4. ⚠️ **Negative news** often has stronger impact than positive
        5. 🎯 **Expectations matter** - beating them is key
        """)
    
    # Quiz Section
    st.markdown("---")
    st.markdown("## 🧠 Price Discovery Quiz")
    
    with st.form("pricing_quiz"):
        q1 = st.radio(
            "What is the primary factor that determines stock prices?",
            ["The company CEO", "Government regulations", "Supply and demand", "The stock exchange"],
            key="pricing_q1"
        )
        
        q2 = st.radio(
            "If more people want to buy a stock than sell it, what happens to the price?",
            ["It goes down", "It goes up", "It stays the same", "It becomes volatile"],
            key="pricing_q2"
        )
        
        q3 = st.multiselect(
            "Which factors can influence stock prices? (Select all that apply)",
            ["Company earnings", "Economic conditions", "Market sentiment", "News events", "The weather", "Industry trends"],
            key="pricing_q3"
        )
        
        submitted = st.form_submit_button("Test My Understanding")
        
        if submitted:
            score = 0
            
            if q1 == "Supply and demand":
                st.success("✅ Correct! Supply and demand drive stock prices.")
                score += 1
            else:
                st.error("❌ Stock prices are determined by supply and demand in the market.")
            
            if q2 == "It goes up":
                st.success("✅ Right! High demand with low supply pushes prices up.")
                score += 1
            else:
                st.error("❌ When demand exceeds supply, prices rise.")
            
            correct_factors = {"Company earnings", "Economic conditions", "Market sentiment", "News events", "Industry trends"}
            selected_factors = set(q3)
            
            if correct_factors.issubset(selected_factors) and "The weather" not in selected_factors:
                st.success("✅ Perfect! You identified the key price factors.")
                score += 1
            else:
                st.error("❌ All except 'The weather' can influence stock prices!")
            
            st.info(f"Your Score: {score}/3")
            
            if score == 3:
                st.balloons()
                st.session_state.progress_tracker.mark_completed("5_💰_Stock_Pricing")
                st.success("🎉 Excellent! You understand how stock prices work!")
    
    # Key Takeaways
    st.markdown("---")
    st.markdown("## 🎯 Key Takeaways")
    
    st.info("""
    **Essential Pricing Principles:**
    
    1. 👥 **You Set Prices**: Stock prices are determined by all investors collectively
    2. ⚖️ **Supply vs Demand**: The fundamental force behind all price movements
    3. 🏢 **Company Performance**: The most important long-term price driver
    4. 🌍 **Multiple Factors**: Economics, sentiment, news all play roles
    5. 🎢 **Volatility is Normal**: Prices swing - focus on long-term trends
    """)
    
    if st.button("⭐ Bookmark Key Takeaways", key="takeaways"):
        add_to_bookmarks("Stock Pricing - Key Takeaways", "How supply, demand, and various factors determine stock prices")
    
    # Navigation footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("← Previous Topic", use_container_width=True):
            st.switch_page("pages/4_📊_Stock_Exchanges.py")
    
    with col3:
        if st.button("Next: Market Analogies →", use_container_width=True):
            st.switch_page("pages/6_☕_Market_Analogies.py")

if __name__ == "__main__":
    main()
