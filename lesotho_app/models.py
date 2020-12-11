from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Client Profile'


class Claims(models.Model):
    claimant = models.ForeignKey(User, on_delete=models.CASCADE)
    claimant_title = models.CharField(max_length=500)
    claimant_first_name = models.CharField(max_length=500)
    claimant_last_name = models.CharField(max_length=500)
    claimant_phone_number = models.CharField(max_length=500)
    claimant_policy_number = models.CharField(max_length=500)
    claimant_email = models.CharField(max_length=500)
    claimant_id_number = models.CharField(max_length=500)
    claimant_passport_number = models.CharField(max_length=500)
    claimant_physical_address = models.CharField(max_length=500)
    claimant_postal_address = models.CharField(max_length=500)
    claimant_age = models.CharField(max_length=500)
    claimant_relationship = models.CharField(max_length=500)

    deceased_title = models.CharField(max_length=500)
    deceased_first_name = models.CharField(max_length=500)
    deceased_last_name = models.CharField(max_length=500)
    deceased_date_of_birth = models.CharField(max_length=500)
    deceased_place_of_birth = models.CharField(max_length=500)
    deceased_gender = models.CharField(max_length=500)
    deceased_date_of_death = models.CharField(max_length=500)
    deceased_time_of_death = models.CharField(max_length=500)
    deceased_age_of_death = models.CharField(max_length=500)
    deceased_cause_of_death = models.CharField(max_length=500)
    deceased_place_of_death = models.CharField(max_length=500)
    deceased_passport_number = models.CharField(max_length=500)
    deceased_id_number = models.CharField(max_length=500)
    deceased_marital_status = models.CharField(max_length=500)
    deceased_physical_address = models.CharField(max_length=500)
    deceased_postal_address = models.CharField(max_length=500)

    # image = models.ImageField(upload_to='service_images/', blank=False)
    # price = models.IntegerField(default=0)
    def __str__(self):
        return self.claimant

