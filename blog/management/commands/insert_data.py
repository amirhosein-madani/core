from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from ...models import Post, Category
from random import choice


class Command(BaseCommand):
    help = "creating random users and posts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):

        categories = list(Category.objects.all())

        user = User.objects.create_superuser(
            username=self.fake.user_name(),
            password=self.fake.password(),
            phone_number=self.fake.numerify("############"),
            email=self.fake.email(),
        )

        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.date_of_birth = self.fake.date_of_birth()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for _ in range(10):
            post = Post.objects.create(
                author=profile,
                title=self.fake.sentence(nb_words=6, variable_nb_words=True),
                content=self.fake.paragraph(nb_sentences=10),
                status=choice([True, False]),
                published_date=self.fake.date_time_this_year(),
            )

            post.category.add(choice(categories))
