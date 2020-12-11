from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ClaimForm
from .models import Claims
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html/', {})


def sign_in(request):
    return render(request, 'sign_in.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def about(request):
    return render(request, 'about.html/', {})


@login_required()
def claim_log(request):
    form = ClaimForm()

    if request.method == "POST":
        form = ClaimForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('my_claims')

    return render(request, 'claim_log.html/', {
        "form": form
    })


@login_required()
def my_claim(request):
    details = Claims.objects.all
    return render(request, 'my_claims.html/', {'details': details})


#
#
# def blog(request):
#     return render(request, 'blog.html', {})
#
#
# def blog_details(request):
#     return render(request, 'blog-details.html', {})
#
#
# def contact(request):
#     return render(request, 'contact.html', {})
#
#
# def main(request):
#     return render(request, 'main.html', {})
#
#
# def services(request):
#     return render(request, 'services.html', {})
#
#
# def services_detail(request):
#     return render(request, 'services-detail.html', {})
#
#
# def shop(request):
#     return render(request, 'shop.html', {})
#
#
# def shop_details(request):
#     return render(request, 'shop-details.html', {})

