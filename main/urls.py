from django.urls import path
from . import views


urlpatterns = [
        path("index/", views.index, name="index"),
        path("signup/", views.signup, name="signup"),
        path("loginpage/", views.loginpage, name="loginpage"),
        path("logoutpage/", views.logoutpage, name="logoutpage"),
        path("about/", views.about, name="about"),
        path("product/<int:pk>", views.product, name="product"),
        path("category/<str:foo>", views.category, name="category"),
        #path("category_summary/", views.category_summary, name="category_summary"),
     
]