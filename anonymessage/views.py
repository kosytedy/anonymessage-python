from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import MessageForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    messages_list = request.user.message.order_by('-date_posted').all()
    
    paginator = Paginator(messages_list, 5)
    #return HttpResponse(paginator.count)
    page = request.GET.get('page', 1)
    try:
        messages = paginator.get_page(page)
    except PageNotAnInteger:
        messages = paginator.get_page(1)
    except EmptyPage:
        messages = paginator.get_page(paginator.num_pages)

    private_link = request.build_absolute_uri(reverse('private_link', args=(request.user.username,)))

    #return HttpResponse(messages.object_list)
    return render(request, 'dashboard.html', {'messages':messages, 'private_link': private_link})

def send_message(request, username):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        messaged_to = get_object_or_404(User, username=username)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = messaged_to
            message.date_posted = timezone.now()
            message.save()

            messages.success(request, 'You have sent %s an anonymous message' % username, extra_tags='success')
            return render(request, 'success.html')
    else:
        form = MessageForm()
        return render(request, 'message.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')