import os
import sys
import json
import openai

from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,ConversationChain

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.memory import ConversationBufferMemory


from dotenv import load_dotenv
load_dotenv()




# Put you OpenAI API key in .env file
openai_key = os.getenv('OPENAI_KEY')
from peewee import *

db = SQLDatabase.from_uri('sqlite:////Users/raydu/Desktop/Autonomous_Course_Calendar_Agent/data/courses.db')
llm=OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)


def initialize_memory():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def class_recommendation(class_standing=None,major=None,major_class='No',ge='No',ge_area=None,upper='No'):

    agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    print(class_standing,major,major_class,ge)
    prompt_option='empty prompt'
    if ge == 'Yes':
        
        prompt_option='You are a knowledgeable UCSB course advisor. You specialize in helping students find their passion and interests. You need to assist them in planning their course schedules based on these preferences, ensuring a personalized and fulfilling academic journey. The students wants to take a ge class with area '+ge_area +' can you recommend some for the student? You should first find the generalEducation column that contains '+ge_area+', then look at the course title column and give me top five course that you think are more interesting. Please give the class in the format of 1. courseId:... \n class title: ... \n instructor:... \n reason: \n ge area:... \n why you think the class is good \n 2.'
    elif ge=='No':
        if major_class=='Yes':
            if upper=='Yes':
                prompt_option='You are a knowledgeable UCSB course advisor. You specialize in helping students find their passion and interests. You need to assist them in planning their course schedules based on these preferences, ensuring a personalized and fulfilling academic journey. The student is a ' +major+ ' '+class_standing+', The students wants to take a upper-division ' +major + ' class, can you recommend some for the student? In order to find the upper division, you need to find the class with courseID that contains 3 digit. You should first find the subjectArea column that contains the abbreviation for this major then look at the course title column and give me top five course that you think are more interesting. Please give the class in the format of 1. courseId:... \n class title: ... \n instructor:... \n reason: why you think the class is good \n 2.'
            else:
                prompt_option='You are a knowledgeable UCSB course advisor. You specialize in helping students find their passion and interests. You need to assist them in planning their course schedules based on these preferences, ensuring a personalized and fulfilling academic journey. The student is a ' +major+ ' '+class_standing+', The students wants to take a lower-division ' +major + ' class, can you recommend some for the student? In order to find the lower division, you need to find the class with courseID that contains less than 3 digit. You should first find the subjectArea column that contains the abbreviation for this major then look at the course title column and give me top five course that you think are more interesting. Please give the class in the format of 1. courseId:... \n class title: ... \n instructor:... \n reason: why you think the class is good \n 2.'

        
    # prompt_class=PromptTemplate(
    #     template= "You are a knowledgeable UCSB course advisor. You specialize in helping students find their passion and interests. You need to assist them in planning their course schedules based on these preferences, ensuring a personalized and fulfilling academic journey. The student is a {standing} {major} student, The students wants to take a math class, can you recommend some for the student? You should first find the subjectArea column that contains MATH, then look at the course title column and give me top five course that you think are more interesting. Please give the class in the format of \n 1. \n class title: ... \n instructor:... \n reason: why you think the class is good \n 2.",
    #     input_variables=['standing','major']
    # )

    
    # prompt_class=ChatPromptTemplate.from_messages(
    #     SystemMessage(content=PERSONA_TEMPLATE),
    #     MessagesPlaceholder(variable_name="chat_history"),
    #     HumanMessagePromptTemplate.from_template("{human_input}")
    # )
    
    # class_chain=LLMChain(llm=agent_executor, prompt=prompt_class,output_key='rec_class')


    # response=class_chain({"standing":standing, "major":major, "school":school})
    print(prompt_option)
    print(class_standing,major,major_class,ge,ge_area,upper)
    response=agent_executor.invoke({'input':prompt_option})
    return response['output']

if __name__ == "__main__":
    class_standing = 'Senior'
    major = 'CS'
    ge='No'
    ge_area='None'
    major_class='Yes'
    upper='Yes'
    print(class_recommendation(class_standing,major,major_class,ge,ge_area,upper))