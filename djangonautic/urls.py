from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('',include('django.contrib.auth.urls')),
    path('', article_views.article_list.as_view(), name="home"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html", success_url='/'), name='reset-password'),
    path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password-reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),        
    path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)