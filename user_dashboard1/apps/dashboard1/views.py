# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def index(request):
    return render(request, 'dashboard1/index.html')

def sigin(request):
    return render(request, 'dashboard1/sigin.html')

def register(request):
    return render(request, 'dashboard1/register.html')


def register_user(request):
    user = User.objects.all()
    counter=user.count()
    if counter == 0:
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],user_level=True)
       
    else:
         User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],user_level=False)
         
    return redirect('/sigin')

def login(request):
    if User.objects.filter(email=request.POST['email'],password=request.POST['password'],user_level=True):
        user=User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        
        return redirect('/dashboard/admin')

    else:
        user=User.objects.get(email=request.POST['email'],password=request.POST['password'])
        request.session['user_id'] = user.id
        # print(request.session['normaluser_id'])
        return redirect('/dashboard')

def admin(request):
    user=User.objects.get(id= request.session['user_id'])
    if user.user_level == True:
        user=User.objects.all()
    
        context = {'users':user}

        return render(request, 'dashboard1/admin_dashboard.html',context)

    else:
        return redirect('/dashboard')


def dashboard(request):
    user=User.objects.all()
    context={
        'users':user
    }

    return render(request, 'dashboard1/user_dashboard.html',context)

def new(request):
    
    return render(request, 'dashboard1/newuser.html')

def add_user(request):
    user=User.objects.get(id= request.session['user_id'])
    if user.user_level == True:
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],user_level=request.POST['option'])
         
        return redirect('/dashboard/admin')
    else:
        return redirect('/dashboard')



def edit(request,user_id):
    user = User.objects.get(id = user_id )
    context={
        'users':user,
        'user_id':user,
    }

    return render(request,'dashboard1/edit.html',context)

def update_user(request,user_id):
    user = User.objects.get(id=user_id)

    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    user.password=request.POST['password']
    user.description=request.POST['description']
    user.save()
    return redirect('/dashboard/admin')

def profile(request):
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user_id':user
    }

    return render(request,'dashboard1/edit.html',context)


def edit_profile(request):
    user=User.objects.get(id=request.session['user_id'])
    context={
        'users':user,
        'user_id':user,
        
    }

    return render(request,'dashboard1/edit.html',context)


def info(request,user_id):
    user=User.objects.get(id=user_id)
    post =Post.objects.filter(reciver=user)
    massage= Massage.objects.filter(post=post)
    context={
        'users':user,
        'user_id':user,
        'user_post':post,
        'user_massage':massage,
    }

    return render(request,'dashboard1/user_info.html',context)

def post(request,user_id):
    user=User.objects.get(id=request.session['user_id'])
    post =Post.objects.create(post=request.POST['post'],user=User.objects.get(id=request.session['user_id']),reciver=User.objects.get(id=user_id))

    return redirect('/dashboard/info/'+str(user_id))

def massage(request,post_id,user_id):
    user=User.objects.get(id=request.session['user_id'])
    print(request.POST['massage'])
    massage = Massage.objects.create(massage=request.POST['massage'],user=User.objects.get(id=request.session['user_id']),post=Post.objects.get(id=post_id))
    

    return redirect('/dashboard/info/'+str(user_id))



def remove(request,user_id):
    user = User.objects.get(id = user_id ).delete()       # Note both option of deleting are working

    # user = User.objects.get(id = user_id )
    # user.delete()
    return redirect('/dashboard/admin')

def logoff(request):
    request.session.clear()
    print(request.session.clear())
    return redirect('/')
