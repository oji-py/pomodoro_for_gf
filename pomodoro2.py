import streamlit as st
import time as t
from datetime import timedelta
import base64
from PIL import Image, ImageOps

st.set_page_config(page_title = "Pomodoro Technique", layout = "wide", initial_sidebar_state = "collapsed")

class Pomodoro:
    def study(self, study=25*60):
        header = st.empty()
        pom = st.empty()
        with header:
            st.header("Study Timer")
        with pom:
            while study >= 0:
                countdown = str(timedelta(seconds=study))
                st.metric("Time Remaining", value=f"{countdown:0>8}")
                study -= 1
                t.sleep(1)
            st.success("Rest Time!")
        st.balloons()
        self.autoplay_audio("New_Project2.mp3")
        pom.empty()
        header.empty()
    def rest(self, rest=5*60):
        header = st.empty()
        pom = st.empty()
        with header:
            st.header("Rest Timer")
        with pom:
            while rest >= 0:
                countdown = str(timedelta(seconds=rest))
                st.metric("Time Remaining", value=f"{countdown:0>8}")
                rest -= 1
                t.sleep(1)
            st.success("Study Time!")
        st.balloons()
        self.autoplay_audio("New_Project.mp3")
        pom.empty()
        header.empty()
    def autoplay_audio(self, file_path: str):
        sound = st.empty()
        with sound:
            with open(file_path, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                md = f"""
                    <audio autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    """
                st.markdown(
                    md,
                    unsafe_allow_html=True,
                )
        t.sleep(13)
        sound.empty()

st.title("Pomodoro Technique")
st.markdown("*Made by Ezra for my love!! <33*")
st.markdown("""*Use it well my love! I hope it helps you in studying. You will be a great nurse!*""")
st.caption("""\tThe Pomodoro Technique is a time management method designed to improve productivity and focus. It was developed by Francesco Cirillo in the late 1980s and is named after the Italian word for \"tomato\" because Cirillo initially used a tomato-shaped kitchen timer to track his work intervals.
\n\tThe technique involves breaking your work into focused intervals, usually 25 minutes in length, called \"Pomodoros.\" During each Pomodoro, you work on a single task without any interruptions or distractions. Once the 25 minutes are up, you take a short break of around 5 minutes to rest and recharge.""")

st.caption("""    
           To use the timer, press the \"Start Timer\" Button. Once pressed the study timer will start, the rest timer will only start once the study timer ends.
           To stop the timer, press the \"Stop Timer\" button. This will terminate the program as a whole, in order to run it again, press the \"R\" key or the rerun on the menu bar.
           """)

# PROGRAM
st.write("_"*50)
# main program
col1, col2 = st.columns([40, 50])
with col2:
    start = st.button("Start")
    print(end="") 
    stop = st.button("Stop")
    
col3, col4 = st.columns([40, 60], gap="large")
with col4:
    main = Pomodoro()
    counter = 0
    empty = st.empty()
    header = "Study Timer"
    while start:
        if counter == 4:
            main.study()
            main.rest(rest=25*60)
        elif stop:
            exit()
        else:
            main.study()
            main.rest()
        counter += 1

st.markdown("__"*50)
st.header("Pics Together <33")
pics_num = 12
cols = 3
rows = int(1 + pics_num//cols)  # typecasting the result to an int (works differently in c)
grid = [st.columns(cols) for row in range(rows)]
cols_list = [column for row in grid for column in row]
for column, image in zip(cols_list, list(range(1,13))):  # pairs the photos and columns
    image = Image.open(f"{image}.JPG")
    image_ = ImageOps.exif_transpose(image)
    column.image(image_)

    



