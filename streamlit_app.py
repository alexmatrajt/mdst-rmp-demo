import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='🧠')
st.title('UMICH Rate My Professor Sentiment Analysis')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app provides visualization and interaction with our processed dataset webscraped from Ratemyprofessor.com')
  st.markdown('**How to use the app?**')
  st.warning('Select desired data information with the dropdown menu and checkboxes')
  
st.subheader('Course Review')

# Load data
df = pd.read_csv('data/course_review_polarity_emotion_merged.csv')

# Input widgets
## Genres selection
class_list = df["class"].unique()
class_selection = st.multiselect('Select class', class_list)

df_selection = df[df["class"].isin(class_selection)]


# Display DataFrame
st.dataframe(df_selection, height=400, use_container_width=True)
