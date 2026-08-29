from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, PointTransaction

@receiver(post_save, sender=Order)
def handle_order_points(sender, instance, created, **kwargs):
    if not created and instance.status == 'Completed' and instance.points_earned == 0:
        earned_points = int(instance.total_price / 10)
        
        instance.points_earned = earned_points
        instance.customer.points_balance += earned_points
        instance.customer.total_spent += instance.total_price
        instance.customer.visits_count += 1
        
        instance.customer.save()
        instance.save()
        
        PointTransaction.objects.create(
            customer=instance.customer,
            order=instance,
            points=earned_points,
            transaction_type='Earned'
        )