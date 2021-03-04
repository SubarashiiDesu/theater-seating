from collections import deque
from pathlib import Path
from string import ascii_uppercase

from rich import print
from rich.syntax import Syntax
from rich.table import Column, Table
from rich.text import Text


class TheaterSeating(dict):
    def __init__(self, input=None):
        super().__init__()
        self.in_filename = None
        self.out_filename = None
        self.available_count = 0
        self.unavailable_count = 0
        self.reserved_count = 0
        self.is_available = lambda seat: (seat != "unavailable" and seat != "reserved")
        self.shift_up = lambda row: chr(ord(row) - 1)
        self.shift_down = lambda row: chr(ord(row) + 1)
        for char in ascii_uppercase[:10]:
            self[char] = ["available" for _ in range(20)]
        if isinstance(input, str):
            self.load_reservations(input)
        elif isinstance(input, list):
            self.apply_reservations(*input)


    def show_table(self, highlight=None):
        self.update_count()
        cstyle = "bright_cyan blink2" if highlight == "available" else "bright_cyan"
        caption = Text(f"Available: {self.available_count}\t\t", style=cstyle)
        caption.append(Text(f"Unavailable: {self.unavailable_count}\t\t", style="dim strike"))
        cstyle = "green bold blink2" if highlight == "reserved" else "green bold"
        caption.append(Text(f"Reserved: {self.reserved_count}", style=cstyle))

        self.table = Table(
            *[Column(f"{i:02}", justify="center") if i != 0 else "  " for i in range(21)],
            caption=caption,
            title="SCREEN",
            expand=True,
            show_lines=True,
            header_style="bright_cyan",
            title_style="bold underline blink2",
            caption_justify="center")

        for row_id, row in self.items():
            seats = []
            seats.append(Text(row_id, style="bright_cyan"))
            for i, status in enumerate(row):
                if status == "reserved":
                    style = "green bold"
                elif status == "available":
                    style = "bright_cyan"
                elif status == "unavailable":
                    style = "dim strike"
                if status == highlight:
                    style += " blink2"
                seat = Text(f"{row_id}{i+1:02}", justify="center", style=style, end="")
                seats.append(seat)
            self.table.add_row(*seats)

        msg = Text('\nUse command "seating.show_table(OPTION)" to ', style="bright_blue")
        msg.append(Text("highlight", style="bright_blue blink2"))
        msg.append(Text(' "reserved" or "available" seating...', style="bright_blue"))
        print(msg)
        print()
        print(self.table)
        print()


    def update_count(self):
        self.available_count = 0
        self.unavailable_count = 0
        self.reserved_count = 0
        for row in self.values():
            for seat in row:
                self.available_count += (seat == "available")
                self.unavailable_count += (seat == "unavailable")
                self.reserved_count += (seat == "reserved")


    def load_reservations(self, input):
        self.in_filename = input.split('/')[-1]
        reservations = []
        with open(input, 'r') as f:
            for line in f.readlines():
                count = int(line.strip()[-1])
                reservations.append(count)
        self.apply_reservations(*reservations)


    def apply_reservations(self, *args):
        self.reservations = {}
        for i, reservation in enumerate(args):
            dq = deque()
            visited = {char: False for char in ascii_uppercase[:10]}
            left = 10 - (reservation // 2)
            right = left + reservation
            dq.appendleft(('F', left, right))
            visited['F'] = True
            deadend = [False, False]
            while dq:
                row, new_left, new_right = dq.pop()
                if all(self.is_available(seat) for seat in self[row][new_left:new_right]):
                    self.reservations[f"R{i+1:03} "] = [f"{row}{id+1}" for id in range(new_left, new_right)]
                    self[row][new_left:new_right] = ["reserved" for _ in range(reservation)]
                    self.load_restrictions(row, new_left, new_right)
                    break
                else:
                    if not deadend[0]:
                        if new_left - 1 >= 0:
                            dq.appendleft((row, new_left - 1, new_right - 1))
                        else:
                            deadend[0] = True
                    if not deadend[1]:
                        if new_right + 1 < 20:
                            dq.appendleft((row, new_left + 1, new_right + 1))
                        else:
                            deadend[1] = True
                    if not dq and all(deadend):
                        row_up, row_down = self.shift_up(row), self.shift_down(row)
                        if row_up in self and not visited[row_up]:
                            dq.appendleft((row_up, left, right))
                            visited[row_up] = True
                        elif row_down in self and not visited[row_down]:
                            dq.appendleft((row_down, left, right))
                            visited[row_down] = True


    def load_restrictions(self, row, left, right):
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
        row_up, row_down = self.shift_up(row), self.shift_down(row)
        if row_up in self:
            restrictions.append((row_up, left, right))
        if row_down in self:
            restrictions.append((row_down, left, right))
        for restriction in restrictions:
            self.apply_restriction(*restriction)


    def apply_restriction(self, row, left, right):
        self[row][left:right] = ["unavailable" for _ in range(right-left)]


    def export_out(self):
        self.out_filename = self.in_filename.replace(".in", ".out")
        with open(self.out_filename, "w") as f:
            for k, v in self.reservations.items():
                line = k + (", ").join(v) + "\n"
                f.write(line)

        msg = Text("Successfully exported output to ", style="bright_green bold")
        msg.append(Text(f"{str(Path.cwd())}/{self.out_filename}", style="bright_green bold underline"))
        print(msg)
        print(Text('(Use command "seating.show_output()" to view outputted file.)', style="bright_green bold"))
        print()


    def show_output(self):
        if self.out_filename:
            with open(self.out_filename, "rt") as f:
                print(Syntax(f.read(), "python"))
        else:
            print(Text("No output has been exported!", style="bright_red bold blink2"))

        print()
