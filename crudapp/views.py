from django.shortcuts import render
from .forms import userForm
# Create your views here.
def LoginForm(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'testapp/signuppage.html')  # Redirect to a success page
    else:
        form = userForm()
        
    return render(request,'testapp/index.html')

def SingUpForm(req):
    return render(req,'testapp/signuppage.html')