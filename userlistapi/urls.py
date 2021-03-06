from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('userlist.urls')),
    path('users', TemplateView.as_view(template_name='user_list.html')),
]

