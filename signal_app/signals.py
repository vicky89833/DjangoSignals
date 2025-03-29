from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Book
import threading
import time

@receiver(pre_save, sender=Book)
def before_book_save(sender, instance, **kwargs):
    print("\n--- PRE_SAVE SIGNAL ---")
    print(f"Book '{instance.title}' is about to be saved")
    print(f"Running in thread: {threading.current_thread().name}")

@receiver(post_save, sender=Book)
def after_book_save(sender, instance, created, **kwargs):
    print("\n--- POST_SAVE SIGNAL ---")
    print(f"Book '{instance.title}' was just saved (Created: {created})")
    print(f"Running in thread: {threading.current_thread().name}")
    time.sleep(2)  # Simulate slow operation (proves synchronous behavior)
    print("Signal handler completed!")



import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def check_thread(sender, instance, **kwargs):
    current_thread = threading.current_thread()
    print("\n--- SIGNAL THREAD INFO ---")
    print(f"Signal running in thread: {current_thread.name} (ID: {current_thread.ident})")






from django.db import connection

@receiver(post_save, sender=Book)
def check_transaction(sender, instance, **kwargs):
    print(f"In transaction? {connection.in_atomic_block}") 
     # True if inside atomic block
