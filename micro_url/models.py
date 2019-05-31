from django.db import models


class URLService(models.Model):
    """
    Given a long url, this will create a new short url from a generated id
    """
    original_url = models.CharField(max_length=255, help_text='Old Long URL.')
    new_url = models.CharField(max_length=255, help_text='New Shorty URL.')
    unique_id = models.CharField(max_length=55, help_text='Unique ID', primary_key=True)
    count = models.IntegerField(help_text='Number of times used')
    create_date = models.DateTimeField(auto_now_add=True, help_text='Timestamp when the URL was created (automatically set, ISO format).')
    edit_date = models.DateTimeField(auto_now=True, help_text='Timestamp when the URL was last modified (automatically set, ISO format).')

    def save(self, *args, **kwargs):
        from time import time
        # onsave add unique id
        self.unique_id = hex(int(time() * 10000000))[2:]
        super(URLService, self).save(*args, **kwargs)
