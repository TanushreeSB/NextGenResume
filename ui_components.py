import streamlit as st

def apply_modern_styles():
    """Apply modern styles to the Streamlit app."""
    st.markdown("""
        <style>
        /* Add your custom CSS styles here */
        .main-header {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            text-align: center;
        }
        .main-header h1 {
            color: white;
            font-size: 2.5rem;
            font-weight: 600;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)

def hero_section(title, subtitle):
    """Render a hero section with a title and subtitle."""
    st.markdown(f"""
        <div class="main-header">
            <h1>{title}</h1>
            <p style="color: white; font-size: 1.2rem;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

def feature_card(icon, title, description):
    """Render a feature card with an icon, title, and description."""
    st.markdown(f"""
        <div style="background: rgba(45, 45, 45, 0.9); border-radius: 20px; padding: 2rem; margin: 1rem 0;">
            <i class="{icon}" style="font-size: 2.5rem; color: #4CAF50;"></i>
            <h3 style="color: white; margin: 1rem 0;">{title}</h3>
            <p style="color: #ddd;">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def page_header(title, subtitle):
    """Render a page header with a title and subtitle."""
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: white;">{title}</h1>
            <p style="color: #ddd;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

def render_analytics_section():
    """Render the analytics section."""
    st.markdown("""
        <div style="background: rgba(45, 45, 45, 0.9); border-radius: 20px; padding: 2rem; margin: 1rem 0;">
            <h2 style="color: white;">Analytics</h2>
            <p style="color: #ddd;">Your analytics data will appear here.</p>
        </div>
    """, unsafe_allow_html=True)

def render_activity_section():
    """Render the activity section."""
    st.markdown("""
        <div style="background: rgba(45, 45, 45, 0.9); border-radius: 20px; padding: 2rem; margin: 1rem 0;">
            <h2 style="color: white;">Activity</h2>
            <p style="color: #ddd;">Your activity data will appear here.</p>
        </div>
    """, unsafe_allow_html=True)

def render_suggestions_section():
    """Render the suggestions section."""
    st.markdown("""
        <div style="background: rgba(45, 45, 45, 0.9); border-radius: 20px; padding: 2rem; margin: 1rem 0;">
            <h2 style="color: white;">Suggestions</h2>
            <p style="color: #ddd;">Your suggestions will appear here.</p>
        </div>
    """, unsafe_allow_html=True)