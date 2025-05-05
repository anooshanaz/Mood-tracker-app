import streamlit as st 
import pandas as pd #data save in files in format
import csv #for reading writting cdv file
import datetime
import os #for file management

MOOD_FILE = "mood_log.csv" #it is constant and have multiple files

#function to load mood data
def load_mood_data():
    #check if file exists
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date","Mood"])
    return pd.read_csv(MOOD_FILE)


def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date,mood])

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")
mood = st.selectbox("Choose a mood", ["Happy", "Neutral", "Sad","Angry"])

if st.button("Lock Mood"):
    
    save_mood_data(today,mood)

st.success("Mood Logged Successfully")

data = load_mood_data()
if not data.empty:
    st.subheader("Mood Trends Over Time")

data["Date"] = pd.to_datetime(data["Date"])

mood_count = data.groupby("Mood").count()["Date"]

st.bar_chart(mood_count)

st.write("Build with by 💞 Anoosha Naz")