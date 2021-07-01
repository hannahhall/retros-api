from django.urls import include, path
from rest_framework.routers import DefaultRouter
from retros_api.views import CardViewSet, CohortViewSet, RetroViewSet, StudentViewSet
from rest_framework.authtoken import views as auth_token_views


router = DefaultRouter(trailing_slash=False)
router.register(r'cards', CardViewSet)
router.register(r'cohorts', CohortViewSet)
router.register(r'retros', RetroViewSet, 'retro')
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', auth_token_views.obtain_auth_token)
]
