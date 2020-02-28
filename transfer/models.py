from django.db import models
from users.models import User


# Create your transfer_models here.
class Transfer(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='from_user',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='to_user',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return f'{str(self.from_user.email)} sent {str(self.amount)} ' \
               f'to {str(self.to_user.email)}'
