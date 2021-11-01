import streamlit as st
def calculate_emi(p,n,r):
  emi=p*(r/12)/100*(1+1/100)**n*12/(1+r/100)**n-1
  return emi
st.title("EMI Calculator App")
st.slider("principal",0.0,10000000.0)
st.slider("tenure",0.0,10000.0)
st.slider("roi",0.0,1000000.0)
st.button('Predict',calculate_emi())