from st_pages import Page, show_pages, add_page_title  # allow multipages
import streamlit as st
import os, sys
from glob import glob
import streamlit.components.v1 as components

# ================================ configs ================================ 
st.set_page_config(layout="wide")
DEBUG=0

# ================================  add paths ================================ 
parent_dir = os.path.dirname( os.path.realpath(__file__) )
gparent_dir = os.path.dirname( parent_dir )



st.text( parent_dir  )
st.text( gparent_dir )
sys.path.append( gparent_dir )
sys.path.append( parent_dir  )


# ================================ Widget =============================== 
st.header("Other results")

tabs = st.tabs( ['Europe', 'USA', 'Canada'] )

month = os.path.basename( __file__ ).split( '.' )[0]

with tabs[0]:
 ss = gparent_dir + f'/visualizations/html/EU/eu*{month}*.html' 
 if DEBUG:
  st.text(ss)
 files = glob( ss )
 html_datasets, pages = [], []
 st.header( 'Results on tweets from Europe' )
 
 for i,file in enumerate( files ):
   with open(file,'r') as f: 
     html_data = f.read()   
   st.write( month.upper() + ' 2021' ) 
   components.html(html_data, scrolling=True, height=1000 ) 

with tabs[1]:
 st.header( 'Results on tweets from USA' )
 files = glob( gparent_dir + f'/visualizations/html/US/us*{month}*.html' )
 html_datasets, pages = [], []
 for i,file in enumerate( files ):
   with open(file,'r') as f: 
     html_data = f.read()   
   #st.write( file )
   st.write( month.upper() + ' 2021' ) 
   components.html(html_data, scrolling=True, height=1000 ) 

with tabs[2]:
 st.header( 'Results on tweets from Canada' )
 files = glob( gparent_dir + f'/visualizations/html/*{month}*.html' )
 html_datasets, pages = [], []
 for i,file in enumerate( files ):
   with open(file,'r') as f: 
     html_data = f.read()   
   st.write( month.upper() + ' 2021' ) 
   components.html(html_data, scrolling=True, height=1000 ) 


#html_datasets.append( html_data ) 
  
  
