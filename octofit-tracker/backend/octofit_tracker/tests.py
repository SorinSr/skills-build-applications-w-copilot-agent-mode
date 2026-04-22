from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, team)

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test Activity')
        self.assertEqual(str(activity), 'Test Activity')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        activity = Activity.objects.create(name='Test Activity')
        workout = Workout.objects.create(user=user, activity=activity, duration=10, points=5)
        self.assertEqual(workout.duration, 10)
        self.assertEqual(workout.points, 5)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
