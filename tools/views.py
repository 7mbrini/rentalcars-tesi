# (C) 2025 Francesco Settembrini

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

import os
import random
from django.contrib.gis.geos import Point

from cars.models import Car


# =============================================================================
def tools_view(request):
    #return HttpResponse("tools")
    return render(request, "tools/tools.html")


# =============================================================================
def tools_create_cars_view(request):

    try:
        create_cars()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    #return HttpResponse("create cars table")
    return HttpResponseRedirect(reverse('tools'))

# =============================================================================
# Genera intego random a 4 cifre e lo aggiunge ad una lista predefinita
# =============================================================================
def generate_unique_four_digit_id(target_list):
    while True:
                                # genera un integer random tra 1000 and 9999 (incluso)
        new_id = random.randint(1000, 9999)

                                # verifica per l'uncita' nella lista
        if new_id not in target_list:
            target_list.append(new_id)
            return new_id


# =============================================================================
# Genera in maniera random un punto geografico in un rettangolo assegnato
# =============================================================================
def generate_random_geopoint(min_lat, min_lon, max_lat, max_lon):

    random_latitude = random.uniform(min_lat, max_lat)
    random_longitude = random.uniform(min_lon, max_lon)

    # Crea un Point usando l'ordine (Lon, Lat)
    # Imposta il riferimento a srid=4326 WGS84 (GPS standard)
    random_point = Point(random_longitude, random_latitude, srid=4326)

    return random_point

# =============================================================================
# Genera e restituisce una lista di autoveicoli
# =============================================================================
def create_cars():

    # Bari city
    #left, bottom: 41.10751446264695, 16.85352562217128
    #right, top: 41.12516739837555, 16.87395332625426

    plates = []
    nCars = 10
    Car.objects.all().delete()

    # 41.1141225305812, 16.85285574900471
    # 41.12503246011228, 16.87363442013302
    minLat = 41.114
    minLon = 16.853
    maxLat = 41.125
    maxLon = 16.873

    # 3 doors cars
    carModels = [
        {'seats': 2, 'doors': 3, 'hourly_rate': 20.0, 'image': 'car_images/ecar_01.jpg', 'range_km': 100},
        {'seats': 2, 'doors': 3, 'hourly_rate': 25.0, 'image': 'car_images/ecar_02.jpg', 'range_km': 150},
        {'seats': 2, 'doors': 3, 'hourly_rate': 20.0, 'image': 'car_images/ecar_03.jpg', 'range_km': 150},
        {'seats': 2, 'doors': 3, 'hourly_rate': 25.0, 'image': 'car_images/ecar_04.jpg', 'range_km': 100},
        {'seats': 2, 'doors': 3, 'hourly_rate': 20.0, 'image': 'car_images/ecar_05.jpg', 'range_km': 150},
    ]

    for i in range(0, nCars):
        randModel = carModels[random.randint(0, len(carModels)-1)]

        TheCar = Car()
        TheCar.license_plate = f'BA{generate_unique_four_digit_id(plates)}'
        TheCar.seats = randModel['seats']
        TheCar.hourly_rate = randModel['hourly_rate']
        TheCar.doors = randModel['doors']
        TheCar.image = randModel['image']
        TheCar.range_km = randModel['range_km']
        TheCar.available = random.choice([True, False])
        TheCar.location = generate_random_geopoint(minLat, minLon, maxLat, maxLon)

        TheCar.save()

    # 5 doors cars
    carModels = [
        {'seats': 4, 'doors': 5, 'hourly_rate': 30.0, 'image': 'car_images/ecar_11.jpg', 'range_km': 300},
        {'seats': 4, 'doors': 5, 'hourly_rate': 35.0, 'image': 'car_images/ecar_12.jpg', 'range_km': 350},
        {'seats': 6, 'doors': 5, 'hourly_rate': 50.0, 'image': 'car_images/ecar_13.jpg', 'range_km': 250},
        {'seats': 4, 'doors': 5, 'hourly_rate': 35.0, 'image': 'car_images/ecar_14.jpg', 'range_km': 300},
        {'seats': 6, 'doors': 5, 'hourly_rate': 50.0, 'image': 'car_images/ecar_15.jpg', 'range_km': 350},
    ]

    for i in range(0, nCars):
        randModel = carModels[random.randint(0, len(carModels)-1)]

        TheCar = Car()
        TheCar.license_plate = f'BA{generate_unique_four_digit_id(plates)}'
        TheCar.seats = randModel['seats']
        TheCar.hourly_rate = randModel['hourly_rate']
        TheCar.doors = randModel['doors']
        TheCar.image = randModel['image']
        TheCar.range_km = randModel['range_km']
        TheCar.available = random.choice([True, False])
        TheCar.location = generate_random_geopoint(minLat, minLon, maxLat, maxLon)

        TheCar.save()

