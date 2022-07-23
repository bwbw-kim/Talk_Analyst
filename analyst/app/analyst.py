import re
from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib

class Analyst:
    def __init__(self):
        self.regex = re.compile(r"\[([^[]+)\]\s\[(오전|오후)\s[0-9]+:[0-9]+\]\s(.+)")
        self.unnecessary_list = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
                        "ㅏ","ㅑ","ㅓ","ㅕ","ㅗ","ㅛ","ㅜ","ㅠ","ㅡ","ㅣ",
                        "이모티콘", "사진", "근데", "진짜", "아니", "샵검색", "너무", "그래", "하고"]
        self.helper_list = ["은", "는", "이", "가", "도"]
        self.word_count = 150
        self.word_list = []
        self.word_dic_list = {}
    def parse_with_regex(self, msg):
        try:
            matchobj = self.regex.search(msg)
            map = { 'name':matchobj.group(1), 'msg':matchobj.group(3)}
            return map
        except:
            return None, None

    def remove_unnecessary_word(self, msg):
        temp_msg = msg
        for item in self.unnecessary_list:
            temp_msg = temp_msg.replace(item,"")
        for item in self.helper_list:
            if temp_msg[-1] == item:
                temp_msg = temp_msg[:-1]
        if len(temp_msg) <= 1:
            return ""
        return temp_msg

    def get_tags_from_lines(self, line_list):
        for line in line_list:
            map = self.parse_with_regex(line)
            if map['name'] == None:
                continue
            self.name_check(map['name'])
            if map['msg'] != None:
                splited_msg = map['msg'].split()
                for word in splited_msg:
                    self.append_word(word)
                for i in range(len(splited_msg) - 1):
                    word = splited_msg[i] + splited_msg[i+1]
                    self.append_word(word)
        return self.make_tags()

    def make_tags(self):
        counts = Counter(self.word_list)
        tags = counts.most_common(self.word_count)
        return tags

    def name_check(self, name):
        if name not in self.word_dic_list:
             self.word_dic_list[name] = []

    def append_word(self, word):
        deboned_word = self.remove_unnecessary_word(word)
        if deboned_word:
            self.word_dic_list[map['name']].append(deboned_word)
            self.word_list.append(deboned_word)





# wc = WordCloud(font_path="malgun",background_color="white", max_font_size=60)
# cloud = wc.generate_from_frequencies(dict(tags))

# rows=len(word_dic_list)

# fig, ax = plt.subplots(1, 1, figsize=(12.5,6.5))
# font_path = 'fonts/H2GTRM.ttf'
# fontprop = matplotlib.font_manager.FontProperties(fname=font_path, size=18)
# plt.figure()
# plt.axis('off') 
# ax.imshow(cloud)
# ax.axis('off')
# ax.set_title("종합 분석 결과", size = 3, fontproperties=fontprop)
# plt.show()

