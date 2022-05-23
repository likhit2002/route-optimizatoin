import streamlit as st

st.set_page_config(page_title="Route Optimization For Bus Fleet", page_icon=":tada:", layout="wide")

st.subheader("Route Optimization For Bus Fleet")
st.title("Select a name from the given box below")

option = st.selectbox(
     'Who would you like to be contacted?',
     ('Prabhath','Likhit','Tharun', 'Reddy','Chandu','Venkatesh','Sharath','Nandini','Tulasi'))

st.write('You selected:', option)