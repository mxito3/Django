from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, VideoSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from .models import Video

# rest api test


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


#post
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data.get('your_name')
            print(name)
            return HttpResponseRedirect('/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


def contactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            cc_myself = form.cleaned_data.get('cc_myself')

            recipients = ['1477311729@qq.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks')
    else:
        form = ContactUsForm()
    return render(request, 'contactUs.html', {'form': form})
