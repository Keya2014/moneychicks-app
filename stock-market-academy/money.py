import streamlit as st
import pandas as pd
import numpy as np

# --- Reduce white space on top and under graph title ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    .section-title {
        margin-bottom: 0.3rem !important;
        margin-top: 1.2em !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Custom CSS: Pastel outlines, no backgrounds, no outline for calculator ---
st.markdown(
    """
    <style>
        .big-title { font-size: 2.8em; font-weight: bold; color: #a54cb7; }
        .section-title { font-size: 1.5em; color: #a54cb7; }
        .mission {
            border-radius: 10px;
            padding: 1em;
            border: 2px solid #ffd6f6; /* pastel pink outline */
        }
        .manifesto {
            border-radius: 10px;
            padding: 1em;
            border: 2px solid #c6e6fd; /* pastel blue outline */
        }
        .community {
            border-radius: 10px;
            padding: 1em;
            border: 2px solid #e7ffd6; /* pastel green outline */
        }
        .financial-learning {
            border-radius: 10px;
            padding: 1em;
            border: 2px solid #ffe6c7; /* pastel orange/peach outline */
            margin-bottom: 2em;
        }
        .calculator {
            /* No border, no box-shadow, no background */
            border: none !important;
            box-shadow: none !important;
            background: none !important;
            padding: 0 !important;
        }
        a.ig-link {
            display: inline-flex;
            align-items: center;
            background: linear-gradient(90deg, #f9ce34 0%, #ee2a7b 50%, #6228d7 100%);
            border-radius: 30px;
            padding: 10px 22px;
            font-size: 1.2em;
            font-weight: bold;
            color: white !important;
            box-shadow: 0 2px 8px #eee;
            text-decoration: none;
            transition: box-shadow 0.2s;
            margin-top: 1.2em;
        }
        a.ig-link:hover {
            box-shadow: 0 4px 16px #d1a3e4;
            color: white !important;
        }
        .ig-icon {
            font-size:1.5em; margin-right: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="big-title">💜 Welcome to MoneyChicks</div>', unsafe_allow_html=True)
st.write("We’re a financial community that helps you learn how to take control of your money, and do it well.")

st.markdown(
    """
    <div class="mission">
        <h3 class="section-title">🌟 Mission Statement</h3>
        <p>Our mission is to simplify money and close the gender gap in investing.</p>
        <p><i>MoneyChicks was born as a reaction to the intimidating world of stock markets from an 18-year-old teenager’s perspective. We wish to demystify, un-mansplain and foster inclusive conversation that helps women understand from scratch, without feeling stupid.</i></p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="manifesto">
        <h3 class="section-title">🚀 Manifesto</h3>
        <p>For the ones who’ve been left out of the narrative. For the ones that want to contradict conversations that don’t expect them. We’re the community for those who wish to challenge the tides of power, to take charge of what’s theirs. To be able to be aware, grow and leverage their finances. The way that you like. Unconventionally.</p>
        <p><b>We’ll start you off to learn from the very beginning, (no, really. Not from stock charts) All you need to be is believe you can.</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">📈 Why you should get started now</div>', unsafe_allow_html=True)
st.write("See for yourself how investing outperforms savings over time!")

# Layout: Sliders on left, graph on right
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="calculator">', unsafe_allow_html=True)
    starting_amount = st.slider("💰 Starting amount (₹)", 0, 1000000, 0, 1000)
    monthly_contribution = st.slider("📅 Monthly contribution (₹)", 0, 200000, 2000, 500)
    years = st.slider("⏳ Time horizon (years)", 1, 40, 20, 1)
    st.markdown('</div>', unsafe_allow_html=True)

# Investment calculation logic
annual_return = 0.08  # 8% global average as per Female Invest
months = years * 12

contributions = []
returns = []
total = starting_amount
for month in range(months):
    total += monthly_contribution
    total *= (1 + annual_return / 12)
    contributions.append(starting_amount + monthly_contribution * (month + 1))
    returns.append(total - contributions[-1])

years_list = [2025 + i for i in range(years)]
contribs_by_year = [starting_amount + monthly_contribution * (12 * (i + 1)) for i in range(years)]
returns_by_year = []
total_by_year = starting_amount
for i in range(years):
    for _ in range(12):
        total_by_year += monthly_contribution
        total_by_year *= (1 + annual_return / 12)
    returns_by_year.append(total_by_year - contribs_by_year[i])

df = pd.DataFrame({
    "Year": years_list,
    "Contributions": contribs_by_year,
    "Returns": returns_by_year
})

with col2:
    st.metric("Total if Invested", f"₹{(df['Contributions'].iloc[-1] + df['Returns'].iloc[-1]):,.0f}")
    st.metric("Total if Not Invested", f"₹{starting_amount + monthly_contribution * months:,.0f}")
    st.bar_chart(df.set_index("Year"))
    st.caption("This calculator is for illustrative purposes only and does not constitute financial advice.")

# --- Collapsible "Understanding the Formula" Section above Financial Learning ---
with st.expander("📚 Understanding the Formula"):
    st.write(
        """
        The compound interest formula is used to find the total principal plus accrued interest. 
        It can also solve for principal, rate, or time given the other known values. 
        You can use this equation to set up a compound interest calculator in Excel or other tools.

        **Compound Interest Formula:**

            A = P(1 + r/n)^(nt)

        Where:

        - **A** = Final amount (principal + accrued interest)
        - **P** = Principal starting amount
        - **r** = Annual nominal interest rate as a decimal
        - **R** = Annual nominal interest rate as a percent (r = R/100)
        - **n** = Number of compounding periods per unit of time
        - **t** = Time in decimal years (e.g., 6 months = 0.5 years; months/12)

        **Notes:**
        - Use the Annual Percentage Rate (APR) as the nominal interest rate r.
        - This formula does **not** account for fees or additional costs associated with loans or investments.

        **APR (Annualised Percentage Rate):** Used for loans to show the base cost of borrowing.

        **EAR (Effective Annual Rate):** Useful for understanding the actual return, but less common in bank rates for loans.
        """
    ) 
# --- Financial Learning Section with pastel outline ---
st.markdown(
    """
    <div class="financial-learning">
        <div class="section-title">🎓 Financial Learning</div>
        Financial Learning is the foundation of women empowerment. We’ve made it our mission to give you an unparalleled learning ground. Where all questions are safe, because when those are out in the open, that’s when you give your future a chance to be safe.Financial Literacy gives you the freedom to walk out on relationships and jobs that you don’t need. You choose because you can.

    </div>
    """,
    unsafe_allow_html=True,
)

# --- Community section ---
st.markdown(
    """
    <div class="community">
        <h3 class="section-title">🤝 Community</h3>
        <p>Community is the most important part of MoneyChicks. So you know that you’re anything but alone. We help create choice for marginalised voices, breaking barriers and creating a movement. Becoming a catalyst to real change, breaking long-standing generational inequity, one chick at a time.</p>
        <p><i>Diamonds will decline, Finances are forever.</i> Invest in something that always sticks by your side-you.</p>
        <p><b>Empowering one woman, uplifting three generations.</b></p>
        <a class="ig-link" href="https://instagram.com/money.chicks" target="_blank">
            <span class="ig-icon">📸</span>
            Follow us on <span style="margin-left: 6px; font-family: 'Segoe UI', 'Arial', sans-serif;">@money.chicks</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    ---
    <center>
        <b>MoneyChicks &copy; 2025 | Empowering one woman, uplifting three generations.</b>
    </center>
    """,
    unsafe_allow_html=True,
)
