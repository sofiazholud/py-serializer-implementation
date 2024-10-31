from car.models import Car
import json
from car.serializers import CarSerializer

def serialize_car_object(car):
    serializer = CarSerializer(car)
    data = serializer.data
    # Add the id field if it exists on the Car object
    if hasattr(car, 'id'):
        data['id'] = car.id
    return json.dumps(data)

def deserialize_car_object(json_data):
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError("Invalid data for Car object")
