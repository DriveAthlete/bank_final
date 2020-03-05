from django.test import SimpleTestCase
from django.urls import resolve, reverse

from transfer.transfer_views.transferListView import TransferListView
from transfer.transfer_views.TransferCreate import TransferCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_resolve(self):
        url = reverse('transfer_list')
        self.assertEquals(resolve(url).func.view_class, TransferListView)

    def test_create_url_resolve(self):
        url = reverse('transfer_create')
        self.assertEquals(resolve(url).func.view_class, TransferCreateView)
