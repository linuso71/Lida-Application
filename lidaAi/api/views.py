from django.shortcuts import render
from files.demo import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(http_method_names=['POST'])
def csvfile_visualization(request):
    csv_file = request.data.get('file')
    saved_file = save_uploaded_csv_file(csv_file)
    summary = get_csv_summary(saved_file)
    goals = get_goals(saved_file)
    dic = {}
    i = 0
    for goal in goals:
        query = goal.visualization
        graph = get_visualization(saved_file,query)
        if i <=5:
            dic[i] = graph[0].raster
            i+=1

    print(dic)
    os.remove(saved_file)
    return Response(dic)

@api_view(http_method_names=['POST'])
def visualization_question(request):
    question = request.data.get('question')
    csv_file = request.data.get('file')
    saved_file = save_uploaded_csv_file(csv_file)
    
    graph = get_visualization(saved_file,question)
    os.remove(saved_file)
    try:
        if graph[0]:
            return Response({"data":graph[0].raster })
    except:
        print("this is  data" ,graph)
        return Response({"data":graph})


@api_view(http_method_names=['POST'])
def upload_file(request):
    csv_file = request.data.get('file')
    saved_file = save_uploaded_csv_file(csv_file)
    summary = get_csv_summary(saved_file)
    goals = get_goals(saved_file)
    return Response({"data":goals})