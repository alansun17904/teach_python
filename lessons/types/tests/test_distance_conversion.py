from .context import DistanceConversion as Distance


def test_distance_converison_km_to_miles():
    assert Distance.distance_conversion_km_to_miles(50) == 31.06
    assert Distance.distance_conversion_km_to_miles(45) == 27.95
    assert Distance.distance_conversion_km_to_miles(1) == 0.62
    assert Distance.distance_conversion_km_to_miles(1.61) == 1
    assert Distance.distance_conversion_km_to_miles(64.91) == 40.32
    assert Distance.distance_conversion_km_to_miles(0) == 0

