from django.urls import path, include
from rest_framework import routers
from .views import HabitList, HabitDetail
    # HabitViewSet, JournalViewSet, BonusViewSet


# router = routers.DefaultRouter()
# router.register(r'habits', HabitViewSet)
# router.register(r'journals', JournalViewSet)
# router.register(r'bonuses', BonusViewSet)
# from .views import HabitList, HabitDetail


urlpatterns = [
    # path('', include(router.urls))
    path('', HabitList.as_view()),
    path('<int:pk>/', HabitDetail.as_view()),
]