from django.urls import path,re_path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/',views.Signup.as_view(),name ='signup'),
    path('',auth_view.LoginView.as_view(template_name="login.html" ,success_url="{%url 'index' %}"),name='login'),
    path('info/',views.info,name='info'),
    path('index/',views.index,name='index'),        
    path('offc/',views.offc,name='off-comp'),        
    # path('oncp/',views.oncamp,name='on-camp'),        
    path('profs/<int:pk>/',views.profs,name='profs'),        
    path('anns/',views.anns,name='anns'),        
    path('apply/<int:pk>/',views.apply,name='apply'),        
    path('stl/<int:pk>/',views.stul,name='stl'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
