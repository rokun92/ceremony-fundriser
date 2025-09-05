from django.shortcuts import render, redirect
from .models import Donation
from django.http import HttpResponse
import csv

def index_view(request):
    return render(request, 'donations/index.html')

def donate_view(request):
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('name')
        batch = request.POST.get('batch')
        mobile_bank = request.POST.get('mobile_bank')
        amount = request.POST.get('amount')
        contact = request.POST.get('Contact')
        txn_id = request.POST.get('txn_id')
        
        Donation.objects.create(
            name=name,
            batch=batch,
            mobile_bank=mobile_bank,
            amount=amount,
            contact=contact,
            txn_id=txn_id
        )

        # Redirect to Thank_You page
        return render(request, 'donations/thank_you.html', {'donor_name': name}) 

    return render(request, 'donations/donate.html')



def thank_you_view(request):
    return render(request, 'donations/thank_you.html')


def export_donations_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=donations.csv'
    writer = csv.writer(response)

    # Write header
    writer.writerow(['Name', 'Batch', 'Mobile Bank', 'Amount', 'Contact', 'Transaction ID', 'Created At'])

    # Write data
    for donation in Donation.objects.all():
        writer.writerow([
            donation.name,
            donation.batch,
            donation.mobile_bank,
            donation.amount,
            donation.contact,
            donation.txn_id,
            donation.created_at,
        ])

    return response
