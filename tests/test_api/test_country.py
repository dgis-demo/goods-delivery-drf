from django.urls import reverse


class TestCountryEndPoints:
    def test_list_country_view(
            self,
            db,
            country_factory,
            api_client
    ) -> None:
        country_factory.create_batch(10)
        url: str = reverse('measurement:countries-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_filters_list_country_view(
            self,
            db,
            country,
            api_client
    ) -> None:
        url: str = reverse('measurement:countries-list')
        url += f'?full_name_in={country.full_name}'
        response = api_client.get(url)
        assert response.status_code == 200

    # def test_retrieve_country_view(
    #         self,
    #         db,
    #         country_factory,
    #         api_client
    # ) -> None:
    #     country = country_factory()
    #     url: str = reverse(
    #         'measurement:countries-detail', kwargs={'pk': country.id}
    #     )
    #     response = api_client.get(url)
    #     assert response.status_code == 200
