from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .utils import predict_next_word
import json, datetime
@login_required(login_url="/login/")
def lobby(request):
    return render(request,'nwp/lobby.html')
@api_view(['POST'])
def nwp(request):
        if request.method == 'POST':
            if request.body:
                json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
            try:
                text = json_data.get('text')
                # model=json_data.get('model','BERT') 
                # topk = json_data.get('topk',3)
                predicted_words = predict_next_word(text)
                return Response({"message":"Sucess","time":datetime.datetime.now(),'data':predicted_words})


            except Exception as e:
                return Response({"message":"Failure","time":datetime.datetime.now(),'data':{"error":str(e)}})


    # bert_tokenizer, bert_model  = load_model('BERT')
    # preds = get_prediction_eos(input_text)
    # return preds[model.lower()].split('\n')