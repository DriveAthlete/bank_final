from django.urls import path

from transfer.transfer_views.transferListView import TransferListView
from transfer.transfer_views.TransferCreate import TransferCreateView

urlpatterns = [
    path('list/', TransferListView.as_view()),
    path('', TransferCreateView.as_view(), name='transfer_create')
]
