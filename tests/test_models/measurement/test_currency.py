import pytest

from apps.measurement.models import Country, Currency


@pytest.mark.django_db
def test_currency(currency):
    """"""
    assert isinstance(currency, Currency)


@pytest.mark.django_db
@pytest.mark.parametrize("currency__currency", ["Namibian dollar"])
def test_currency_currency(currency):
    """"""
    assert currency.currency == "Namibian dollar"


@pytest.mark.django_db
@pytest.mark.parametrize("currency__code", ["ARS"])
def test_currency_code(currency):
    """"""
    assert currency.code == "ARS"


@pytest.mark.django_db
def test_no_equil_currency_two_currency(first_currency, second_currency):
    """"""
    assert first_currency.currency != second_currency.currency


@pytest.mark.django_db
def test_no_equil_code_two_currency(first_currency, second_currency):
    """"""
    assert first_currency.code != second_currency.code


@pytest.mark.django_db
def test_has_country_two_currency(first_currency, second_currency):
    """"""
    assert isinstance(first_currency.country, Country)
    assert isinstance(second_currency.country, Country)


@pytest.mark.django_db
def test_no_equil_currency_country_fullname_two_currency(first_currency, second_currency):
    """"""
    assert first_currency.country.full_name != second_currency.country.full_name


@pytest.mark.django_db
def test_no_equil_currency_country_code_two_currency(first_currency, second_currency):
    """"""
    assert first_currency.country.code != second_currency.country.code
