import pytest

from apps.measurement.models import Country


@pytest.mark.django_db
def test_country(country):
    """"""
    assert isinstance(country, Country)


@pytest.mark.django_db
@pytest.mark.parametrize("country__full_name", ["Turkey"])
def test_country_full_name(country):
    """"""
    assert country.full_name == "Turkey"


@pytest.mark.django_db
@pytest.mark.parametrize("country__code", ["MG"])
def test_country_code(country):
    """"""
    assert country.code == "MG"


@pytest.mark.django_db
def test_no_equil_country_fullname_two_country(first_country, second_country):
    """"""
    assert first_country.full_name != second_country.full_name


@pytest.mark.django_db
def test_no_equil_country_code_two_country(first_country, second_country):
    """"""
    assert first_country.code != second_country.code
