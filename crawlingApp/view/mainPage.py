from django.shortcuts import render
from crawlingApp.model import adminpageModels


def admin_main(request):
    adminpageModelObj = adminpageModels.models.__all__()

    return render(request, 'admin_mainPage.html', {adminpageModelObj : adminpageModelObj})