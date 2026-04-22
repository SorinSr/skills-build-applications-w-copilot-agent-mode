from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        run = Activity.objects.create(name='Running')
        walk = Activity.objects.create(name='Walking')
        strength = Activity.objects.create(name='Strength Training')

        # Create Workouts
        for user in users:
            Workout.objects.create(user=user, activity=run, duration=30, points=50)
            Workout.objects.create(user=user, activity=walk, duration=20, points=20)
            Workout.objects.create(user=user, activity=strength, duration=15, points=30)

        # Create Leaderboard
        for team in [marvel, dc]:
            Leaderboard.objects.create(team=team, points=Workout.objects.filter(user__team=team).aggregate_sum('points'))

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
