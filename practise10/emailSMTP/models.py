from django.db import models


# Create your models here.
class SmtpMailModel(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    # attachment = models.FileField(null=True)

    class Meta:
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'

    def __str__(self):
        return f"{self.sender}"

    def delete(self, *args, **kwargs):
        self.attachment.delete()
        super().delete(*args, **kwargs)
