import recommendation as rec
import streamlit as st
from openai import OpenAI
from peewee import *
import os

from dotenv import load_dotenv
load_dotenv()
openai_key = os.getenv('OPENAI_KEY')
st.title('Class Recommendation')

db = SqliteDatabase('students.db')
# Database Initalization
class Student(Model):
    name = CharField()
    age = IntegerField()
    class_standing = CharField()
    major = CharField()

    class Meta:
        database = db
db.connect()
db.create_tables([Student])


student_name = st.text_input('Please enter your name:')
student_age = st.slider('Please enter your age:', 0, 60, 20)
student_major = st.text_input('Please enter your major:')
student_class_standing = st.selectbox('Please enter your class standing:', ['Freshman', 'Sophomore', 'Junior', 'Senior'])
ge=st.radio('Do you want to take a GE course?', ['Yes', 'No'])
if ge=='Yes':
    ge_area=st.selectbox('Please select the GE area you want to take:', ['A-1','A-2' 'B', 'C', 'D', 'E', 'F', 'G'])
major_class=st.radio('Do you want to take a major course?', ['Yes', 'No'])
if major_class=='Yes':
    upper_lower=st.radio('Do you want to take a upper or lower division course?', ['Upper', 'Lower'])
prompt = st.chat_input("Say something")
submit_button = st.button("Submit")
if submit_button:
    student = Student.create(name=student_name, age=student_age, class_standing=student_class_standing, major=student_major)
    st.write("Your information recorded successfully. Student ID: " + str(student.id))
    response=rec.class_recommendation(student_class_standing, student_major,ge,ge_area)
    st.text_area('Here are the recommended courses for you:',response)




#Chatbot
#Still woking on it!!!


st.title("ChatBot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})