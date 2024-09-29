# signals.py

from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from .models import UserProfile
import cloudinary.uploader

@receiver(social_account_added)
def get_google_profile_picture(request, sociallogin, **kwargs):
    if sociallogin.provider == 'google':
        # Get user's profile information
        user_data = sociallogin.account.extra_data

        # Get the profile picture URL
        profile_picture_url = user_data.get('picture')

        if profile_picture_url:
            # Upload the image to Cloudinary
            result = cloudinary.uploader.upload(profile_picture_url)
            cloudinary_url = result['url']

            # Create or update the user profile
            user_profile, created = UserProfile.objects.get_or_create(user=sociallogin.user)
            user_profile.pfp = cloudinary_url  # Save the Cloudinary URL
            user_profile.save()
