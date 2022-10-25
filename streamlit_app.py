import streamlit as st
from streamlit import config

st.write("fastReruns: ", config.get_option("runner.fastReruns"))
