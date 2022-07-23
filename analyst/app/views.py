from django.shortcuts import render
from matplotlib import pyplot as plt
import matplotlib
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wordcloud import WordCloud
from app.analyst import Analyst


@api_view(['POST'])
def Views(request):
    lines = request.data['msg'].split("\n")
    analyst = Analyst()

    font_path = '/home/readytoleave/Talk_Analyst/analyst/app/fonts/NanumGothic.ttf'
    tags = analyst.get_tags_from_lines(lines)
    wc = WordCloud(font_path=font_path, background_color="white", max_font_size=60)
    cloud = wc.generate_from_frequencies(dict(tags))
    fontprop = matplotlib.font_manager.FontProperties(fname=font_path, size=18)
    cloud.to_file('test.jpg')
    return Response(tags)