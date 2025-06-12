import streamlit as st
from utils.content_data import get_all_content

st.set_page_config(
    page_title="Search Topics - Stock Market Academy",
    page_icon="🔍",
    layout="wide"
)

# Initialize bookmarks
if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def add_to_bookmarks(title, content):
    bookmark = {"title": title, "content": content, "page": "Search Results"}
    if bookmark not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(bookmark)
        st.success("Added to bookmarks! ⭐")
    else:
        st.info("Already in bookmarks!")

def search_content(query, content_data):
    """Search through all content and return matching results"""
    results = []
    query_lower = query.lower()
    
    for item in content_data:
        # Search in title
        if query_lower in item['title'].lower():
            results.append({
                **item,
                'match_type': 'title',
                'relevance': 3
            })
        # Search in content
        elif query_lower in item['content'].lower():
            results.append({
                **item,
                'match_type': 'content', 
                'relevance': 2
            })
        # Search in keywords
        elif any(query_lower in keyword.lower() for keyword in item.get('keywords', [])):
            results.append({
                **item,
                'match_type': 'keyword',
                'relevance': 1
            })
    
    # Sort by relevance (higher first)
    results.sort(key=lambda x: x['relevance'], reverse=True)
    return results

def display_search_result(result):
    """Display a single search result"""
    with st.container():
        st.markdown(f"### 📍 {result['title']}")
        st.markdown(f"**📄 From:** {result['page']}")
        
        # Show a preview of the content
        content_preview = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
        st.markdown(f"**Preview:** {content_preview}")
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button(f"⭐ Bookmark", key=f"bookmark_{result['title']}"):
                add_to_bookmarks(result['title'], result['content'])
        
        with col2:
            page_mapping = {
                "What is a Stock": "pages/1_📈_What_is_a_Stock.py",
                "Why Companies Go Public": "pages/2_🏢_Why_Companies_Go_Public.py", 
                "Where to Buy Stocks": "pages/3_🛒_Where_to_Buy_Stocks.py",
                "Stock Exchanges": "pages/4_📊_Stock_Exchanges.py",
                "Stock Pricing": "pages/5_💰_Stock_Pricing.py",
                "Market Analogies": "pages/6_☕_Market_Analogies.py",
                "Market Indices": "pages/7_📋_Market_Indices.py"
            }
            
            if result['page'] in page_mapping:
                if st.button(f"📖 Go to Page", key=f"goto_{result['title']}"):
                    st.switch_page(page_mapping[result['page']])
        
        st.markdown("---")

def main():
    st.title("🔍 Search Learning Topics")
    st.markdown("### *Find Exactly What You're Looking For*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Back to Home"):
            st.switch_page("app.py")
    with col3:
        if st.button("View Bookmarks →"):
            st.switch_page("pages/9_⭐_Bookmarks.py")
    
    st.markdown("---")
    
    # Search interface
    st.markdown("## 🔎 Search Our Learning Content")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Enter your search term:",
            placeholder="e.g., stock price, IPO, index, supply demand, analogy...",
            help="Search through all our educational content"
        )
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    # Popular search suggestions
    st.markdown("### 💡 Popular Search Terms")
    
    popular_terms = [
        "stock definition", "IPO", "supply demand", "market index", 
        "coffee matcha", "beauty basket", "ETF", "volatility",
        "primary market", "secondary market", "NYSE", "Nifty 50"
    ]
    
    # Create clickable buttons for popular terms
    cols = st.columns(4)
    for i, term in enumerate(popular_terms):
        with cols[i % 4]:
            if st.button(f"🔖 {term}", key=f"popular_{i}"):
                search_query = term
                search_button = True
    
    # Perform search
    if search_query and (search_button or True):  # Auto-search as user types
        st.markdown("---")
        st.markdown(f"## 📋 Search Results for: *'{search_query}'*")
        
        # Get all content
        all_content = get_all_content()
        
        # Search through content
        results = search_content(search_query, all_content)
        
        if results:
            st.success(f"Found {len(results)} result(s)")
            
            # Display results
            for i, result in enumerate(results):
                display_search_result(result)
                
        else:
            st.warning("No results found. Try different search terms or browse our topics:")
            
            # Suggest browsing options
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                ### 📚 **Browse by Topic:**
                - Stock Basics
                - Company IPOs  
                - Market Mechanics
                - Pricing Factors
                """)
                
                if st.button("📈 Start with Stock Basics"):
                    st.switch_page("pages/1_📈_What_is_a_Stock.py")
            
            with col2:
                st.markdown("""
                ### 🎭 **Browse by Analogy:**
                - Coffee vs Matcha
                - Beauty Basket
                - Mall Shopping
                - Classroom Average
                """)
                
                if st.button("☕ View Fun Analogies"):
                    st.switch_page("pages/6_☕_Market_Analogies.py")
    
    # Quick access section
    st.markdown("---")
    st.markdown("## ⚡ Quick Access")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔰 **Beginner Topics**")
        beginner_topics = [
            ("What is a Stock?", "pages/1_📈_What_is_a_Stock.py"),
            ("Why Go Public?", "pages/2_🏢_Why_Companies_Go_Public.py"),
            ("Where to Buy?", "pages/3_🛒_Where_to_Buy_Stocks.py")
        ]
        
        for title, page in beginner_topics:
            if st.button(title, key=f"beginner_{title}"):
                st.switch_page(page)
    
    with col2:
        st.markdown("### 📊 **Intermediate Topics**")
        intermediate_topics = [
            ("Stock Exchanges", "pages/4_📊_Stock_Exchanges.py"),
            ("Stock Pricing", "pages/5_💰_Stock_Pricing.py"),
            ("Market Indices", "pages/7_📋_Market_Indices.py")
        ]
        
        for title, page in intermediate_topics:
            if st.button(title, key=f"intermediate_{title}"):
                st.switch_page(page)
    
    with col3:
        st.markdown("### 🎭 **Fun Learning**")
        fun_topics = [
            ("Market Analogies", "pages/6_☕_Market_Analogies.py"),
            ("My Bookmarks", "pages/9_⭐_Bookmarks.py")
        ]
        
        for title, page in fun_topics:
            if st.button(title, key=f"fun_{title}"):
                st.switch_page(page)
    
    # Search tips
    st.markdown("---")
    with st.expander("💡 **Search Tips**"):
        st.markdown("""
        ### 🎯 **How to Search Effectively:**
        
        **📝 Try These Search Types:**
        - **Concepts**: "supply demand", "market index", "volatility"
        - **Companies**: "Apple", "Microsoft", "Reliance" 
        - **Analogies**: "coffee", "beauty basket", "seesaw"
        - **Market Terms**: "IPO", "ETF", "NYSE", "Nifty"
        
        **🔍 Search Tips:**
        - Use simple, specific terms
        - Try both full terms and abbreviations  
        - Search for analogies if concepts seem complex
        - Browse popular terms for inspiration
        
        **📚 Can't Find What You Need?**
        - Start with basic topics and build up
        - Use the quick access sections
        - Check your bookmarks for saved content
        - Browse by learning level (beginner → intermediate)
        """)
    
    # Recent searches (if we want to implement this)
    if 'recent_searches' not in st.session_state:
        st.session_state.recent_searches = []
    
    # Add current search to recent searches
    if search_query and search_query not in st.session_state.recent_searches:
        st.session_state.recent_searches.insert(0, search_query)
        st.session_state.recent_searches = st.session_state.recent_searches[:5]  # Keep last 5
    
    if st.session_state.recent_searches:
        st.markdown("---")
        st.markdown("### 🕒 Recent Searches")
        
        cols = st.columns(len(st.session_state.recent_searches))
        for i, recent_query in enumerate(st.session_state.recent_searches):
            with cols[i]:
                if st.button(f"🔄 {recent_query}", key=f"recent_{i}"):
                    search_query = recent_query
                    st.rerun()

if __name__ == "__main__":
    main()
