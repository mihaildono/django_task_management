from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from accounts.api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^current-user', views.current_user, name="current_user"),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
    url(r'^', include(router.urls))
]
