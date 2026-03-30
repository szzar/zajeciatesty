from src.models import Apartment
from src.manager import Manager
from src.models import Parameters



def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_tenant_names():
    parameters = Parameters()
    manager = Manager(parameters)

    names =[
        "Jan Nowak",
        "Adam Kowalski",
        "Ewa Adamska",
    ]
    for tenant in manager.tenants.values():
        assert tenant.name in names

def test_tenant_assigned_apartment():
    parameters = Parameters()
    manager = Manager(parameters)
    assert manager.validate_tenant_apartments() is True

    manager.tenants["tenant-1"].apartment = "apartament-fgdjskjf" #apartment-fgdjskjf nie istnieje w apartments
    assert manager.validate_tenant_apartments() is False