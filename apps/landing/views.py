from django.shortcuts import render_to_response
from django.utils.datetime_safe import datetime

COMPANY_NAME = 'Aptitude World ANZ'
META_KEYWORDS = ['Aptitude World AU', 'Aptitude World NZ', 'Aptitude World Australia', 'Aptitude World New Zealand']


def index(request):
    title = COMPANY_NAME + ' - ' + 'Home'
    keywords = ','.join(META_KEYWORDS)
    description = ','.join(META_KEYWORDS)
    year = datetime.now().year
    return render_to_response('landing/index.html',
                              {
                                  'title': title,
                                  'keywords': keywords,
                                  'description': description,
                                  'page': 'index',
                                  'year': year,
                              }
    )


def product(request):
    title = COMPANY_NAME + ' - ' + 'Product'
    keywords = ','.join(META_KEYWORDS)
    description = ','.join(META_KEYWORDS)
    year = datetime.now().year
    return render_to_response('landing/product.html',
                              {
                                  'title': title,
                                  'keywords': keywords,
                                  'description': description,
                                  'page': 'product',
                                  'year': year,
                              }
    )


def solutions(request):
    title = COMPANY_NAME + ' - ' + 'Solutions'
    keywords = ','.join(META_KEYWORDS)
    description = ','.join(META_KEYWORDS)
    year = datetime.now().year
    return render_to_response('landing/solutions.html',
                              {
                                  'title': title,
                                  'keywords': keywords,
                                  'description': description,
                                  'page': 'solutions',
                                  'year': year,
                              }
    )


def consulting(request):
    title = COMPANY_NAME + ' - ' + 'Consulting'
    keywords = ','.join(META_KEYWORDS)
    description = ','.join(META_KEYWORDS)
    year = datetime.now().year
    return render_to_response('landing/consulting.html',
                              {
                                  'title': title,
                                  'keywords': keywords,
                                  'description': description,
                                  'page': 'consulting',
                                  'year': year,
                              }
    )