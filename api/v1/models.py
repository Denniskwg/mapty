from django.db import models
from django.contrib.gis.db.models import PointField
import uuid

# Create your models here.
class CustomUserManager(models.Manager):
    def create_user(self, email, first_name, last_name, password, user_name):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            user_name=user_name
        )
        user.set_password(password)
        user.save()
        return user


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        abstract = True

class User(BaseModel):
    email = models.CharField(max_length=60, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=60, null=False, blank=False)
    user_name = models.CharField(max_length=60, null=False, blank=False)
    objects = CustomUserManager()

class Workout(BaseModel):
    coords_start = PointField()
    coords_end = PointField()
    type = models.CharField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', related_name='workouts', null=False, blank=False)

class Demo(BaseModel):
    type = models.CharField(max_length=60, null=False, blank=False)
    coords_start = PointField()
    coords_end = PointField()
    name = models.CharField(max_length=60, null=False, blank=False)
