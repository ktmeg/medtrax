# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import MedForm, UserSignUpForm
from .models import Patient, Meds, Log
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
from users.models import User
import json
from django.views.decorators.http import require_GET, require_POST

# =================Sign-up View========================


# class UserSignUpView(CreateView):
#     model = User
#     form_class = UserSignUpForm
#     template_name = 'registration/signup.html'

#     def home(request):
#         if request.user.is_authenticated:
#             return redirect('dashboard')
#         return render(request, 'dashboard.html')

#     def form_valid(self, form):
#         user = form.save()
#         user.save()
#         login(self.request, user)
#         return redirect('dashboard')

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

    return render(request, 'core/dashboard.html', {'meds': meds})


@login_required
def med(request, pk):
    meds = Meds.objects.all()

    return render(request, 'core/med.html', {'meds': meds})

# =========================================MED FORMS===================================================


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


@login_required
def edit_med(request, pk):
    med = get_object_or_404(Meds, pk=pk)
    if request.method == "POST":
        form = MedForm(request.POST, instance=med)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    else:
        form = MedForm(instance=med)
    return render(request, 'core/edit_med.html', {'form': form, 'pk': pk, 'med': med})


@login_required
def delete_med(request, pk):
    med = get_object_or_404(Meds, pk=pk)
    med.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# @login_required
@csrf_exempt
def log(request, pk):
    med = Meds.objects.get(pk=pk)
    instance = Log(med = request.med)
    instance = Log(user = request.user)
    if request.method == 'POST':
        request.body
        data = json.loads(request.body)
        instance = Log(**data)
        # instance.med = med
        # instance.user = request.user
        instance.save()   
        return redirect ('dashboard')


    
