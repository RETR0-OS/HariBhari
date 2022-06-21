from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your models here.


class MailText(models.Model):
    subject = models.TextField()
    message = models.TextField()
    users = User.objects.all()
    send_it = models.BooleanField(default=False) #check it if you want to send your email
    def save(self):
        if self.send_it:
            user_list = []
            for u in self.users:
                user_list.append(u.email)
            send_mail(str(self.subject),
                      str(self.message),
                  'r3tr0.m1ll3r@gmail.com',
                      user_list,
                  fail_silently=False)
    class Meta:
        verbose_name = "Emails to send"
        verbose_name_plural = "Emails to send"
