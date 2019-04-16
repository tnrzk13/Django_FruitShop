from django.urls import path
from . import views

#path(url)
#url is url without the /products 
urlpatterns = [
    path("", views.index), #dont call function, django will do that at runtime
    path("new/", views.new)
]