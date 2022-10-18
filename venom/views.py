from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login
from venom.models import Contact
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    #return HttpResponse("hello")
    return render(request,'index.html')
    

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent to our developers. We will try to respond your message !! Q F L I X ')


    return render(request,'contact.html')

def signin(request):
    if request.method == "POST":
        user11 = request.POST['username']
        pass11 = request.POST['pass']
        

        user = authenticate(username=user11, password=pass11)

        if user is not None:
            login(request,user)
            fname = request.user.username
           
            return render(request, "indexa.html",{"name":fname})
           

        else:
            messages.error(request,"Username and password did not matched !!! try again..")
            return redirect('/login/')





    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']

        a = len(fname)
        b = len(lname)
        c = len(username)
        d = len(pass1)

        account = User.objects.all()
        for info in account:
            if info.email == email:
                messages.error(request, 'Email Already Exists!! Try Another')
                return redirect('/signup/')

        
        for info in account:
            if info.username == username:
                messages.error(request, 'Username Already Exists!! Try Somrthing Unique !!')
                return redirect('/signup/')        


        if a<=4 or b<=4 or c<=4:
            messages.error(request, "Length of each field should be at least 4 charactors !!")
            return redirect('/signup/')


        elif d<8:
            messages.error(request, "Password should be at least 8 charactors long ")
            return redirect('/signup/')


        
        elif not username.isalnum() or not fname.isalnum() or not lname.isalnum():
            messages.error(request,"Username only contains letters and numbers !!")
            return redirect('/signup/')


        else:

        

            myuser = User.objects.create_user(username, email, pass1)

            #myuser.username = username
            #myuser.email = email
            myuser.first_name = fname
            myuser.last_name = lname
        
        
            myuser.save()
            messages.success(request, "Your account has been sucessfully created.")

            return redirect('signin')





    return render(request,'signup.html')    




def msgsent(request):
    return render(request,'msgsent.html')


def movie1(request):
    return render(request,'movie1.html')


    