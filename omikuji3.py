
import streamlit as st
import numpy as np
import time

from streamlit.elements.image import image_to_url

st.title("晩御飯何する？")
name=st.sidebar.text
date = st.sidebar.date_input("今日の日付を入力してください")
options=["カレー"," 照り焼きチキン","焼き魚","おむらいす","パスタ","うどん","中華丼"]
  
luck = np.random.choice(options, 1, p=[0.1,0.1,0.2,0.1,0.2,0.1,0.2])[0]

if luck=="カレー":
    image = "kari-.jpg"
elif luck=="照り焼きチキン":
    image = "teriyaki.jpg"
elif luck=="焼き魚":
    image = "sakana.jpg"
elif luck=="おむらいす":
     image = "omuraisu.jpg"  
elif luck=="パスタ":
    image ="pasuta.jpg"
elif luck=="うどん":
    image ="udon.jpg"
elif luck=="中華丼":
    image ="cyuuka.jpg"
st.image("lodo.jpg", caption=f"　↓↓↓{name}{date}本日の晩御飯は？↓↓↓", use_column_width=True)
time.sleep(3)

st.write(luck)
st.image(image, use_column_width=True)

if st.button("リセット"):
    placeholder = st.empty()
    placeholder.empty()
