from st_pages import Page, show_pages, add_page_title  # allow multipages
import streamlit as st
import os, sys
from glob import glob
import streamlit.components.v1 as components
from pathlib import Path

# ================================  add paths ================================ 
parent_dir = os.path.dirname( os.path.realpath(__file__) )
gparent_dir = os.path.dirname( parent_dir )

st.set_page_config(layout="wide") 
st.text( parent_dir  )
st.text( gparent_dir )
sys.path.append( gparent_dir )
sys.path.append( parent_dir  )

if 0:
 # ================================  Widget ================================ 
 path_to_html = gparent_dir + '/visualizations/project2/yearly_network_graph.html'
 with open(path_to_html,'r') as f: 
     html_data = f.read()
 
 st.header("Project 2")
 components.html(html_data, scrolling=True, height=500 ) 
 
show_pages(
    [
     Page( parent_dir + "/app.py", "Home", "🏠"),         
     Page( parent_dir + "/jan.py", "Jan 2021 (pyLDA viz)"),         
     Page( parent_dir + "/march.py", "Mar 2021"),         
     Page( parent_dir + "/may.py", "May 2021"),         
     Page( parent_dir + "/july.py", "Jul 2021"),         
     Page( parent_dir + "/sep.py", "Sep 2021"),         
     Page( parent_dir + "/nov.py", "Nov 2021"),         
     Page( parent_dir + "/show_notebooks.py", "Notebooks (test)"),         
    ] 
)

f = gparent_dir + '/README.md'
# st.text(f)
mkd = Path( f ).read_text()
st.markdown( mkd )
