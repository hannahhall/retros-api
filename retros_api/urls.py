from django.urls import include, path
from rest_framework.routers import DefaultRouter
from retros_api.views import CardViewSet, CohortViewSet, RetroViewSet, StudentViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'cards', CardViewSet)
router.register(r'cohorts', CohortViewSet)
router.register(r'retros', RetroViewSet, 'retro')
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
