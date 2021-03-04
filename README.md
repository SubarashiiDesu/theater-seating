# Movie Theater Seating Optimizer 🎥 🎥 🎥

Optimizes seating placement for best satisfaction using BFS and prioritizing the middle, while taking into account social distancing!

## Requirements

python 3.6.1 or later

rich (library for rich text and terminal formatting)

```bash
pip install rich
```

## Usage

cd to root directory ( /theater-seating ) and run the run script with:

```bash
./run argv
```

where the optional argv arguements can be a path to an input file with the extension ".in" or a sequence of numbers representing the reservations in order.

No arguements (constructs an empty TheaterSeating class with no seats assigned yet)

```bash
./run
```

Sequence of numbers (constructs the TheaterSeating class by passing it the sequence of numbers as a list)

```bash
./run 2 4 4 3
```

Input File (constructs the TheaterSeating class using the input file)

```bash
./run reservations1.in # Assuming reservations1.in is in the same folder as run script.
```

![Demo](https://media0.giphy.com/media/EVN6jeOEK3PIz7ze4e/giphy.gif)

The run script executes a simple main.py as the entry point and enables interactive mode.
The output file with the seating assignments is automatically generated upon passing an input file (which is not supported with the other 2 modes however).
After the table is generated and shown, the program will just stay in interactive mode until issuing a `quit()` command.
While in interactive mode environment variables may be interacted with. In this case 'seating' is the created TheaterSeating class that has already been created.
You can do commands such as `seating.show_table("reserved")` to highlight reserved seating or replace with "available" to highlight the available seating.
You can view the output file with `seating.show_output()` (if one was generated).
You may also apply more reservations by passing any sequence of numbers to `seating.apply_reservations()`.
(Note that you will have to reload the table with `seating.show_table()` to see the changes take effect.)

## Testing Requirements

pytest

```bash
pip install pytest
```

## Testing Usage

Testing support is included which generates 5 random tests each time by running

```bash
./test
```

This is done by randomly generating a list of 5 numbers from the range of 1 to 9.
The tests pass when there are no occupied seats within 3 seats to the left and right of a given reservation,
as well as the the seats that are directly in font and behind.

![Testing](https://media0.giphy.com/media/0EVkAQVCOyjUmxSaO1/giphy.gif)
