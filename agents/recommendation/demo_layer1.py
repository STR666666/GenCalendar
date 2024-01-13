#pip install peewee
import gradio as gr
import random
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from gradio_pdf import PDF
import openai
from peewee import *
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



def random_response(message, history):
    return random.choice(["Yes", "No"])
def process_student_info(name, age, class_standing,major,transcript):
    if not name:
        return 'Please enter your name!'
    elif not class_standing:
        return 'Plase enter your class standing'
    elif not major:
        return 'Plase enter your major'
    else:
        student = Student.create(name=name, age=age, class_standing=class_standing, major=major)
        return "Your information recorded successfully. Student ID: " + str(student.id)
def random_response(message, history):
    return random.choice(["Yes", "No"])
with gr.Blocks() as demo:
    gr.Markdown("Hello, please enter your basic information for initialization.")
    with gr.Row():
        with gr.Column():
            iface = gr.Interface(
                fn=process_student_info, 
                inputs=[
                    "text", 
                    gr.Slider(minimum=0, maximum=100, step=1),
                    gr.Radio(["Freshman", "Sophomore", "Junior", "Senior"]),
                    'text',
                    gr.File()
                ], 
                title="GenCalendar Demo",
                allow_flagging='never',
          
                outputs="text",
                
            )
        chatBot=gr.ChatInterface(random_response)
    
demo.launch()