from django.test import TestCase

from django.contrib.auth.models import User


from .models import Habit


class HabitTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        #Create new Habit
        test_habit = Habit.objects.create(
            owner=testuser1, name='Running 10K', description='Run run')
        test_habit.save()

        def test_habit_content(self):
            habit = Habit.objects.get(id=1)
            expected_owner = f'{habit.owner}'
            expected_name = f'{habit.name}'
            expected_description = f'{habit.description}'
            self.assertEqual(expected_owner, 'testuser1')
            self.assertEqual(expected_name, 'Running 10K')
            self.assertEqual(expected_description, 'Run run')

