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
    path('org/', views.OrganizationListView.as_view(), name='organization_list'),
    path('org/<str:pk>/', views.OrganizationView.as_view(), name='organization'),
    path('highscore/', views.ScoreboardView.as_view(), name='scoreboard'),
    path('api/', include(router.urls)),
    # TODO find a way to integrate with router
    path('organization_scoreboard/', views.organization_scoreboard)
]
