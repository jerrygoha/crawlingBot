# 크롤링 로직

import time
import os
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render
from crawlingApp.model.crawlingDCModels import CrawlingLog, ImageFile


def download_and_save_image(image_url, log):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        # 이미지를 다운로드하여 ImageFile 모델에 저장
        image_file = ImageFile()
        image_file.file.save(os.path.basename(image_url), response.raw)
        image_file.save()
        # CrawlingLog 모델과 연결
        log.image_files.add(image_file)


def crawl_and_log(gallery_id):
    gallery_url = f'https://gall.dcinside.com/board/lists/?id={gallery_id}'
    response = requests.get(gallery_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = [img['src'] for img in soup.find_all('img', class_='img_thumb')]

        # 로그 기록
        log = CrawlingLog.objects.create(gallery_id=gallery_id, images=images)
        log.save()

        # 이미지 다운로드 및 로컬에 저장
        for image_url in images:
            download_and_save_image(image_url, log)

        return {'success': True, 'log_id': log.id, 'images': images}

    return {'success': False, 'error': 'Failed to fetch gallery content.'}


def start_crawling(request, gallery_id):
    # 이 부분에서 크롤링을 시작하도록 로직을 추가
    # 크롤링은 백그라운드에서 주기적으로 실행되어야 하며, 중복 실행을 방지하는 메커니즘이 필요함
    return JsonResponse({'success': True})


def stop_crawling(request):
    # 이 부분에서 크롤링을 멈추도록 로직을 추가
    return JsonResponse({'success': True})


def get_logs(request):
    logs = CrawlingLog.objects.all()
    return render(request, 'logs.html', {'logs': logs})