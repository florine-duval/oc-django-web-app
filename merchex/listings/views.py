from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def listing_list(request):
    all_listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': all_listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def contact(request):
    form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})