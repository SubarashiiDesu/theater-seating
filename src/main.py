from sys import argv
from theater_seating import TheaterSeating


if __name__ == '__main__':
    if len(argv) == 2 and ".in" in argv[1]:
        seating = TheaterSeating(argv[1])
        seating.show_table()
        seating.export_out()
    elif len(argv) > 1 and all(arg.isnumeric() for arg in argv[1:]):
        seating = TheaterSeating([int(arg) for arg in argv[1:]])
        seating.show_table()
    else:
        seating = TheaterSeating()
        seating.show_table()
