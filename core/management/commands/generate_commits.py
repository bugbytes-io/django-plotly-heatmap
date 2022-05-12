import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Repository, Commit

class Command(BaseCommand):
    help = 'Generate commits'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            raise CommandError("Create a superuser before running this command!")

        now = timezone.now()
        previous_year = now - timezone.timedelta(weeks=52)

        # create a repository
        repo = Repository.objects.get_or_create(
            name="The Next Facebook",
            user=user
        )[0]

        repo.created = previous_year
        repo.save()

        # generate commits from one year previous.
        # clear any existing first
        Commit.objects.filter(repository=repo).delete()

        delta = now - previous_year
        
        for n in range(delta.days):
            day = previous_year + timezone.timedelta(days=n)

            # with probability 0.5, skip making any commits
            if random.uniform(0, 1) > 0.5:
                continue

            # create a random number of commits for this day
            num_commits = random.randint(1,10)
            for _ in range(num_commits):
                Commit.objects.create(
                    user=user,
                    repository=repo,
                    created=day,
                    code="print('hello world')"
                )





        
