from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Habit, Journal, Bonus
from .permissions import IsAuthorOrReadOnly
from .serializers import HabitSerializer, JournalSerializer, BonusSerializer


class HabitList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

# class HabitViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()

    # def get_queryset(self):
    #     return Habit.objects.filter(user=self.request.user)

#
# class JournalViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = JournalSerializer
#
#     def get_queryset(self):
#         return Journal.objects.filter(user=self.request.user)
#
#
# class BonusViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BonusSerializer
#
#     def get_queryset(self):
#         return Bonus.objects.filter(user=self.request.user)
