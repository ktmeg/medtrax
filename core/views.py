from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
# from forms import 
from .models import Patient, Meds
from django.views.decorators.csrf import csrf_exempt



def home(request):
    # user = request.user
    # meds = request.user.meds_set.all()

    return render(request, "home.html")
