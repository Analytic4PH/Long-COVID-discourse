from st_pages import Page, show_pages, add_page_title  # allow multipages
import streamlit as st
import os, sys
from glob import glob

import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ================================  add paths ================================ 
parent_dir = os.path.dirname( os.path.realpath(__file__) )
gparent_dir = os.path.dirname( parent_dir )

st.text( parent_dir  )
st.text( gparent_dir )
sys.path.append( gparent_dir )
sys.path.append( parent_dir  )

st.write( 'This page is only deployed for demo purposes.')

# ================================  Widget ================================ 
path_to_html = gparent_dir + '/visualizations/project2/yearly_network_graph.html'
with open(path_to_html,'r') as f: 
    html_data = f.read()

st.header("Project 2")
st.write( 'Below show rendering of notebooks (which are far from usable)')
components.html(html_data, scrolling=True, height=500 ) 
 
# ================================ Widget =============================== 
st.title("Notebooks")
st.write( 'Below show rendering of notebooks')
if 1:
  files = glob( gparent_dir + '/visualizations/notebooks/*.*' )
  html_datasets, pages = [], []
  #st.header( 'Results on tweets from Europe' )
  for i,file in enumerate( files ):
    with open(file,'r') as f: 
      data = f.read()   
    st.write( file )
    components.html( data, scrolling=True, height=1000 ) 
 
