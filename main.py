from car.models import Car
import json
from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    data = serializer.data
    if hasattr(car, "id"):
        data = {"id": car.id, **data}
    return json.dumps(data)


def deserialize_car_object(json_data):
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car_data = serializer.validated_data
        if "id" in data:
            car_data["id"] = data["id"]
        return Car(**car_data)
    else:
        raise ValueError("Invalid data for Car object")
