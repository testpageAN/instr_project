import datetime
from datetime import timedelta


# Update next_check date and delta_days
def update_next_check(listings):
    for listing in listings:
        listing.next_check = listing.last_checked + timedelta(days=listing.interval)
        listing.delta_days = (listing.next_check.date() - datetime.date.today()).days

    return listings