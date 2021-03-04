from random import sample
from src.theater_seating import TheaterSeating

def verify_seating(seating, seats):
    for row, left, right in seats:
        restrictions = []
        left_offset = left
        right_offset = right
        for _ in range(3):
            if left_offset - 1 >= 0:
                left_offset -= 1
            if right_offset + 1 < 20:
                right_offset += 1
        restrictions.append((row, left_offset, left))
        restrictions.append((row, right, right_offset))
        row_up, row_down = seating.shift_up(row), seating.shift_down(row)
        if row_up in seating:
            restrictions.append((row_up, left, right))
        if row_down in seating:
            restrictions.append((row_down, left, right))
        for restriction in restrictions:
            row, left, right = restriction
            if any([seating.is_available(seat) for seat in seating[row][left:right]]):
                return False

    return True

def test_1():
    seats = []
    inputs = sample(range(1, 9), 5)
    seating = TheaterSeating(inputs)
    for section, row in seating.items():
        flag = False
        for i, seat in enumerate(row):
            if seat == "reserved" and not flag:
                start = i
                flag = True
            elif flag and seat != "reserved":
                stop = i
                flag = False
                seats.append((section, start, stop))

    assert verify_seating(seating, seats)

def test_2():
    seats = []
    inputs = sample(range(1, 9), 5)
    seating = TheaterSeating(inputs)
    for section, row in seating.items():
        flag = False
        for i, seat in enumerate(row):
            if seat == "reserved" and not flag:
                start = i
                flag = True
            elif flag and seat != "reserved":
                stop = i
                flag = False
                seats.append((section, start, stop))

    assert verify_seating(seating, seats)

def test_3():
    seats = []
    inputs = sample(range(1, 9), 5)
    seating = TheaterSeating(inputs)
    for section, row in seating.items():
        flag = False
        for i, seat in enumerate(row):
            if seat == "reserved" and not flag:
                start = i
                flag = True
            elif flag and seat != "reserved":
                stop = i
                flag = False
                seats.append((section, start, stop))

    assert verify_seating(seating, seats)

def test_4():
    seats = []
    inputs = sample(range(1, 9), 5)
    seating = TheaterSeating(inputs)
    for section, row in seating.items():
        flag = False
        for i, seat in enumerate(row):
            if seat == "reserved" and not flag:
                start = i
                flag = True
            elif flag and seat != "reserved":
                stop = i
                flag = False
                seats.append((section, start, stop))

    assert verify_seating(seating, seats)

def test_5():
    seats = []
    inputs = sample(range(1, 9), 5)
    seating = TheaterSeating(inputs)
    for section, row in seating.items():
        flag = False
        for i, seat in enumerate(row):
            if seat == "reserved" and not flag:
                start = i
                flag = True
            elif flag and seat != "reserved":
                stop = i
                flag = False
                seats.append((section, start, stop))

    assert verify_seating(seating, seats)
