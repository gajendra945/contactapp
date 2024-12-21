from django.contrib import admin
from django.urls import path
from contact_app.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_view, name='contact'),
]
