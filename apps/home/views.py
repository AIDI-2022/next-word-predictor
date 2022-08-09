
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import re
from apps.nwp.models import NWP
from django.contrib.auth.models import User
# Create your views here.
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from apps.home.utils import word_predicted_bar, get_pie_chart


@login_required(login_url="/login/")
@api_view(['GET'])
def index(request):
    overall_data = pd.DataFrame(list(NWP.objects.all().values()))
    user_data = pd.DataFrame(list(NWP.objects.filter(user__username=request.user).values()))
    data_len = len(user_data)
    ignored = user_data.selected.isna().sum()
    selected_none = user_data.selected.str.fullmatch('None').sum()
    selected_predictions = data_len-(ignored+selected_none)
    labels = ['Selected Prediction','Selected None', 'Ignored']
    pie_fig = get_pie_chart(labels,[selected_predictions,selected_none,ignored])

    bar_fig = word_predicted_bar(overall_data)
    # bar_plot_ = plot(bar_fig,output_type="div")
    bar_plot_ = bar_fig.to_html(full_html=False, include_plotlyjs='cdn')
    pie_plot_ = pie_fig.to_html(full_html=False, include_plotlyjs='cdn')
    context={'plot1':bar_plot_, 'plot2':pie_plot_}
    # pie_fig = display_pieplot()
    # pie_plot_ = plot(pie_fig,output_type="div")
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def (request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
