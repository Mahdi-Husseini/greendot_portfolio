import streamlit as st
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

st.title('About Us')

st.markdown("""
## Leading Healthcare Innovation

At GreenDot Solutions, we are dedicated to advancing healthcare through cutting-edge software solutions and state-of-the-art biomedical products. With almost two decades of experience, we have established ourselves as a trusted partner in the healthcare technology sector, serving hospitals, clinics, and healthcare institutions.

## Our Mission

We strive to transform healthcare delivery by providing innovative technologies that enhance patient care, streamline clinical workflows, and improve healthcare outcomes. Our commitment to excellence drives us to develop solutions that meet the evolving needs of modern healthcare facilities.

## Industry Leadership

Our strategic partnerships with global technology leaders enable us to deliver comprehensive healthcare solutions that integrate seamlessly with existing systems. We are proud to collaborate with:

""")

# Image carousel for partner logos
image_urls = [
    os.path.join(current_dir, "images", "dms.jpg"),
    os.path.join(current_dir, "images", "cisco.png"),
    os.path.join(current_dir, "images", "microsoft.png"),
    os.path.join(current_dir, "images", "teletrade.jpeg"),
    os.path.join(current_dir, "images", "dell.png"),
    os.path.join(current_dir, "images", "HP.png"),
    os.path.join(current_dir, "images", "ibm.jpg"),
    os.path.join(current_dir, "images", "GFI.jpg"),
    os.path.join(current_dir, "images", "3com.jpg"),
    os.path.join(current_dir, "images", "medicate.png"),
    os.path.join(current_dir, "images", "sibelmed.png"),
    os.path.join(current_dir, "images", "chison.png"),
]

if "image_index" not in st.session_state:
    st.session_state.image_index = 0

# Display the current image
current_image = image_urls[st.session_state.image_index]
st.image(current_image, width=400)

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("◀️ Previous"):
        st.session_state.image_index = (st.session_state.image_index - 1) % len(image_urls)
with col3:
    if st.button("Next ▶️"):
        st.session_state.image_index = (st.session_state.image_index + 1) % len(image_urls)

st.markdown("""
## Our Expertise

### Healthcare Software Solutions
- Electronic Health Records (EHR) Systems
- Hospital Management Software
- Clinical Decision Support Systems
- Medical Imaging Solutions
- Telemedicine Platforms
- Healthcare Analytics Tools

### Biomedical Products
- Advanced Diagnostic Equipment
- Patient Monitoring Systems
- Medical Imaging Devices
- Laboratory Equipment
- Surgical Technologies
- Rehabilitation Equipment

## Quality Assurance

We maintain the highest standards of quality and compliance in all our products and services. Our solutions are:
- FDA-compliant
- ISO 13485:2016 certified
- HIPAA-compliant
- CE-marked for applicable products

## Local Presence

With a strong presence across Lebanon, we serve over 30 healthcare providers. Our local network of support teams ensures reliable service and prompt technical assistance to all our clients.
""")

# Image carousel for partner logos
image_urls2 = [
    os.path.join(current_dir, "images", "sgh.jpg"),
    os.path.join(current_dir, "images", "dar-amal.png"),
    os.path.join(current_dir, "images", "mount-lebanon.png")
]

if "image_index2" not in st.session_state:
    st.session_state.image_index2 = 0

# Display the current image
current_image2 = image_urls2[st.session_state.image_index2]
st.image(current_image2, width=400)

# Navigation buttons
col4, col5, col6 = st.columns([1, 2, 1])
with col4:
    if st.button("◀️"):
        st.session_state.image_index2 = (st.session_state.image_index2 - 1) % len(image_urls2)
with col6:
    if st.button("▶️"):
        st.session_state.image_index2 = (st.session_state.image_index2 + 1) % len(image_urls2)

st.markdown("""
## Innovation & Research

Our dedicated R&D team continuously works on developing innovative solutions that address emerging healthcare challenges. We invest significantly in research and collaborate with leading medical institutions to stay at the forefront of healthcare technology.

## Customer Success

Our commitment extends beyond product delivery. We provide:
- Comprehensive implementation support
- Regular software updates and maintenance
- 24/7 technical support
- Customized training programs
- Ongoing consultation services

## Contact Us

Partner with us to transform your healthcare delivery capabilities. Our team of experts is ready to understand your needs and provide tailored solutions.

""")

# Create two columns for contact buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📞 Schedule a Consultation"):
        st.write("Contact our technical sales manager at ahusseini@greendotsite.com")

with col2:
    if st.button("📧 Technical Support"):
        st.write("Reach our support team at info@greendotsite.com")