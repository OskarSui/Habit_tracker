from rest_framework import serializers
from .models import Habit, Journal, Bonus


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        # fields = '__all__'

        fields = ('id', 'name', 'description', 'goal', 'frequency', 'start_date', 'end_date', 'owner', 'created_at')
        owner = serializers.ReadOnlyField(source='owner.username')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'
