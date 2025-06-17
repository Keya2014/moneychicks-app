import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="MoneyChicks - Financial Empowerment",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Enhanced Custom CSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1200px !important;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: -2rem -2rem 3rem -2rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .big-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5em;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.3em;
        color: rgba(255,255,255,0.9);
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .section-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8em;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #e2e8f0;
    }
    
    .card {
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.12);
    }
    
    .mission {
        background: linear-gradient(135deg, #ffeef8 0%, #fff0f8 100%);
        border-left: 5px solid #e91e63;
    }
    
    .manifesto {
        background: linear-gradient(135deg, #e3f2fd 0%, #f0f8ff 100%);
        border-left: 5px solid #2196f3;
    }
    
    .community {
        background: linear-gradient(135deg, #e8f5e8 0%, #f0fff0 100%);
        border-left: 5px solid #4caf50;
    }
    
    .financial-learning {
        background: linear-gradient(135deg, #fff3e0 0%, #ffeee0 100%);
        border-left: 5px solid #ff9800;
    }
    
    .calculator-section {
        background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .metric-value {
        font-size: 2em;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        color: #718096;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.9em;
        letter-spacing: 1px;
    }
    
    .ig-link {
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #4facfe 100%);
        border-radius: 50px;
        padding: 15px 30px;
        font-size: 1.1em;
        font-weight: 600;
        color: white !important;
        box-shadow: 0 8px 25px rgba(245, 87, 108, 0.4);
        text-decoration: none;
        transition: all 0.3s ease;
        margin-top: 1.5rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .ig-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(245, 87, 108, 0.6);
        color: white !important;
    }
    
    .ig-icon {
        font-size: 1.3em;
        margin-right: 10px;
    }
    
    .formula-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        font-family: 'Monaco', 'Consolas', monospace;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    .highlight-stat {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .footer {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        text-align: center;
        padding: 2rem;
        margin: 3rem -2rem -2rem -2rem;
        border-radius: 20px 20px 0 0;
    }
    
    /* Slider Styling */
    .stSlider > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
        border-radius: 10px;
        padding: 1rem;
        border: 1px solid #e2e8f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Main Header ---
st.markdown(
    """
    <div class="main-header">
        <div class="big-title">💜 MoneyChicks</div>
        <div class="subtitle">Empowering women to take control of their financial future through education, community, and smart investing</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Mission Section ---
st.markdown(
    """
    <div class="card mission">
        <h3 class="section-title">🌟 Our Mission</h3>
        <p style="font-size: 1.1em; line-height: 1.7; color: #2d3748;">Our mission is to <strong>simplify money</strong> and <strong>close the gender gap in investing</strong>.</p>
        <p style="font-style: italic; color: #4a5568; line-height: 1.6;">MoneyChicks was born as a reaction to the intimidating world of stock markets from an 18-year-old teenager's perspective. We wish to demystify, un-mansplain and foster inclusive conversation that helps women understand from scratch, without feeling stupid.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Manifesto Section ---
st.markdown(
    """
    <div class="card manifesto">
        <h3 class="section-title">🚀 Our Manifesto</h3>
        <p style="font-size: 1.1em; line-height: 1.7; color: #2d3748;">For the ones who've been left out of the narrative. For the ones that want to contradict conversations that don't expect them. We're the community for those who wish to <strong>challenge the tides of power</strong>, to take charge of what's theirs.</p>
        <div class="highlight-stat">
            <strong>We'll start you off to learn from the very beginning — All you need is to believe you can! 💪</strong>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Investment Calculator Section ---
st.markdown('<div class="calculator-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📈 Investment Growth Calculator</h2>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.1em; color: #4a5568; margin-bottom: 2rem;">See the power of compound interest and why starting early makes all the difference!</p>', unsafe_allow_html=True)

# Enhanced Layout
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### 🎯 Your Investment Parameters")
    starting_amount = st.slider("💰 Starting Amount (₹)", 0, 1000000, 10000, 5000)
    monthly_contribution = st.slider("📅 Monthly Contribution (₹)", 0, 200000, 5000, 1000)
    years = st.slider("⏳ Time Horizon (years)", 1, 40, 20, 1)
    
    # Enhanced metrics display
    total_contributions = starting_amount + (monthly_contribution * 12 * years)
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">₹{total_contributions:,.0f}</div>
            <div class="metric-label">Total You'll Invest</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Enhanced calculation logic
annual_return = 0.12  # Adjusted to 12% for better illustration
months = years * 12
monthly_return = annual_return / 12

# Calculate compound growth
investment_values = []
contribution_values = []
total_value = starting_amount

for month in range(months + 1):
    if month > 0:
        total_value += monthly_contribution
        total_value *= (1 + monthly_return)
    
    current_contributions = starting_amount + (monthly_contribution * month)
    investment_values.append(total_value)
    contribution_values.append(current_contributions)

# Create DataFrame for visualization
months_array = np.arange(0, months + 1)
df_detailed = pd.DataFrame({
    'Month': months_array,
    'Total Value': investment_values,
    'Contributions': contribution_values,
    'Returns': [inv - cont for inv, cont in zip(investment_values, contribution_values)]
})

# Yearly aggregation for cleaner display
years_range = list(range(2025, 2025 + years + 1))
yearly_data = []
for i, year in enumerate(years_range):
    month_index = i * 12
    if month_index < len(df_detailed):
        yearly_data.append({
            'Year': year,
            'Total Value': df_detailed.iloc[month_index]['Total Value'],
            'Contributions': df_detailed.iloc[month_index]['Contributions'],
            'Returns': df_detailed.iloc[month_index]['Returns']
        })

df_yearly = pd.DataFrame(yearly_data)

with col2:
    if len(df_yearly) > 0:
        final_value = df_yearly.iloc[-1]['Total Value']
        final_contributions = df_yearly.iloc[-1]['Contributions']
        final_returns = df_yearly.iloc[-1]['Returns']
        
        # Enhanced metrics
        col2a, col2b = st.columns(2)
        with col2a:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">₹{final_value:,.0f}</div>
                    <div class="metric-label">Final Investment Value</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2b:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">₹{final_returns:,.0f}</div>
                    <div class="metric-label">Returns Earned</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Enhanced Plotly chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Your Contributions',
            x=df_yearly['Year'],
            y=df_yearly['Contributions'],
            marker_color='rgba(102, 126, 234, 0.8)',
            hovertemplate='<b>Year:</b> %{x}<br><b>Contributions:</b> ₹%{y:,.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Bar(
            name='Investment Returns',
            x=df_yearly['Year'],
            y=df_yearly['Returns'],
            marker_color='rgba(245, 87, 108, 0.8)',
            hovertemplate='<b>Year:</b> %{x}<br><b>Returns:</b> ₹%{y:,.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            title=dict(
                text='<b>Your Wealth Growth Over Time</b>',
                font=dict(size=20, color='#2d3748'),
                x=0.5
            ),
            xaxis_title='Year',
            yaxis_title='Amount (₹)',
            barmode='stack',
            template='plotly_white',
            height=400,
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            ),
            font=dict(family="Poppins", size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # ROI calculation
        roi_percentage = (final_returns / final_contributions) * 100 if final_contributions > 0 else 0
        st.markdown(
            f"""
            <div class="highlight-stat">
                💡 Your money will grow by <strong>{roi_percentage:.1f}%</strong> through the power of compound interest!
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# --- Enhanced Formula Section ---
with st.expander("📚 Understanding Compound Interest Formula", expanded=False):
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%); padding: 2rem; border-radius: 15px; border: 1px solid #e2e8f0;">
        
        <h4 style="color: #4a5568; margin-bottom: 1rem;">The Magic Formula Behind Wealth Building</h4>
        
        <div class="formula-box">
            <strong>A = P(1 + r/n)^(nt)</strong>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #667eea;">
                <strong>A</strong> = Final amount<br><small>Your total wealth</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #f5576c;">
                <strong>P</strong> = Principal amount<br><small>Your starting investment</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;">
                <strong>r</strong> = Annual interest rate<br><small>Expected return %</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #ff9800;">
                <strong>n</strong> = Compounding frequency<br><small>How often interest compounds</small>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #9c27b0;">
                <strong>t</strong> = Time period<br><small>Years you invest</small>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, #e8f5e8 0%, #f0fff0 100%); padding: 1.5rem; border-radius: 10px; margin-top: 2rem;">
            <h5 style="color: #2e7d32; margin-bottom: 1rem;">💡 Key Insights:</h5>
            <ul style="color: #2d3748; line-height: 1.8;">
                <li><strong>Time is your best friend:</strong> Starting early gives compound interest more time to work</li>
                <li><strong>Consistency matters:</strong> Regular contributions accelerate your wealth building</li>
                <li><strong>Patience pays:</strong> The longer you stay invested, the more exponential your growth becomes</li>
            </ul>
        </div>
        
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Enhanced Financial Learning Section ---
st.markdown(
    """
    <div class="card financial-learning">
        <h3 class="section-title">🎓 Financial Education Hub</h3>
        <p style="font-size: 1.2em; line-height: 1.7; color: #2d3748; margin-bottom: 1.5rem;">
            <strong>Financial literacy is the foundation of women's empowerment.</strong> We've created an unparalleled learning environment where all questions are safe, because when knowledge is shared openly, your financial future becomes secure.
        </p>
        <div style="background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
            <p style="font-size: 1.1em; color: #2d3748; margin: 0;"><em>"Financial literacy gives you the freedom to walk away from relationships and jobs you don't need. You choose because you can."</em></p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Enhanced Community Section ---
st.markdown(
    """
    <div class="card community">
        <h3 class="section-title">🤝 Join Our Community</h3>
        <p style="font-size: 1.1em; line-height: 1.7; color: #2d3748;">Community is the heart of MoneyChicks. You're never alone in your financial journey. We create opportunities for marginalized voices, breaking barriers and catalyzing real change.</p>
        
        <div style="background: rgba(255,255,255,0.8); padding: 2rem; border-radius: 15px; margin: 2rem 0; text-align: center;">
            <h4 style="color: #2e7d32; margin-bottom: 1rem;">💎 Our Philosophy</h4>
            <p style="font-style: italic; font-size: 1.2em; color: #2d3748; margin-bottom: 1rem;">
                "Diamonds will decline, Finances are forever."
            </p>
            <p style="color: #4a5568;">Invest in something that always sticks by your side — <strong>you</strong>.</p>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <h4 style="color: #2e7d32; font-size: 1.5em; margin-bottom: 1rem;">🌟 Impact Statement</h4>
            <div style="background: linear-gradient(135deg, #4caf50, #45a049); color: white; padding: 1.5rem; border-radius: 15px; font-size: 1.3em; font-weight: 600; box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);">
                Empowering one woman, uplifting three generations.
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a class="ig-link" href="https://instagram.com/money.chicks" target="_blank">
                <span class="ig-icon">📸</span>
                Follow @money.chicks on Instagram
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Enhanced Footer ---
st.markdown(
    """
    <div class="footer">
        <h3 style="margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">💜 MoneyChicks</h3>
        <p style="font-size: 1.1em; margin-bottom: 0.5rem;"><strong>Empowering one woman, uplifting three generations.</strong></p>
        <p style="opacity: 0.8; margin: 0;">&copy; 2025 MoneyChicks. Building financial futures together.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
