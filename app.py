import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout='wide')

df = pd.read_csv("charcters_stats.csv")

avengers = df[(df.Name == "Iron Man") | (df.Name == "Captain America") | (df.Name == "Spider-Man") | (df.Name == "Hulk") | (df.Name == "War Machine") | (df.Name == "Vision") | (df.Name == "Black Panther") | (df.Name == "Ant-Man")].reset_index(drop=True)

avenger_options = avengers['Name'].unique().tolist()
avenger = st.selectbox('Avengers', avenger_options,0)
row = avengers[avengers['Name']==avenger]


antMan = Image.open('antman.jpg')
blackPanther = Image.open('blackpanther.jpg')
captainAmerica = Image.open('captainamerica.jpg')
hulk = Image.open('hulk.jpg')
ironMan = Image.open('ironman.jpg')
spiderMan = Image.open('spiderman.jpg')
vision = Image.open('vision.jpg')
warMachine = Image.open('warmachine.jpg')

col1,col2,col3 = st.columns(3)
col2.metric('Stength',row.iloc[0]['Strength'])
col2.metric('Speed', row.iloc[0]['Speed'])
col3.metric('Power', row.iloc[0]['Power'])
col2.metric('Intelligence', row.iloc[0]['Intelligence'])
col3.metric('Durability', row.iloc[0]['Durability'])
col3.metric('Combat', row.iloc[0]['Combat'])
st.metric('Rating', row.iloc[:,2:7].mean(axis=1))
#put scatter plot here

if avenger == "Ant-Man":
    col1.image(antMan)
elif avenger == 'Black Panther':
    col1.image(blackPanther)
elif avenger == 'Captain America':
    col1.image(captainAmerica)
elif avenger == 'Hulk':
    col1.image(hulk)
elif avenger == 'Iron Man':
    col1.image(ironMan)
elif avenger == 'Spider-Man':
    col1.image(spiderMan)
elif avenger == 'Vision':
    col1.image(vision)
elif avenger == 'War Machine':
    col1.image(warMachine)






