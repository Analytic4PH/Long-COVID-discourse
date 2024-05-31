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


show_pages(
    [
     Page( parent_dir + "/app.py", "Home", "🏠"),         
     Page( parent_dir + "/jan.py", "Expansions of Figure 1 (pyLDA viz)" ),      
    ] 
)

f = gparent_dir + '/README.md'
# st.text(f)
mkd = Path( f ).read_text()
st.markdown( mkd )
