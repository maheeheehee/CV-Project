import streamlit as st

# Custom CSS for improved aesthetics
def set_custom_style():
    st.markdown("""
    <style>
    /* Custom background and theme */
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Stylish title */
    .title {
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 30px;
        font-size: 2.5em;
    }
    
    /* Enhanced file uploader */
    .stFileUploader {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Sidebar styling */
    .css-1aumxhk {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
    
    /* Info message styling */
    .stAlert {
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Apply custom styling
    set_custom_style()
    
    # Add a more descriptive title with custom class
    st.markdown('<h1 class="title">🚦 Traffic Surveillance System</h1>', unsafe_allow_html=True)
    
    # Video upload with enhanced styling
    st.markdown("### Upload Traffic Video")
    uploaded_file = st.file_uploader(
        "Choose a video file", 
        type=['mp4', 'avi', 'mov'], 
        help="Upload a traffic surveillance video"
    )
    
    # Sidebar for options
    st.sidebar.header("📋 System Options")
    
    # Optional: Add some explanatory text to sidebar
    st.sidebar.markdown("""
    ### About the System
    This advanced traffic surveillance tool helps monitor and analyze 
    traffic-related activities using intelligent video processing.
    """)
    
    # Commented out detection options as requested
    # helmet_detection = st.sidebar.checkbox("Detect Helmets", value=True)
    # license_plate_detection = st.sidebar.checkbox("Detect License Plates", value=True)
    
    # Process video when uploaded
    if uploaded_file is not None:
        # Create two columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Uploaded Video")
            st.video(uploaded_file)
        
        with col2:
            st.markdown("### Video Details")
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"File Size: {uploaded_file.size} bytes")
        
        # Detection button with more prominent styling
        if st.button("🔍 Start Detection"):
            st.info("🚧 Detection functionality will be implemented soon")
            
            # Placeholder for detection results (commented out)
            # if helmet_detection:
            #     st.write("Helmet Detection: Pending")
            
            # if license_plate_detection:
            #     st.write("License Plate Detection: Pending")

if __name__ == "__main__":
    main()
