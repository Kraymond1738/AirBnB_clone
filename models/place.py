#!/usr/bin/python3
"""the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    this file contains the city_id
    user_id, name, description, number_rooms
    number_bathrooms, max_guest, price_by_night
    latitude, logitude and amenity_id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
