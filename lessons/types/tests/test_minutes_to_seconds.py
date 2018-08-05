from lessons.types.src.minutes_to_seconds import MinutesAndSecondsToSeconds as Minute


def test_minutes_to_seconds():
    assert Minute.minutes_to_seconds(3, 0) == 180
    assert Minute.minutes_to_seconds(5, 10) == 310
    assert Minute.minutes_to_seconds(10, 68) == 668
    assert Minute.minutes_to_seconds(85, 30) == 5130
    assert Minute.minutes_to_seconds(3, 396) == 576
    assert Minute.minutes_to_seconds(0, 0) == 0
