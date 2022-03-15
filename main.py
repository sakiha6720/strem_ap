from tkinter import Button
from conda import conda_signal_handler
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from sympy import expand
import time
st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!!!!!'
left_column,right_column = st.columns(2)

button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('rihhe')
    
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')    
    
    
option=st.text_input(
    'あなたが好きな数字を教えてください', 
     
)
con=st.slider('あなたの今の調子は?',0,100,50)

'あなたの好きな数字は',option,'Deth'


'コンディション：',con
#if st.checkbox('Show image'):
#    img=Image.open('tikyu.png')
#    st.image(img,caption='tikyu',use_column_width=True)
