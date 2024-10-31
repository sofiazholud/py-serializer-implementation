from car.models import Car
import json

from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    return json.dumps(serializer.data)


def deserialize_car_object(json_data):
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError("Invalid data for Car object")
