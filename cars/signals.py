from django.db.models.signals import pre_delete,pre_save, post_delete,post_save
from django.dispatch import receiver
from cars.models import Car , Car_Inventory
from django.db.models import Sum


def Car_Inventory_Update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    Car_Inventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )    
    
    
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    Car_Inventory_Update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    Car_Inventory_Update()