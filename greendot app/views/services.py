import streamlit as st

st.title('Products & Services')


# Define categories and products
categories = {
    'ECG Papers': [
        'Brands and Paper Types'
    ],
    'Neonatal Equipment': [
        'Incubators', 'Phototherapy', 'Defibrillator', 'Respiratory Equipment', 'Resuscitation Equipment'
    ],
    'Patient Monitoring Systems': [
        'CCU, ICU Patient Monitors', 'Vital Sign Monitors', 'Central Station', 'Fetal Monitors', 'Oximeters', 'ECG', 'EEG & EMG Machines'
    ],
    'Medical Imaging': [
        'Ultrasound Machines', 'X-Ray'
    ],
    'Cardiac Systems': [
        'CardioTest', 'Stress Test', 'Holter', 'CardioSuite', 'CardioDatabase'
    ],
    'Ventilators and Respiratory Systems': [
        'Critical Care Ventilators', 'CPAP', 'BIPAP', 'Anesthesia Machines', 'Other Respiratory Systems'
    ],
    'Surgical Equipment': [
        'Surgical Drapes & Sets', 'Surgical Gowns', 'Disposable Medical Plastics'
    ],
    'Radiation Protection': [
        'Lead Apron', 'Gonadal Protection', 'Patient Radiation Protection', 'Lead Gloves', 'Radiation Protection Goggles'
    ],
    'Lab Equipment': [
        'Centrifuges', 'Microscopes', 'Blood Collection Monitor', 'Donor Lounge', 'Thrombocyte Incubator'
    ],
    'Hospital Furniture': [
        'Hospital Beds', 'Ward Furniture', 'Hospital Cart and Stands', 'Baby Furniture'
    ]
}

papers = {
    'Mortara' : {'ELI 100/150' : 'Size: 108 * 140 * 200  -  Description: QuickTrace-HS80 ', 'ELI 210/250' : 'Size: 210 * 300 * 250   Description: QuickTrace-HS75 '},
    'Nihon Kohden' : {'TEC' : 'Size: 50 * 100 * 300    Description: QuickTrace-HS ', 'ECG 9010/9020' : 'Size: 110 * 140 * 150   Description: QuickTrace-HS ', 'ECG 9110/9130' : 'Size: 210 * 140 * 200   Description: QuickTrace-HS ', 'ECG 9320 K' : 'Size: 210 * 295 * 250   Description: QuickTrace-HS '},
    'HP/PHILIPS' : {'M1350 A/ M1351 A' : 'Size: 150 * 100 * 150    Description: QuickTrace-HS ', 'M-1700/1701 A' : 'Size: 210 * 300 * 200   Description: QuickTrace-HS75 '},
    'SONY' : {'UPP110S' : 'Size: 110 * 20    Description: Plastic-S ', 'UPP110HD' : 'Size: 110 * 20   Description: Plastic-HD ', 'UPP110HG' : 'Size: 110 * 20   Description: Plastic-HG '},
    'CARDIOLINE' : {'DELTA - 1 PLUS' : 'Size: 60 * 30    Description: QuickTrace-HS ', 'DELTS - 60 PLUS' : 'Size: 210 * 30   Description: QuickTrace-HS ', 'DELTA - 3 PLUS' : 'Size: 112 * 100 * 300   Description: QuickTrace-HS '},
    'FUKUDA' : {'OP-110 TE' : 'Size: 63 * 30 ', 'SP200' : 'Size: 58 * 25 ', 'DENSHI OP-12 KE' : 'Size: 50 * 30    Description: QuickTrace-HS'},
    'HELLIGE - MARQUETTE' : {'MICROSMART' : 'Size: 90 * 35    Description: QuickTrace-HS', 'CARDISMART' : 'Size: 210 * 295 * 150     Description: QuickTrace-HS '},
    'SCHILLER' : {'AT - 101' : 'Size: 80 * 70 * 300    Description: QuickTrace-HS75', 'AT - 1' : 'Size: 90 * 90 * 400     Description: QuickTrace-HS '},
    'SONICAID' : {'MERDIAN500' : 'Size: 142 * 150 * 300'},
    'COROMETRICS' : {'SERIES:115/116/118/120/150' : 'Size: 152 * 90 * 150   Description: QuickTrace-HS'},
    'BISTOS' : {'BT- 300/330/350' : 'Size: 130 * 120 * 250'},
    'CARDIETTE' : {'AR-600 ADV / 66010037 / DOT-CARD / BLUE GRID' : 'Size: 60 * 15 Sensor'},
    'ESAOTE' : {'P80/ SECA' : 'Size: 90 * 70 * 400'},


}

# Function to display product descriptions
def display_product_details(category):
    if category == 'ECG Papers':
        st.subheader('ECG Papers')
        brand = st.selectbox('Select a Brand', papers.keys())
        paper_type = st.selectbox('Select Paper Type / Model', list(papers[brand]))
        st.write(f"Brand: {brand}")
        st.write(f"Paper Type:\t {papers[brand][paper_type]}")
        # Add more details related to selected brand and type if needed
    else:
        st.write(f"Here are our services under the category **{category}**:")
        for product in categories[category]:
            st.write(f"- {product}")  # Modify this to include actual descriptions



category = st.selectbox('Select a Category', list(categories.keys()))

display_product_details(category)

if st.button("💲 Pricing"):
        st.write("We have the best Wholesale and retail prices! Contact us at ahusseini@greendotsite.com")
