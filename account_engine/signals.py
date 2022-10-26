from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging, traceback
logger = logging.getLogger('django')

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.warning(f" {user.username} loggin through page {request.META.get('HTTP_REFERER')} ")


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logger.warning(f" {user.username} failed to log in through page {request.META.get('HTTP_REFERER')} ")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.warning(f" {user.username} logged out through {request.META.get('HTTP_REFERER')} ")
