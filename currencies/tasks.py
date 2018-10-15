from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(name='update_currency_rates')
def update_currency_rates():
    print('update_currency_rates')
    return 1