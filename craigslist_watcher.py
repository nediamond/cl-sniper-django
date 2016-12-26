# Based on code at https://github.com/nediamond/craigslist-sniper
import time, datetime, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sniper.settings")
import django
django.setup()
from sniper.models import *
from craigslist import CraigslistForSale
from django.core.mail import EmailMessage


def run():
    for sniper in CLSniper.objects.filter(active=True):
        query = CraigslistForSale(site=sniper.site, filters={ 'search_titles': sniper.search_titles,
                                                               'query': sniper.query,
                                                               'min_price': sniper.min_price,
                                                               'max_price': sniper.max_price})
        results = query.get_results(limit=10, sort_by='newest')
        for result in results:
            if not Hit.objects.filter(sniper=sniper, post_id=result['id']).exists():
                try:
                    price=result['price'][1:]
                except TypeError:
                    price=0
                new_hit = Hit(sniper=sniper,
                              post_name=result['name'],
                              price=price,
                              url=result['url'],
                              post_id=result['id'],
                              date=result['datetime'])
                new_hit.save()

                # Only sending new post alerts for posts from within last 12 hours
                if (datetime.datetime.now() - datetime.datetime.strptime(new_hit.date, '%Y-%m-%d %H:%M')
                        < datetime.timedelta(hours=2)):
                    send_email_alert(new_hit)
        time.sleep(5)


def send_email_alert(hit):
    try:
        message = """New CL Listing Matches query \"{0}\":\n\n\t{1}\n\n\tPrice: ${2}\n\n\t{3}\n\n\tPosted: {4}
                    \n\nTurn off notifications at http://cl-sniper.com by setting this sniper to inactive.""".format(hit.sniper.query,
                                                                                                                hit.post_name,
                                                                                                                hit.price,
                                                                                                                hit.url,
                                                                                                                hit.date)
        email = EmailMessage("CL Sniper Hit for {0}".format(hit.sniper.owner),
                             message,
                             to=[hit.sniper.owner.email])
        email.send()
    except Exception as e:
        print "**Email Alert Error**"
        print "Time:", datetime.datetime.now()
        print "Hit ID:", hit.id
        print e
        print


if __name__=="__main__":
    run()
