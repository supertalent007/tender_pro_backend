"""
URL configuration for Tender_Pro_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from TenderApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', views.my_api_test, name='my_api_test'),
    path('api/getExeTeamMembers/', views.getExeTeamMembers, name='getExeTeamMembers'),
    path('api/home/header/', views.get_home_page_header, name="get_home_page_header"),
    path('api/home/process_header/', views.get_home_process_header, name="get_home_process_header"),
    path('api/home/process_content/', views.get_home_process_content, name="get_home_process_content"),
    path('api/news/', views.get_news, name="get_news"),
    path('api/testimonials/', views.get_testimonials, name="get_testimonials"),
    path('api/products/', views.get_products, name="get_products"),
    path('api/product/<int:id>', views.get_single_product, name="get_single_product"),
    path('api/benefits/<int:id>', views.get_product_benefits, name="get_product_benefits"),
    path('api/team/', views.get_team, name="get_team"),
    path('api/advisor/', views.get_advisor, name="get_advisor"),
    path('api/design_privacy/', views.get_design_privacy, name="get_design_privacy"),
    path('api/our_values/', views.get_our_values, name="get_our_values"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
