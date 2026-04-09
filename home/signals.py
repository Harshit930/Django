from django.db.models.signals import pre_save
from django.db.models.signals import post_save


from django.dispatch import receiver

from .models import Student


@receiver(pre_save, sender=Student)

def before_save(sender, instance, **kwargs):

    print("Data save hone se pehle signal run hua")

    instance.name = instance.name.upper()
    
# Student.objects.create(name="ayushman", age=22)


@receiver(post_save, sender=Student)

def after_save(sender, instance, created, **kwargs):

    if created:

        print("New student add hua")

    else:

        print("Student update hua")