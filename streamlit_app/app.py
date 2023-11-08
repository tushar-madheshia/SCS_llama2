import streamlit as st

st.set_page_config(page_title="Refract",layout="wide", page_icon="")
st.header("Demand Forecasting")
st.write("Demand forecasting is, in essence, developing the best possible understanding of future demand.")
with st.sidebar:
    from PIL import Image
    image = Image.open('streamlit_app/ref1.png')

    st.image(image)
    st.sidebar.header("Criteria")

    brand =  st.selectbox("Select Brand", ['None','Optic','Daffodils','Spectra','Carnations','Turkestan ','Red Cross ','Hybrid Tea ','Sage','Aspect','Refract','Helenium','Magnolia','Goldenrod','Morning Glory','Lavender','Flaming Katy','Golden-rayed'], index=1,key=0, help='Select the brand name')
    print("Selected Brand : "+ brand)
    if(brand != 'None'):
        retailer =  st.selectbox("Select Retailer",['None','Retailer1','Retailer2','Retailer3','Retailer4','Retailer5'], index= 1,key=1, help='Select the Retailer')
        print("Selected retailer : "+ retailer)

