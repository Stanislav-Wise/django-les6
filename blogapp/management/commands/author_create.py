from django.core.management.base import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    help = 'Create author'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help="Author name")

    def handle(self, *args, **options):
        first_name = options.get('first_name')
        author = Author(first_name=first_name,
                        last_name='unname',
                        email='user@vk.com',
                        bio='text',
                        b_data='2023-10-23')
        author.save()
        self.stdout.write(f'{author}')

