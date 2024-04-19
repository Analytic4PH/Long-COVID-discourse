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
 

# ================================ Widget =============================== 
st.header("Other results")

files = glob( gparent_dir + '/visualizations/html/*.html' )

html_datasets, pages = [], []

for i,file in enumerate( files ):
  with open(file,'r') as f: 
    html_data = f.read()
  st.components.v1.html(html_data, scrolling=True, height=500 ) 
  #html_datasets.append( html_data ) 
  
  
