from django.shortcuts import render

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def lobby(request):
    return render(request,'nwp/lobby.html')

def predict_next_word(input_text, model='BERT', topk=3):
    bert_tokenizer, bert_model  = load_model('BERT')
    preds = get_prediction_eos(input_text)
    return preds[model.lower()].split('\n')