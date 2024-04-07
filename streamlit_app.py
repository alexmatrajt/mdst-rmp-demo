import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title='Umich RMP Interactive Data Explorer', page_icon='📊')
st.title('📊 Umich RMP Interactive Data Explorer')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the michigan professor rating data based on polarity and emotion score')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select class of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
st.subheader('Sentient Analysis Results')

# Load data
df = pd.read_csv('data/course_review_polarity_emotion_merged.csv')

# Input widgets
## Genres selection
class_list = df["class"].unique()
class_selection = st.multiselect('Select class', class_list)

df_selection = df[df["class"].isin(class_selection)]


# Display DataFrame
st.dataframe(df_selection, height=400, use_container_width=True)
