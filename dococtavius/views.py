from django.shortcuts import render, HttpResponseRedirect, reverse
from recipeBox.models import RecipeItem 
from recipeBox.models import Author
from recipeBox.forms import NewsAdd, AuthAdd, LoginForm
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def ticket_view(request):
    pass



def assignedticket_view(request):
    pass