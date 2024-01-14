import os
import sys
import json
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()
# Put you OpenAI API key in .env file
openai_key = os.getenv('OPENAI_KEY')
from peewee import *

def class_recommendation(standing, major, school):

    llm = OpenAI(temperature=0,openai_api_key=openai_key)

    
    prompt_class=PromptTemplate(
        template="I am a{standing} {major} student from {school}, Can you recommend some upper division class to me.",
        input_variables=['standing','major','school']
    )
    
    class_chain=LLMChain(llm=llm, prompt=prompt_class)
    response=class_chain({"standing":standing, "major":major, "school":school})
    return response

if __name__ == "__main__":
    standing = 'Freshman'
    major = 'Computer Science'
    school = 'University of California, Santa Barbara'
    print(class_recommendation(standing, major, school))
