from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from librarian.models import BorrowingRecord

class Command(BaseCommand):
    help = 'Send overdue reminders'

    def handle(self, *args, **kwargs):
        overdue_records = BorrowingRecord.objects.filter(
            return_date__isnull=True,
            due_date__lt=timezone.now()
        )
        for record in overdue_records:
            send_mail(
                'Overdue Book Reminder',
                f'Please return "{record.book.title}" as soon as possible.',
                'library@example.com',
                [record.member.user.email],
                fail_silently=False,
            )