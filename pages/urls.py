from django.urls import path
from .views import AboutPageView, HomePageView
#from pages import views (different way)
#from pages import views 

urlpatterns = [
        path("", HomePageView.as_view(), name="home"),
        path("about/", AboutPageView.as_view(), name="about")
    ]