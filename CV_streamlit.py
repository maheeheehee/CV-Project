import streamlit as st

# Custom CSS with traffic-inspired theme
def set_custom_style():
    st.markdown("""
    <style>
    /* Traffic-inspired color palette and design */
    .stApp {
        background-color: #f0f4f8;
        font-family: 'Arial', sans-serif;
    }
    
    /* Road-inspired title style */
    .title {
        color: #1a5f7a;
        text-align: center;
        font-weight: bold;
        margin-bottom: 30px;
        font-size: 2.5em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* File uploader styled like a road sign */
    .stFileUploader {
        background-color: #e6f2ff;
        border: 3px solid #2c7bb6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Sidebar like a traffic control panel */
    .css-1aumxhk {
        background-color: #d9edf7;
        border: 2px solid #337ab7;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Buttons styled like traffic signals */
    .stButton>button {
        background-color: #28a745;  /* Green for go */
        color: white;
        border-radius: 8px;
        border: 2px solid #218838;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #218838;
        transform: scale(1.05);
    }
    
    /* Info message like a road warning */
    .stAlert {
        border-radius: 8px;
        background-color: #fff3cd;
        border: 2px solid #ffc107;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Apply custom styling
    set_custom_style()
    
    # Traffic-themed title
    st.markdown('<h1 class="title">🚦 Traffic Surveillance</h1>', unsafe_allow_html=True)
    
    # Video upload with traffic-inspired styling
    st.markdown("### 📹 Upload Traffic Video")
    uploaded_file = st.file_uploader(
        "Choose a video file", 
        type=['mp4', 'avi', 'mov'], 
        help="Upload a traffic surveillance video"
    )
    
    # Sidebar header
    st.sidebar.header("🛣️ Options")
    
    # Process video when uploaded
    if uploaded_file is not None:
        # Create two columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 🎥 Uploaded Video")
            st.video(uploaded_file)
        
        with col2:
            st.markdown("### 📋 Video Details")
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"File Size: {uploaded_file.size} bytes")
        
        # Detection button with traffic signal styling
        if st.button("🚨 Start Detection"):
            st.info("🚧 Detection functionality will be implemented soon")

if __name__ == "__main__":
    main()
