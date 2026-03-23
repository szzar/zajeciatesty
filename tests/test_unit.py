import pytest

from pydantic import ValidationError
from src.models import Apartment, Tenant



def test_tenant_fields():
    data = Tenant(
        name="tenant-test",
        apartment="Test Apartment",
        room="Test Room",
        rent_pln=100.0,
        deposit_pln=150.0,
        date_agreement_from="Test Date From",
        date_agreement_to="Test Date To"
    )
    assert data.name == "tenant-test"
    assert data.apartment == "Test Apartment"
    assert data.room == "Test Room"
    assert data.rent_pln == 100.0
    assert data.deposit_pln == 150.0
    assert data.date_agreement_from == "Test Date From"
    assert data.date_agreement_to == "Test Date To"

def test_tenant_from_dict():
    data = {
        "name":"tenant-test",
        "apartment":"Test Apartment",
        "room":"Test Room",
        "rent_pln": 100.0,
        "deposit_pln":150.0,
        "date_agreement_from":"Test Date From",
        "date_agreement_to":"Test Date To"
    }
    tenant = Tenant(**data)
    assert tenant.name == data["name"]
    assert tenant.apartment == data["apartment"]
    assert tenant.room == data["room"]
    assert tenant.rent_pln == data["rent_pln"]
    assert tenant.deposit_pln == data["deposit_pln"]
    assert tenant.date_agreement_from == data["date_agreement_from"]
    assert tenant.date_agreement_to == data["date_agreement_to"]

    data['rent_pln'] = "string"
    with pytest.raises(ValidationError):
        Tenant(**data)



def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2 # if assert==3 :, f"Oczekiwano 3 mieszkań, ale znaleziono {len(data.rooms)}"


def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)
