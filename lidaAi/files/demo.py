import csv
import os
import pandas as pd
from lida import Manager, TextGenerationConfig, llm
from lida.datamodel import Goal
from lida.utils import plot_raster
import matplotlib

lida1 = Manager(text_gen = llm("openai",api_key = openapikey))


def save_uploaded_csv_file(file):
    
    # return file_name
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Generate a unique file name, e.g., using the original file name
    file_name = os.path.join(temp_dir, 'test.csv')
    
    # Write the uploaded file to the generated file name
    with open(file_name, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    return file_name

def get_csv_summary(filename):
    
    lida1 = Manager(text_gen = llm("openai",api_key = openapikey))
    textgen_config = TextGenerationConfig(n=1,temperature=0.2,model='gpt-3.5-turbo',use_cache=True)
    summary = lida1.summarize(filename,textgen_config=textgen_config)
    return summary

def get_goals(filename):
    lida1 = Manager(text_gen = llm("openai",api_key = openapikey))
    summary = get_csv_summary(filename)
    goals = lida1.goals(summary, n=5)
    return pd.DataFrame(goals)

def get_visualization(filename,query):
    lida1 = Manager(text_gen = llm("openai",api_key = openapikey))
    textgen_config = TextGenerationConfig(n=1,temperature=0.2,model='gpt-3.5-turbo',use_cache=True)
    summary = lida1.summarize(filename,textgen_config=textgen_config)
    matplotlib.use('agg')
    charts = lida1.visualize(summary=summary, goal=query,textgen_config=textgen_config,library="seaborn")
    #os.remove(filename)
    return charts
