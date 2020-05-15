from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import MedForm, UserSignUpForm
from .models import Patient, Meds
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required



# =================Sign-up View========================


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

@login_required
def dashboard(request):
    user = request.user
    meds = Meds.objects.all()

    return render(request, "core/dashboard.html", {'meds': meds})

@login_required
def med(request, pk):
    meds = Meds.objects.all()

    return render(request, 'core/med.html', {'meds': meds})

@login_required
def new_med(request):
    user = request.user
    # med = None
    if request.method == "POST":
        form = MedForm(request.POST)
        if form.is_valid():
            med = form.save()
            return redirect('dashboard')
    else:
        form = MedForm()

    return render(request, 'core/new_med.html', {'form': form})

