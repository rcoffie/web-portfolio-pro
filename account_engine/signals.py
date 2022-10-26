from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
user = User
import logging, traceback
logger = logging.getLogger('django')

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.warning(f" {user.username} loggin through page {request.META.get('HTTP_REFERER')} ")


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logger.warning(" failed login attempt  ")



@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.warning(f" {user.username} logged out through {request.META.get('HTTP_REFERER')} ")
