from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files import File
from .models import *
import random
import datetime


# Create your views here.
def index(request):
    if request.user.username == '':
        return render(request, 'index.html', {'name': 'visitor', 'logged_in': False})
    else:
        rec = Record.objects.filter(username=request.user.username).all()[0]
        return render(request, 'index.html',
                      {'name': f'{request.user.first_name} {request.user.last_name}', 'logged_in': True})


def login_page(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user == None:
            message = 'Invalid username or password'
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {'message':message})


def register_page(request):
    message = 'Please enter the account details'
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        repeat = request.POST.get('pwrepeat')
        user = User.objects.filter(username=username)
        if user.exists():
            return render(request, 'register.html', {'message': "Username already taken!"})
        elif password != repeat:
            return render(request, 'register.html', {'message': "Password entered doesn't match"})
        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username
        )
        user.set_password(password)
        user.save()

        rec = Record.objects.create(username=username)
        rec.save()

        return redirect('/login')

    context = {
        'message': message
    }
    return render(request, 'register.html', context)


def logout_page(request):
    logout(request)

    return render(request, 'logout.html')


def physics(request):
    if request.user.username == '':
        return render(request, 'loginneeded.html', {})
    rec = Record.objects.filter(username=request.user.username).all()[0]
    files = PhysicsMCQ.objects.values_list('filename')
    qs = len(files)
    result = 'Please choose the correct answer'
    last = ''
    if request.method == 'POST' and rec.currentphys != -1:
        if 'next' in list(request.POST.keys()):
            used = list(rec.physics)
            canuse = []
            for i in range(qs):
                if used[i] == '0':
                    canuse.append(i)
            if len(canuse) == 0:
                rec.currentphys = -1
                rec.save()
            else:
                rec.currentphys = canuse[random.randint(0, len(canuse) - 1)]
                rec.save()
        else:
            stat = PhysicsStats.objects.filter(filename=files[rec.currentphys][0]).all()[0]
            last = f"Your answer: {request.POST['answer']}"
            if request.POST['answer'] == PhysicsMCQ.objects.filter(no=rec.currentphys).all()[0].ans:
                result = 'Correct!'
                if rec.physics[rec.currentphys] == '0':
                    new = list(rec.physics)
                    new[rec.currentphys] = '1'
                    rec.physics = ''.join(new)
                    rec.physsolved += 1
                    rec.totalsolved += 1
                    rec.physlast = datetime.datetime.now()
                    rec.ovrlast = datetime.datetime.now()
                    rec.save()
                stat.correct += 1
            else:
                result = 'Wrong answer'
                stat.wrong += 1
            stat.save()
    if rec.currentphys == -1:
        result = 'You have finished all questions, congratulations!'
        context = {
            'filename': 'phys/finished.jpg',
            'result': result,
            'last': last,
            'Title': 'Physics practice',
            'source': ''
        }
    else:
        context = {
            'filename': f'phys/{files[rec.currentphys][0]}',
            'result': result,
            'last': last,
            'Title': 'Physics practice',
            'source': f"{'_'.join(files[rec.currentphys][0].strip('.png').split('_')[:-1])} Question {files[rec.currentphys][0].strip('.png').split('_')[-1]}"
        }
    return render(request, 'practice.html', context)


def economics(request):
    if request.user.username == '':
        return render(request, 'loginneeded.html', {})
    rec = Record.objects.filter(username=request.user.username).all()[0]
    files = EconomicsMCQ.objects.values_list('filename')
    qs = len(files)
    result = 'Please choose the correct answer'
    last = ''
    if request.method == 'POST' and rec.currentecon != -1:
        if 'next' in list(request.POST.keys()):
            used = list(rec.economics)
            canuse = []
            for i in range(qs):
                if used[i] == '0':
                    canuse.append(i)
            if len(canuse) == 0:
                rec.currentecon = -1
                rec.save()
            else:
                rec.currentecon = canuse[random.randint(0, len(canuse) - 1)]
                rec.save()
        else:
            last = f"Your answer: {request.POST['answer']}"
            stat = EconomicsStats.objects.filter(filename=files[rec.currentecon][0]).all()[0]
            if request.POST['answer'] == EconomicsMCQ.objects.filter(no=rec.currentecon).all()[0].ans:
                result = 'Correct!'
                if rec.economics[rec.currentecon] == '0':
                    new = list(rec.economics)
                    new[rec.currentecon] = '1'
                    rec.economics = ''.join(new)
                    rec.econsolved += 1
                    rec.totalsolved += 1
                    rec.econlast = datetime.datetime.now()
                    rec.ovrlast = datetime.datetime.now()
                    rec.save()
                stat.correct += 1
            else:
                result = 'Wrong answer'
                stat.wrong += 1
            stat.save()
    if rec.currentecon == -1:
        context = {
            'filename': 'econfinished.jpg',
            'result': result,
            'last': last,
            'Title': 'Economics practice',
            'source': ''
        }
    else:
        context = {
            'filename': f'econ/{files[rec.currentecon][0]}',
            'result': result,
            'last': last,
            'Title': 'Economics practice',
            'source': f"{'_'.join(files[rec.currentecon][0].strip('.png').split('_')[:-1])} Question {files[rec.currentecon][0].strip('.png').split('_')[-1]}"
        }
    return render(request, 'practice.html', context)


def getname(username):
    user = User.objects.filter(username=username).all()[0]
    return f'{user.first_name} {user.last_name}'


def leaderboard(request):
    top10ovr, top10phys, top10econ = [], [], []
    for i in Record.objects.all().order_by('-totalsolved', 'ovrlast')[:10]:
        top10ovr.append([getname(i.username), i.totalsolved])
    for i in Record.objects.all().order_by('-physsolved', 'physlast')[:10]:
        top10phys.append([getname(i.username), i.physsolved])
    for i in Record.objects.all().order_by('-econsolved', 'econlast')[:10]:
        top10econ.append([getname(i.username), i.econsolved])
    context = {
        'top10ovr': top10ovr,
        'top10phys': top10phys,
        'top10econ': top10econ
    }
    return render(request, 'leaderboard.html', context)


def account(request):
    if request.user.username == '':
        return render(request, 'loginneeded.html', {})

    message = ''
    user = User.objects.filter(username=request.user.username).all()[0]
    if request.method == 'POST':
        if request.POST.get('name') != None:
            newfirst = request.POST['firstname']
            newlast = request.POST['lastname']
            user.first_name = newfirst
            user.last_name = newlast
            user.save()
            message = 'Name changed successfully'
        else:
            entered = request.POST['oldpassword']
            new1 = request.POST['newpassword']
            new2 = request.POST['newpwrepeat']
            if authenticate(username=request.user.username, password=entered) == None:
                message = 'Invalid original password'
            elif new1 != new2:
                message = "New password doesn't match"
            else:
                user.set_password(new1)
                user.save()
                message = "Password changed successfully"
    context = {
        'firstname': user.first_name,
        'lastname': user.last_name,
        'message': message
    }
    return render(request, 'account.html', context)


def customised(request):
    return render(request, 'customised.html', {})


def about(request):
    return render(request, 'about.html', {})


def database(request):
    if request.user.is_superuser:
        db_path = settings.DATABASES['default']['NAME']
        dbfile = File(open(db_path, "rb"))
        response = HttpResponse(dbfile)
        response['Content-Disposition'] = 'attachment; filename=%s' % db_path
        response['Content-Length'] = dbfile.size
        return response
    else:
        return render(request, '404.html')