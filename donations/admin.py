from django.contrib import admin
from .models import Donation
from django.http import HttpResponse
import csv

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=donations.csv'
    writer = csv.writer(response)

    # Write header
    writer.writerow(['Name', 'Batch', 'Mobile Bank', 'Amount', 'Contact', 'Transaction ID', 'Created At'])

    # Write data rows
    for donation in queryset:
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

export_as_csv.short_description = "Export Selected Donations to CSV"

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch', 'mobile_bank', 'amount', 'contact', 'txn_id', 'created_at')
    search_fields = ('name', 'batch', 'mobile_bank', 'contact', 'txn_id')
    list_filter = ('contact', 'mobile_bank')
    actions = [export_as_csv]
