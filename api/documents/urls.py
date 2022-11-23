from django.urls import path, include
from rest_framework import routers
from .api import UsersViewSet, DocumentsViewSet, RepositoriesViewSet
from .api import Users, Documents, Repositories
from . import views

router = routers.DefaultRouter()
router.register('users', views.getUsers, basename=Users)
router.register('documents', views.saveUsers, basename=Users)
router.register('repositories', views.GetRepositories, basename=Repositories)
router.register('repositories', views.SaveRepositories, basename=Repositories)
router.register('documents', views.SaveDocument, basename=Documents)
#router.register('repositories', RepositoriesViewSet)

urlpatterns = [
    path('users/', views.getUsers),
    path('repositories/', views.GetRepositories),
    path('create/users/', views.saveUsers),
    path('create/repositories/', views.SaveRepositories),
    path('create/documents/', views.SaveDocument),
]
