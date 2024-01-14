from typing import List, Union
from utils.readkey import set_env
set_env()
from langchain.tools import DuckDuckGoSearchRun

# Define tool for searching on WebMD using DuckDuckGo
def duck(input_text):
    search = DuckDuckGoSearchRun()
    search_results = search.run(f"site:ratemyprofessors.com {input_text}")
    return search_results