import streamlit as st
import cv2
import numpy as np
import tempfile
import os

def extract_frames(video_path, max_frames=10):
    """
    Extract frames from the uploaded video
    
    Args:
    video_path (str): Path to the uploaded video
    max_frames (int): Maximum number of frames to extract
    
    Returns:
    list: Extracted frames as numpy arrays
    """
    frames = []
    try:
        cap = cv2.VideoCapture(video_path)
        
        # Get total number of frames
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Calculate frame interval
        frame_interval = max(1, total_frames // max_frames)
        
        for frame_num in range(0, total_frames, frame_interval):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()
            
            if ret:
                # Convert BGR to RGB for Streamlit display
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frames.append(frame_rgb)
                
                # Stop if we've reached max_frames
                if len(frames) >= max_frames:
                    break
        
        cap.release()
    except Exception as e:
        st.error(f"Error extracting frames: {e}")
    
    return frames

def main():
    # Page configuration
    st.set_page_config(page_title="Traffic Surveillance", page_icon=":camera:")
    
    # Title and description
    st.title("Traffic Surveillance System")
    st.write("Upload a traffic surveillance video for analysis")
    
    # Sidebar for configuration
    st.sidebar.header("Video Processing Options")
    
    # Video upload
    uploaded_file = st.file_uploader(
        "Choose a video file", 
        type=['mp4', 'avi', 'mov'], 
        help="Upload a traffic surveillance video"
    )
    
    # Sidebar options
    with st.sidebar:
        max_frames = st.slider(
            "Maximum frames to extract", 
            min_value=5, 
            max_value=50, 
            value=10, 
            help="Number of frames to extract from the video"
        )
        
        detection_confidence = st.slider(
            "Detection Confidence Threshold", 
            min_value=0.1, 
            max_value=1.0, 
            value=0.5, 
            step=0.1,
            help="Minimum confidence for object detection"
        )
    
    # Process video when file is uploaded
    if uploaded_file is not None:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tfile:
            tfile.write(uploaded_file.read())
        
        try:
            # Extract frames
            st.write("Extracting frames...")
            frames = extract_frames(tfile.name, max_frames=max_frames)
            
            # Display extracted frame count
            st.success(f"Extracted {len(frames)} frames")
            
            # Display frames in a grid
            st.subheader("Extracted Frames")
            cols = st.columns(min(5, len(frames)))
            
            for i, col in enumerate(cols):
                with col:
                    st.image(frames[i], caption=f'Frame {i+1}')
            
            # Additional processing section
            st.subheader("Detection Options")
            col1, col2 = st.columns(2)
            
            with col1:
                helmet_detection = st.checkbox("Detect Helmets", value=True)
            
            with col2:
                license_plate_detection = st.checkbox("Detect License Plates", value=True)
            
            # Placeholder for detection button
            if st.button("Start Detection"):
                st.info("Detection functionality will be implemented soon!")
        
        except Exception as e:
            st.error(f"Error processing video: {e}")
        
        finally:
            # Clean up temporary file
            os.unlink(tfile.name)

if __name__ == "__main__":
    main()