"""neheb URL Configuration

"""
from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'ribbons', views.RibbonViewSet)
router.register(r'attendees', views.AttendeeViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'itemtypes', views.ItemTypeViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    # TODO find a way to integrate with router
    path('organization_scoreboard/', views.organization_scoreboard)
]
