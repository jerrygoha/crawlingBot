
from django.db import models


class CrawlingLog(models.Model):
    gallery_id = models.CharField(max_length=255)
    images = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 추가: 이미지를 저장하는 필드
    image_files = models.ManyToManyField('ImageFile', related_name='logs', blank=True)

    def __str__(self):
        return f'CrawlingLog {self.id} - Gallery {self.gallery_id}'


class ImageFile(models.Model):
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'ImageFile {self.id}'
