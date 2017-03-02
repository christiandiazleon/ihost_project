# -*- coding: utf-8 -*-

# where we have used the shortcut render, which lets you load a template,
# create a context adding a bunch of variables by default, such as information
# about the current logged-in user, or the current language, render it and
#return an HttpResponse, all in one function.
from django.shortcuts import render

def home(request):
    return render(request, "taskbuster/index.html", {})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
