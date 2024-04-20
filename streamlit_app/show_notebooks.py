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
st.title("Notebooks")

tabs = st.tabs( ['Europe', 'USA', 'Canada'] )

with tabs[0]:
  files = glob( gparent_dir + '/visualizations/notebooks/*.*' )
  html_datasets, pages = [], []
  #st.header( 'Results on tweets from Europe' )
  for i,file in enumerate( files ):
    with open(file,'r') as f: 
      data = f.read()   
    st.write( file )
    st.components.v1.html( data, scrolling=True, height=1000 ) 
 