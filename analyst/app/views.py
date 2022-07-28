from django.shortcuts import render
from matplotlib import pyplot as plt
import matplotlib
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wordcloud import WordCloud
from app.analyst import Analyst
import base64
import uuid
import os

@csrf_exempt
def Controller(request):
    return render(request, 'empty.html')

@csrf_exempt
@api_view(['POST'])
def Views(request):
    lines = request.data['msg'].split("\n")
    analyst = Analyst()
    font_path = '/home/readytoleave/Talk_Analyst/analyst/app/fonts/NanumGothic.ttf'
    tags = analyst.get_tags_from_lines(lines)
    wc = WordCloud(font_path=font_path, background_color="white", max_font_size=60)
    cloud = wc.generate_from_frequencies(dict(tags))
    fontprop = matplotlib.font_manager.FontProperties(fname=font_path, size=18)
    file_name = uuid.uuid4().hex + ".jpg"
    cloud.to_file(file_name)
    with open(file_name, 'rb') as img:
        base64_string = base64.b64encode(img.read())
    if os.path.isfile(file_name):
        os.remove(file_name)
    return Response(base64_string)