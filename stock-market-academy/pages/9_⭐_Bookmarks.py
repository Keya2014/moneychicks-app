import streamlit as st

st.set_page_config(
    page_title="My Bookmarks - Stock Market Academy",
    page_icon="⭐",
    layout="wide"
)

# Initialize bookmarks
if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

def remove_bookmark(index):
    """Remove a bookmark by index"""
    if 0 <= index < len(st.session_state.bookmarks):
        removed = st.session_state.bookmarks.pop(index)
        st.success(f"Removed '{removed['title']}' from bookmarks")
        st.rerun()

def clear_all_bookmarks():
    """Clear all bookmarks"""
    st.session_state.bookmarks = []
    st.success("All bookmarks cleared!")
    st.rerun()

def main():
    st.title("⭐ My Bookmarks")
    st.markdown("### *Your Saved Learning Content*")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Back to Search"):
            st.switch_page("pages/8_🔍_Search_Topics.py")
    with col3:
        if st.button("🏠 Home"):
            st.switch_page("app.py")
    
    st.markdown("---")
    
    # Bookmarks summary
    if st.session_state.bookmarks:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.info(f"📚 You have {len(st.session_state.bookmarks)} saved items")
        
        with col2:
            if st.button("🗑️ Clear All Bookmarks", type="secondary"):
                if st.session_state.get('confirm_clear', False):
                    clear_all_bookmarks()
                    st.session_state.confirm_clear = False
                else:
                    st.session_state.confirm_clear = True
                    st.warning("Click again to confirm clearing all bookmarks")
                    st.rerun()
        
        st.markdown("---")
        
        # Display bookmarks
        st.markdown("## 📋 Your Saved Content")
        
        # Group bookmarks by page
        bookmarks_by_page = {}
        for i, bookmark in enumerate(st.session_state.bookmarks):
            page = bookmark.get('page', 'Unknown')
            if page not in bookmarks_by_page:
                bookmarks_by_page[page] = []
            bookmarks_by_page[page].append((i, bookmark))
        
        # Display bookmarks grouped by page
        for page, page_bookmarks in bookmarks_by_page.items():
            with st.expander(f"📄 {page} ({len(page_bookmarks)} items)", expanded=True):
                for bookmark_index, bookmark in page_bookmarks:
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.markdown(f"### 🔖 {bookmark['title']}")
                            
                            # Show content preview
                            content = bookmark.get('content', 'No content available')
                            if len(content) > 300:
                                preview = content[:300] + "..."
                                with st.expander("📖 Preview", expanded=False):
                                    st.markdown(preview)
                                    st.markdown("*Click to see full content...*")
                                    
                                    if st.button(f"📖 Show Full Content", key=f"show_full_{bookmark_index}"):
                                        st.markdown("**Full Content:**")
                                        st.markdown(content)
                            else:
                                st.markdown(f"**Content:** {content}")
                            
                            # Add timestamp if available
                            if 'timestamp' in bookmark:
                                st.caption(f"📅 Saved: {bookmark['timestamp']}")
                        
                        with col2:
                            st.markdown("**Actions:**")
                            
                            # Remove bookmark button
                            if st.button(f"🗑️ Remove", key=f"remove_{bookmark_index}"):
                                remove_bookmark(bookmark_index)
                            
                            # Go to page button (if we can map it)
                            page_mapping = {
                                "What is a Stock": "pages/1_📈_What_is_a_Stock.py",
                                "Why Companies Go Public": "pages/2_🏢_Why_Companies_Go_Public.py", 
                                "Where to Buy Stocks": "pages/3_🛒_Where_to_Buy_Stocks.py",
                                "Stock Exchanges": "pages/4_📊_Stock_Exchanges.py",
                                "Stock Pricing": "pages/5_💰_Stock_Pricing.py",
                                "Market Analogies": "pages/6_☕_Market_Analogies.py",
                                "Market Indices": "pages/7_📋_Market_Indices.py"
                            }
                            
                            if bookmark['page'] in page_mapping:
                                if st.button(f"📖 Go to Page", key=f"goto_{bookmark_index}"):
                                    st.switch_page(page_mapping[bookmark['page']])
                        
                        st.markdown("---")
        
        # Export bookmarks section
        st.markdown("---")
        st.markdown("## 📤 Export Your Bookmarks")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📋 Copy as Text", use_container_width=True):
                export_text = "# My Stock Market Learning Bookmarks\n\n"
                for page, page_bookmarks in bookmarks_by_page.items():
                    export_text += f"## {page}\n\n"
                    for _, bookmark in page_bookmarks:
                        export_text += f"### {bookmark['title']}\n"
                        export_text += f"{bookmark['content']}\n\n"
                
                st.text_area("Copy this text:", export_text, height=200)
        
        with col2:
            # Create a summary of bookmarks
            summary = f"""
            **Your Learning Summary:**
            
            📊 Total Bookmarks: {len(st.session_state.bookmarks)}
            📚 Pages Covered: {len(bookmarks_by_page)}
            
            **Topics You've Saved:**
            """
            
            for page, page_bookmarks in bookmarks_by_page.items():
                summary += f"\n• {page}: {len(page_bookmarks)} items"
            
            st.markdown(summary)
    
    else:
        # Empty state
        st.markdown("""
        ## 📭 No Bookmarks Yet
        
        You haven't saved any content yet! Bookmarks help you:
        
        - 💾 **Save Important Concepts** for quick reference
        - 📚 **Build Your Personal Study Guide** 
        - 🎯 **Track Key Learning Points**
        - 🔄 **Easily Review Complex Topics**
        
        ### 🚀 How to Add Bookmarks:
        
        1. **Browse Learning Pages** - Visit any topic page
        2. **Look for ⭐ Buttons** - Found throughout the content
        3. **Click to Save** - Add important concepts to your bookmarks
        4. **Return Here** - Access all your saved content anytime
        """)
        
        # Quick links to start learning
        st.markdown("---")
        st.markdown("### 🎯 Start Learning and Bookmark Content:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📈 Stock Basics", use_container_width=True):
                st.switch_page("pages/1_📈_What_is_a_Stock.py")
        
        with col2:
            if st.button("☕ Fun Analogies", use_container_width=True):
                st.switch_page("pages/6_☕_Market_Analogies.py")
        
        with col3:
            if st.button("🔍 Search Topics", use_container_width=True):
                st.switch_page("pages/8_🔍_Search_Topics.py")
        
        # Example of what bookmarks look like
        with st.expander("👀 **Preview: What Bookmarks Look Like**"):
            st.markdown("""
            Here's what your bookmarks will look like once you start saving content:
            
            **📄 Stock Basics**
            🔖 **Stock Definition**
            *Content: A stock represents partial ownership in a company...*
            
            **📄 Market Analogies** 
            🔖 **Coffee vs Matcha Analogy**
            *Content: Coffee represents blue-chip stocks while matcha...*
            
            **📄 Market Indices**
            🔖 **Beauty Basket Explanation**
            *Content: Market indices work like tracking a basket of beauty products...*
            """)
    
    # Learning statistics
    st.markdown("---")
    if st.session_state.bookmarks:
        st.markdown("## 📊 Your Learning Stats")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Bookmarks", len(st.session_state.bookmarks))
        
        with col2:
            st.metric("Pages Covered", len(bookmarks_by_page))
        
        with col3:
            # Calculate most bookmarked page
            if bookmarks_by_page:
                most_bookmarked = max(bookmarks_by_page.items(), key=lambda x: len(x[1]))
                st.metric("Favorite Topic", f"{most_bookmarked[0]}")
        
        with col4:
            # Show learning progress indication
            total_possible_pages = 7  # Number of main learning pages
            coverage = min(100, (len(bookmarks_by_page) / total_possible_pages) * 100)
            st.metric("Topic Coverage", f"{coverage:.0f}%")
    
    # Tips section
    st.markdown("---")
    with st.expander("💡 **Bookmark Tips & Tricks**"):
        st.markdown("""
        ### 🎯 **Getting the Most from Bookmarks:**
        
        **📚 Study Strategy:**
        - Bookmark key definitions and concepts
        - Save analogies that help you understand complex topics
        - Mark important takeaways from each section
        - Keep track of topics you want to review later
        
        **🔄 Review Process:**
        - Visit your bookmarks regularly to reinforce learning
        - Use bookmarks to create your own study guide
        - Review saved analogies when concepts seem confusing
        - Export bookmarks as text for offline studying
        
        **🗂️ Organization Tips:**
        - Bookmarks are automatically grouped by page
        - Use the search function to find specific saved content
        - Clear outdated bookmarks to keep your collection relevant
        - Focus on saving actionable insights, not just definitions
        
        **📈 Track Your Progress:**
        - More bookmarks = more engagement with learning content
        - Diverse page coverage = well-rounded understanding
        - Regular bookmark reviews = better retention
        """)
    
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
        if len(st.session_state.bookmarks) == 0:
            if st.button("📈 Start Learning", use_container_width=True):
                st.switch_page("pages/1_📈_What_is_a_Stock.py")
        else:
            # Show link to least bookmarked topic to encourage exploration
            if st.button("📚 Explore More", use_container_width=True):
                st.switch_page("pages/1_📈_What_is_a_Stock.py")

if __name__ == "__main__":
    main()
