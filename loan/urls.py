"""loan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . views import index, about, team, products, personal, home, education, business, car, contact, blog
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('loan/personal', personal, name='personal'),
    path('loan/home', home, name='home'),
    path('loan/education/', education, name='education'),
    path('loan/business/', business, name='business'),
    path('loan/car/', car, name='car'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    # path('loan/car/', car, name='car'),
    path('products/', products, name='products'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('loan/', include(('products.urls', 'products'), namespace='loan')),
]

urlpatterns += staticfiles_urlpatterns()