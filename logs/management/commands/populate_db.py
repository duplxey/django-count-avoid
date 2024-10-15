from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from logs.models import Log
from utils.progress_bar_util import print_progress_bar


class Command(BaseCommand):
    help = "Populates the database with sample data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--amount", type=int, help="The number of logs that should be created."
        )

    def handle(self, *args, **options):
        fake = Faker()
        amount = options["amount"] if options["amount"] else 2_500_000

        # Create the superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "", "password")

        # Create `amount` of logs
        print("Starting the database population process. This might take a while...")
        bulk_count = 2_500
        count = 0
        while count < amount:
            print_progress_bar(count, amount + 1)
            logs = [
                Log(
                    level=fake.random_element(elements=("i", "w", "e")),
                    message=fake.paragraph(nb_sentences=1, variable_nb_sentences=False),
                )
                for _ in range(bulk_count)
            ]
            Log.objects.bulk_create(logs)
            count += bulk_count

        print("")
        print("Successfully populated the database.")
