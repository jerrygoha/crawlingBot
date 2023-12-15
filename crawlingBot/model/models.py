from django.core.serializers import serialize
from django.db import models
from django.utils import timezone

# Create your models here.
# Model에는 id필드가 자동으로 추가된다

class contentsLog(models.Model):
    contents_webUrl = models.URLField                               #웹페이지 url
    contents_webDomain = models.TextField                           #웹페이지 도메인

    contents_gallnum = models.BigIntegerField(default=0)            #(디시전용) 글 번호, 중복가능
    contents_gallwriter = models.TextField(default="unknown")       #(디시전용) 글 작성자, 중복가능

    contents_mediaUrl = models.URLField                             #컨텐츠 url
    contents_filenameExtension = models.TextField                   #확장자

    contents_isDownloaded = models.BooleanField(default=False)      #다운로드 완료 여부
    contents_isTelegramSend = models.BooleanField(default=False)    #텔레그램 전송완료 여부
    contents_date = models.DateTimeField("logging post_date")       #로그 time check

