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
        path("update_user/", views.update_user, name="update_user"),
        path("update_password/", views.update_password, name="update_password"),
        path("update_info/", views.update_info, name="update_info"),
        path("search/", views.search, name="search"),
        #path("category_summary/", views.category_summary, name="category_summary"),
     
]