from django.shortcuts import render, HttpResponse, redirect
from . forms import RegistrationForm, CompleteProfile

# Create your views here.
def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.email = form.cleaned_data['email']
        # user.username = form.cleaned_data['email'].split('@')[0]
        user.username = form.cleaned_data['username']
        user.save()
        request.session['user_id'] = user.id
        return redirect('/accounts/profile')
    else:  
        template_name = 'accounts/register.html'
        return render(request, template_name, {"form":form })

# def complete_profile(request, email):
def complete_profile(request):
    # Get the email of the user as the second parameter so as to get the id of who wants to complete the profile
    form = CompleteProfile(request.POST or None)
    if form.is_valid():
        ins = form.save(commit=False)
        ins.user_id = request.session.get('user_id')
        ins.save()
        return redirect('/loan/dashboard')
    else:
        args = {'form': form }
        template_name = 'accounts/profile.html'
        return render(request, template_name, args)