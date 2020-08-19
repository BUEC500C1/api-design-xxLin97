from  weather import get_city_name get_data show_information

import pytest

def airport2city(airport_name):
    # airport_name = input ("Enter the name of the Airport: ")
    city = get_city_name(airport_name)
    data = get_data(city)
    return city

def test():

  assert airport2city("Total Rf Heliport") == "Bensalem"
  assert airport2city("Aero B Ranch Airport") == "Leoti"
  assert airport2city("Lowell Field") == "Anchor point"
  assert airport2city("Epps Airpark") == "Harvest"
  assert airport2city("Newport Hospital & Clinic Heliport") == "Newport"
  assert airport2city("Fulton Airport") == "Alex"