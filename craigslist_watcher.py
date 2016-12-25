# Based on code at https://github.com/nediamond/craigslist-sniper
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sniper.settings")
import django
django.setup()
from sniper.models import *
from craigslist import CraigslistForSale


for sniper in CLSniper.objects.filter(active=True):
    query = CraigslistForSale(site=sniper.site, filters={'search_titles': True,
                                                           'query': sniper.query,
                                                           'min_price': sniper.min_price,
                                                           'max_price': sniper.max_price})
    results = query.get_results(limit=5, sort_by='newest')
    for result in results:
        if not Hit.objects.filter(sniper=sniper, post_id=result['id']).exists():
            # TODO: Replace this with a Hit.objects.new_hit(..) method which sends notifications
            try:
                price=result['price'][1:]
            except TypeError:
                price=0
            Hit(sniper=sniper,
                post_name=result['name'],
                price=price,
                url=result['url'],
                post_id=result['id'],
                date=result['datetime']).save()
    time.sleep(5)
