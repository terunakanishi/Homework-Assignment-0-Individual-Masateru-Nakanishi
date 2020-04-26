"""Program that plays Rock-Paper-Scissors.

Author: Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor: ...
* TU/e ID number: ...
* Date: ...

The three choice options Rock, Paper, and Scissors are encoded
in an integer (see constant :data:`OPTIONS`).

To translate letter ``c`` (``c in RPS``) to an integer,
use :func:`rps_choice`.
"""

from typing import Sequence, Mapping
import random
import tkinter as tk

#: The encoding of the three choice options
OPTIONS = {0: "Rock", 1: "Paper", 2: "Scissors"}

#: The valid choice letters
RPS = ''.join(name[0].lower() for name in OPTIONS.values())

#: Type for (probability) distribution, assuming same keys as :data:`OPTIONS`
Distribution = Mapping[int, float]


def rps_choice(letter: str) -> int:
    """Return choice integer corresponding to given letter.

    The letter is first converted to lower case.

    Assumptions:
    * len(letter) == 1
    * letter.lower() in RPS

    :param letter: letter to convert to integer
    :return: integer in OPTIONS corresponding to letter

    >>> rps_choice('r')
    0
    >>> rps_choice('P')
    1
    >>> rps_choice('s')
    2
    >>> rps_choice('X')
    Traceback (most recent call last):
        ...
    AssertionError: letter.lower() must be in RPS
    """
    assert letter.lower() in RPS, "letter.lower() must be in RPS"

    return RPS.index(letter.lower())


def what_beats(choice: int) -> int:
    """Return the choice that beats the given choice.

    Assumption: choice in OPTIONS

    :param choice: choice to beat
    :return: the choice that beats the given choice

    >>> what_beats(0)
    1
    >>> what_beats(1)
    2
    >>> what_beats(2)
    0
    """
    return choice + 1  # (choice + 1) % 3


def beats(choice_1: int, choice_2: int) -> bool:
    """Return whether choice_1 beats choice_2.

    Assumption: choice_1 in OPTIONS and choice_2 in OPTIONS

    :param choice_1: choice of first player
    :param choice_2: choice of second player
    :return: whether choice_1 beats choice_2

    >>> beats(0, 0)
    False
    >>> beats(0, 1)
    False
    >>> beats(1, 0)
    True
    >>> beats(0, 2)
    True
    """
    return choice_1 > choice_2  # (choice_1 - choice_2) % 3 == 1
    # equiv to choice_1 == what_beats(choice_2)


def random_choice(distr: Distribution) -> int:
    """Return choice in OPTIONS with given distribution.

    Assumptions:
    * set(weights.keys()) == set(OPTIONS.keys())
    * all(w >= 0 for w in distr)

    >>> all(random_choice({0: 1, 1: 1, 2: 1}) in OPTIONS for _ in range(10))
    True
    """
    return random.choices(list(distr.keys()), weights=list(distr.values()), k=1)[0]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Rock - Paper - Scissors")
        master.geometry('320x320+100+100')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self, borderwidth=4, relief=tk.GROOVE)
        self.frame.pack()

        self.rock_button = tk.Button(self.frame)
        self.rock_button["text"] = OPTIONS[0]
        self.rock_button["command"] = lambda: self.show_choice(0)
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.frame)
        self.paper_button["text"] = OPTIONS[1]
        self.paper_button["command"] = lambda: self.show_choice(1)
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.frame)
        self.scissors_button["text"] = OPTIONS[2]
        self.scissors_button["command"] = lambda: self.show_choice(2)
        self.scissors_button.pack(side=tk.LEFT)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def show_choice(self, choice: int) -> None:
        print(f"You chose {OPTIONS[choice]}")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
