from django.urls import path

from transfer.transfer_views.transferListView import TransferListView

urlpatterns = [
    path('', TransferListView.as_view()),

]
