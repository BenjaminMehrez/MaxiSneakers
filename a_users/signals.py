from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from .models import Profile
from a_payment.models import ShippingAddress

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            email=user.email
        )
        ShippingAddress.objects.create(
            user=user,
            shipping_email=user.email
        )
    else:
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email
        profile.save()
            
        shipping_address = get_object_or_404(ShippingAddress, user=user)
        shipping_address.shipping_email = user.email
        shipping_address.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()


@receiver(post_save, sender=Profile)
def update_account_email(sender, instance, created, **kwargs):
    profile = instance
    if not created:
        try:
            email_address = EmailAddress.objects.get_primary(profile.user)
            if email_address.email != profile.email:
                email_address.email = profile.email
                email_address.verified = False
                email_address.save()
        except:
            pass