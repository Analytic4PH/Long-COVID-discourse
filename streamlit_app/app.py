from st_pages import Page, show_pages, add_page_title  # allow multipages
import streamlit as st
import os, sys
from glob import glob

# ================================  add paths ================================ 
parent_dir = os.path.dirname( os.path.realpath(__file__) )
gparent_dir = os.path.dirname( parent_dir )

st.text( parent_dir  )
st.text( gparent_dir )
sys.path.append( gparent_dir )
sys.path.append( parent_dir  )

path_to_html = gparent_dir + '/visualizations/html/yearly_network_graph.html'
with open(path_to_html,'r') as f: 
    html_data = f.read()
    
# ================================  Widget ================================ 
st.header("Project 2")
st.components.v1.html(html_data, scrolling=True, height=500 ) 
 
show_pages(
    [
        Page( parent_dir + "/app.py", "Home", "🏠"),         
        Page( parent_dir + "/other.py", "Other results"),         
    ] 
)
