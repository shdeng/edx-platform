"""
Utility functions for third_party_auth
"""

from django.contrib.auth.models import User


def user_exists(details):
    """
    Return True if user with given details exist in the system.

    Arguments:
        details (dict): dictionary containing user infor like email, username etc.

    Returns:
        (bool): True if user with given details exists, `False` otherwise.
    """
    # Send the user to the login page if we already have an
    # account that matches the authentication details.
    user_queryset_filter = {}
    email = details.get('email')
    username = details.get('username')
    if email:
        user_queryset_filter['email'] = email
    elif username:
        user_queryset_filter['username'] = username

    return user_queryset_filter and User.objects.filter(user_queryset_filter).exists()
