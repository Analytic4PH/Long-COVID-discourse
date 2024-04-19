from st_pages import Page, show_pages, add_page_title  # allow multipages
import streamlit as st
import os, sys

# ================================  add paths ================================ 
sys.path.append(gparent_dir)
sys.path.append(parent_dir)

path_to_html = gparent_dir + '/visualizations/html/yearly_network_graph.html'

with open(path_to_html,'r') as f: 
    html_data = f.read()

# ================================  widget ================================ 
# Show in webpage
st.header("")
st.components.v1.html(html_data, scrolling=True, height=500 ) 


# ================================ Widgets =============================== 

from glob import glob
files = glob( gparent_dir + '/visualizations/html/*.html' )
pages = []
for i,f in enumerate( files ):
  pages.append( Page( f, f'Result {i}' ) ) 
  
show_pages(
    [
        Page( parent_dir + "/app.py", "Home", "🏠"),         
    ] + pages
)
