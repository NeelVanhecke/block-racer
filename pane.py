"""The Pane class will make a pane containing label/value pairs."""


class Pane:
    def __init__(self, pos, width, height, rows, columns, things):
        self.pos = pos                              # Upper left corner of the pane
        self.width = width                          # Widht of the pane
        self.height = height                        # Height of the pane
        self.rows = rows                            # Number of rows
        self.columns = columns                      # Number of columns
        self.things_to_add_to_pane = things         # Buttons and labels to add to the pane, length should equal rows*columns
                                                    # Its a dict: {'buttons': list, 'labels': list ...}

        self.buttons = []
        self.initialize()

    def initialize(self):


