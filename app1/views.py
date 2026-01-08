from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def run(request):
   return render(request,'start.html')
def looked(request):
   return render(request,'cakemart1.html')

def home(request):
   return render(request,'cakemart1.html')
def showed(request):
   return render(request,'wedding.html')
def seen(request):
   return render(request,'babyshower.html')
def see(request):
   return render(request,'christmas.html')
def look(request):
   return render(request,'birthday.html')


def a(request):
   return render(request,'abt.html')
def b(request):
   return render(request,'cont.html')


def show(request):
 return render(request,'cakeform.html')


def receive(request):
  if  request.method=='POST':
     name=request.POST.get('first_name')
     email=request.POST.get('email')
     phone=request.POST.get('country_code')
     month=request.POST.get('month')
     date=request.POST.get('day')
     size=request.POST.get('size')
     flavour=request.POST.get('taste')
     #quantity=request.POST.get('quantity')
     code=request.POST.get('ccode')
     description=request.POST.get('message')
     z=Booking(name=name,email=email,phone=phone,month=month,date=date,size=size,flavour=flavour,code=code,description=description)
     z.save()
     return HttpResponse("<h1>Your Order Has been Successfully Booked....</h1>")
  else:
     return HttpResponse("<h1>Invalid Request...</h1>") 


     

def display(request):
 return render(request,'f2.html')

def doOrder(request):
  if  request.method=='POST':
     name=request.POST.get('f_name')
     email=request.POST.get('mail')
     phone=request.POST.get('p_code')
     month=request.POST.get('mon')
     date=request.POST.get('dday')
     size=request.POST.get('s_size')
     flavour=request.POST.get('t_taste')
     #quantity=request.POST.get('quantity')
     code=request.POST.get('c_code')
     description=request.POST.get('msg')
     z=Order(name=name,email=email,phone=phone,month=month,date=date,size=size,flavour=flavour,code=code,description=description)
     z.save()
     return HttpResponse("<h1>Your Order Has been Successfully Booked....</h1>")
  else:
     return HttpResponse("<h1>Invalid Request...</h1>") 


def present(request):
 return render(request,'f3.html')


def future(request):
  if  request.method=='POST':
     name=request.POST.get('nname')
     email=request.POST.get('eemail')
     phone=request.POST.get('try_code')
     month=request.POST.get('mmonth')
     date=request.POST.get('d_day')
     size=request.POST.get('ssize')
     flavour=request.POST.get('ttaste')
     #quantity=request.POST.get('qquantity')
     code=request.POST.get('code')
     description=request.POST.get('mmessage')
     z=Purchase(name=name,email=email,phone=phone,month=month,date=date,size=size,flavour=flavour,code=code,description=description)
     z.save()
     return HttpResponse("<h1>Your Order Has been Successfully Booked....</h1>")
  else:
     return HttpResponse("<h1>Invalid Request...</h1>") 



def shown(request):
 return render(request,'f4.html')


def past(request):
  if  request.method=='POST':
     name=request.POST.get('nm')
     email=request.POST.get('em')
     phone=request.POST.get('cc')
     month=request.POST.get('m')
     date=request.POST.get('d')
     size=request.POST.get('s')
     flavour=request.POST.get('f')
     #quantity=request.POST.get('q')
     code=request.POST.get('c')
     description=request.POST.get('mg')
     z=Buy(name=name,email=email,phone=phone,month=month,date=date,size=size,flavour=flavour,code=code,description=description)
     z.save()
     return HttpResponse("<h1>Your Order Has been Successfully Booked....</h1>")
  else:
     return HttpResponse("<h1>Invalid Request...</h1>") 








def feed(request):
 return render(request,'feedback.html')


def doFeedback(request):
  if  request.method=='POST':
     rate=request.POST.get('inlineRadioOptions')
     comments=request.POST.get('comment')
     name=request.POST.get('fname')
     email=request.POST.get('gmail')
     
     z=Feedback(rate=rate,comments=comments,name=name,email=email)
     z.save()
     return HttpResponse("<h1>Your Feedback Has been Successfully Received....</h1>")
  else:
     return HttpResponse("<h1>Invalid Request...</h1>") 



def reporder(request):
     wed=Booking.objects.all()
     return render(request,'report1.html',{'wed':wed})
    
def reporder2(request):
     shower=Order.objects.all()
     return render(request,'report2.html',{'shower':shower})
    
def reporder3(request):
     bday=Purchase.objects.all()
     return render(request,'report3.html',{'bday':bday})
    
def reporder4(request):
     crist=Buy.objects.all()
     return render(request,'report4.html',{'crist':crist})

def reporder5(request):
     feedback=Feedback.objects.all()
     return render(request,'report5.html',{'feedback':feedback})
    