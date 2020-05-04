from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import MedForm
from .models import Patient, Meds
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView


# class SignUpView(TemplateView):
#     template_name = 'accounts/login.html'

#     def home(request):
#         if request.user.is_authenticated:
#             if request.user.is_teacher:
#                 return redirect('dashboard')
#             else:
#                 return redirect('dashboard')
#         return render(request, 'dashboard.html')


def dashboard(request):
    user = request.user
    meds = Meds.objects.all()

    return render(request, "core/dashboard.html", {'meds': meds})


def add_med(request):
    user = request.user
    if request.method == "POST":
        form = MedForm(request.POST)
        if form.is_valid():
            med = form.save()
            return redirect('med', med.pk)
    else:
        form = MedForm()

    return render(request, 'core/new_med.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                form = LoginForm()
                login(request, user)
