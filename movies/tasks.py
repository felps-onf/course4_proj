from celery import shared_task
from django.core.mail import mail_admins
from movies import omdb_integration

@shared_task
def search_and_save(search):
    print("test")
    return omdb_integration.search_and_save(search)



@shared_task
def notify_of_new_search_term(search_term):
    mail_admins("New Search Term", f"A new search term was used: '{search_term}'")
