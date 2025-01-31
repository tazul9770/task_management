from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_activation_mail(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_urls = f"{settings.FRONTEND_URLS}/users/activate/{instance.id}/{token}/"
        subject = "Activate Your acount"
        message = f"{instance.username}\n\nPlease activate your acount by clicking the link blow:\n{activation_urls}\n\nThank you"
        recipient_list = [instance.email]
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        except Exception as e:
            print(f"Fail to send mail to {instance.email}:{str(e)}")

@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='User')
        instance.groups.add(user_group)
        instance.save()


