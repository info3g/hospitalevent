from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
import mysite.models
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from ckeditor.fields import RichTextField
# Create your models here.
class blogpost(models.Model):
    title = models.CharField(max_length=140)
    body = RichTextField()
    date = models.DateTimeField()
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=200,default="")
    category = models.ForeignKey(mysite.models.diseases, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="blog/images", default= 'blog/images/news-newsletter-newspaper-information-158651_5PJlC13.png')
    thumbnail = models.ImageField(upload_to="blog/images", default= 'blog/images/news-newsletter-newspaper-information-158651_5PJlC13.png', null=True, blank=True,editable=False)

    __original_name = None

    def __init__(self, *args, **kwargs):
        super(blogpost, self).__init__(*args, **kwargs)
        self.__original_name = self.image
    def save(self):
        if self.image != self.__original_name:

            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            width, height = im.size

            ImageOps.fit(im, [1920, 1080], Image.ANTIALIAS)

            # after modifications, save it to the output
            im.save(output, format='png', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            super(blogpost, self).save()
            try:
                thumb = Image.open(self.image)
            except:
                pass


            output = BytesIO()

            # Resize/modify the image
            width, height = thumb.size


            thumb = ImageOps.fit(thumb, [300,200], Image.ANTIALIAS)

            # after modifications, save it to the output
            thumb.save(output, format='png', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.thumbnail = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.thumbnail.name.split('.')[0], 'image/jpeg',
                                              sys.getsizeof(output), None)

        super(blogpost, self).save()
        self.__original_name = self.image
    def __str__(self):
        return self.title