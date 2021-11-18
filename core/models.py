from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.db.models.signals import (post_save, post_delete)

# Create your models here.
class Car(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  plate = models.CharField(max_length=100)
  number_of_tables = models.IntegerField(default=1)
  year = models.CharField(max_length=100, blank=True)
  brand = models.CharField(max_length=100, blank=True)
  color = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return "{}/{}".format(self.owner.username, self.plate)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(unique=True, db_index=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField('active', default=True)
    is_admin = models.BooleanField('admin', default=False)

    USERNAME_FIELD = 'email'

    ordering = ('created',)

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return u'Profile of user: {0}'.format(self.user.email)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
post_delete.connect(delete_user, sender=Profile)