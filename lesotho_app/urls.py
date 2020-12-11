from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('claim/', views.claim_log, name="claim"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('claims/', views.my_claim, name="claims"),
    # path('blog/', views.blog, name="blog"),
    # path('blog-details/', views.blog_details, name="blog-details"),
    # path('contact/', views.contact, name="contact"),
    # path('mail/', views.main, name="main"),
    # path('services/', views.services, name="services"),
    # path('services-detail/', views.services_detail, name="services-detail"),
    # path('shop/', views.shop, name="shop"),
    # path('shop-details/', views.shop_details, name="shop-details"),
    path('about/', views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

