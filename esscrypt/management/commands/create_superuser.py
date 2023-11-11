import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser from environment variables'

    def handle(self, *args, **options):
        admin_username = os.environ.get('DJANGO_ADMIN_USERNAME')
        admin_email = ''  # Optionally set an admin email here
        admin_password = os.environ.get('DJANGO_ADMIN_PASSWORD')

        if admin_username and admin_password:
            User = get_user_model()
            if not User.objects.filter(username=admin_username).exists():
                User.objects.create_superuser(admin_username, admin_email, admin_password)
                self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
