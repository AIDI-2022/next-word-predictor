from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

def display_pieplot():
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day')
    return fig

@api_view(['GET'])
def product_lot_analytics_geomap(request):
    fig = display_pieplot()
    plot_ = plot(fig,output_type="div")
    return render(request, 'index.html', {'plot':plot_})