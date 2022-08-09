# Home.utils.py
import re 
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def word_predicted_bar(data):
    word_dict = dict()
    remove = re.compile("[\[\]\"]")
    for i in data['predicted']:
        words = remove.sub('',i)
        words = words.split(",")
        for j in words:
            if j not in word_dict.keys():
                word_dict[eval('j')] = 1
            else:
                word_dict[eval('j')] += 1

    word_dict = pd.DataFrame(word_dict.items(), columns = ['Words','Count'])
    word_dict = word_dict.sort_values('Count', ascending = False)

    df = px.data.stocks(indexed=True)-1
    fig = px.bar(word_dict, x = word_dict['Words'], y = "Count", title = 'All Predicted Words')
    return fig

def get_pie_chart(labels,counts):

    fig = px.pie(names=labels, values=counts, hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu)

    return fig

