from django.urls import reverse


class TestCurrencyEndPoints:
    def test_list_currency_view(
            self,
            db,
            currency_factory,
            api_client
    ) -> None:
        currency_factory.create_batch(10)
        url: str = reverse('measurement:currencies-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_filters_list_currency_view(
            self,
            db,
            currency,
            api_client
    ) -> None:
        url: str = reverse('measurement:currencies-list')
        url += f'?currency_in={currency.currency}'
        response = api_client.get(url)
        assert response.status_code == 200

    def test_retrieve_currency_view(
            self,
            db,
            currency,
            api_client
    ) -> None:
        url: str = reverse(
            'measurement:currencies-detail', kwargs={'pk': currency.id}
        )
        response = api_client.get(url)
        assert response.status_code == 200
