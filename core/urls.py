"""neheb URL Configuration

"""
from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'ribbons', views.RibbonViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    path('organization_scoreboard/', views.organization_scoreboard)
]
