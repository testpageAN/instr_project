import datetime
from datetime import timedelta


# Update next_check date and delta_days
def update_next_check(listings):
    for listing in listings:
        listing.next_check = listing.last_checked + timedelta(days=listing.interval)
        listing.delta_days = (listing.next_check.date() - datetime.date.today()).days

    return listings


def update_last_checked(listing):
    listing.last_checked = datetime.date.today()

    return listing


def update_next_check_for_one(listing):
    listing.next_check = listing.last_checked + timedelta(days=listing.interval)
    listing.delta_days = (listing.next_check.date() - datetime.date.today()).days

    return listing


def update_date_appearance(listings):
    for listing in listings:
        listing.last_checked = listing.last_checked.strftime("%d/%m/%Y")
        listing.next_check = listing.next_check.strftime("%d/%m/%Y")

