import time as t
import datetime as dt
import streamlit as st
import keyboard as key 
from PIL import Image, ImageOps

st.set_page_config(page_title = "Pomodoro Technique", layout = "wide", initial_sidebar_state = "collapsed")


def pomodoro_study(start, stop):
    total_study = 5
    pom = st.empty()
    with pom:
        while total_study >= 0:
            if start:
                mins = dt.timedelta(seconds = total_study)
                st.metric("Time remaining: ", value=f"{str(mins):0>8}")
                total_study -= 1
                t.sleep(1)
            if stop:
                exit()

    
def pomodoro_rest(start, stop):
    rest = 5
    pom = st.empty()
    with pom:
        while rest >= 0:
            if start:
                mins = dt.timedelta(seconds=rest)
                st.metric("Time remaining: ", value=f"{str(mins):0>8}")
                rest -= 1
                t.sleep(1)
            if stop:
                exit()
      
alarm1 = """
            <audio autoplay>
              <source src="https://github.com/oji-py/pomodoro_for_gf/blob/main/sound1.mp3" type="audio/mp3">
            </audio>
            """
alarm2 = """
            <audio autoplay>
              <source src="https://github.com/oji-py/pomodoro_for_gf/blob/main/sound2.mp3" type="audio/mp3">
            </audio>
            """
# HEAD
st.title("Pomodoro Technique")
st.markdown("*Made by Ezra for my love!! <33*")
st.markdown("""*Use it well my love! I hope it helps you in studying. You will be a great nurse!*""")
st.caption("""\tThe Pomodoro Technique is a time management method designed to improve productivity and focus. It was developed by Francesco Cirillo in the late 1980s and is named after the Italian word for \"tomato\" because Cirillo initially used a tomato-shaped kitchen timer to track his work intervals.
\n\tThe technique involves breaking your work into focused intervals, usually 25 minutes in length, called \"Pomodoros.\" During each Pomodoro, you work on a single task without any interruptions or distractions. Once the 25 minutes are up, you take a short break of around 5 minutes to rest and recharge.""")

st.caption("""    
           To use the timer, press the \"Start Timer\" Button. Once pressed the study timer will start, the rest timer will only start once the study timer ends.
           To stop the timer, press the \"Stop Timer\" button. This will terminate the program as a whole, in order to run it again, press the \"R\" key or the rerun on the menubar.
           """)

# PROGRAM
st.write("_"*50)
col3, col4 = st.columns(2)
with col3:  
    start = st.button("Start Timer")
with col4:
    stop = st.button("Stop Timer")

col1, col2 = st.columns(2)
with col1:  
    st.header("Study Timer")
with col2:
    st.header("Rest Timer")
while start:
    with col1:
        loop = st.empty()
        with loop:
            if start:
                pomodoro_study(start, stop)
                st.success("Rest Time!")
            if stop:
                break
               
        st.balloons()
        sound = st.empty()
        sound.markdown(alarm1, unsafe_allow_html=True)  
        t.sleep(2) 
        sound.empty() 
    loop.empty()
    with col2:
        loop = st.empty()
        with loop:
            if start:
                pomodoro_rest(start, stop)
                st.success("Study Time!")
            if stop:
                break
                
        st.balloons()
        sound = st.empty()
        sound.markdown(alarm2, unsafe_allow_html=True)  
        t.sleep(2) 
        sound.empty()
    loop.empty()
    
# COLLAGE:
st.markdown("__"*50)
st.header("Pics Together <33")
pics_num = 12
cols = 3
rows = int(1 + pics_num//cols)
grid = [st.columns(cols) for row in range(rows)]
cols_list = [column for row in grid for column in row]
for column, image in zip(cols_list, list(range(1,13))):
    image = Image.open(f"{image}.JPG")
    image_ = ImageOps.exif_transpose(image)
    column.image(image_)
