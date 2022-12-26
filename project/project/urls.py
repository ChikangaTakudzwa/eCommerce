"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from product.views import product
from app.views import index, shop, signup, login_page
from cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('shop/', shop, name="shop"),
    path('shop/<slug:model>/', product, name="product"),
    path('add_to_cart/<int:product_id>', add_to_cart, name="add_to_cart"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
