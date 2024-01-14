import os
import re
import gradio as gr
from typing import List, Union
from utils.readkey import set_env
set_env()

# Importing langchain related modules
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.tools import DuckDuckGoSearchRun
from langchain.schema import AgentAction, AgentFinish
from langchain.chat_models import ChatOpenAI
from utils.tools import duck
from recommender.template import CustomPromptTemplate, CustomOutputParser
from prompts.prompts_system import REACT_TEMPLATE
from recommender.recommender_system import Recommender

# Set up the tools available to the agent
tools = [
    Tool(
        name="Search ratemyprofessors",
        func=duck,
        description="Useful for answering course and professor selection based on students' comments and scores."
    )
]

output_parser = CustomOutputParser()

prompt = CustomPromptTemplate(
            template=REACT_TEMPLATE,
            tools=tools,
            input_variables=["input", "intermediate_steps"]
        )

# Setup for the agent and its execution
output_parser = CustomOutputParser()
llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])
llm_chain = LLMChain(llm=llm, prompt=prompt)
tool_names = [tool.name for tool in tools]

agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:"],
    allowed_tools=tool_names
)

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

rec = Recommender()

# Greeting message for the chatbot
greeting = """
Let's find your passion!
"""

rec.agent_exec(agent_executor)

# def respond_to_input(user_input):
#     # Use the agent_executor to process the user input
#     response = agent_executor.run(user_input)

#     # Format the response as a list of tuples [(user_input, response)]
#     chat_history = [(user_input, response)]

#     # Return the formatted chat history
#     return chat_history

with gr.Blocks() as demo:
    gr.Markdown('# GenCalendar')
    gr.Markdown(greeting)
    with gr.Row():
        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Talk to me!")
            clear = gr.ClearButton([msg, chatbot])

        # When the user submits their message, process it and update the chatbot
        msg.submit(rec.respond_to_input, inputs=msg, outputs=[msg, chatbot])

# Launch the Gradio app
demo.launch()