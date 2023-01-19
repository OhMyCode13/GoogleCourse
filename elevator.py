class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return "Current floor is: {}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
        else:
            print("Elevator is already at the top floor")
            return self.current
        return self.current

    def down(self):
        """Makes the elevator go down one floor."""
        self.current -= 1
        return self.current

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor != self.current:
            while self.current != floor:
                if floor > self.current:
                    if floor>self.top:
                        print("Wrong floor selected")
                        return self.current
                    else:
                        print(self.up())
                else:
                    if floor<self.bottom:
                        print("Wrong floor selected")
                        return self.current
                    else:
                        print(self.down())
        return self.current


elevator = Elevator(-1, 10, 0)
elevator.up()
print(elevator)
elevator.down()
print(elevator)
elevator.go_to(10)
elevator.go_to(11)
elevator.go_to(3)
elevator.go_to(-2)
print(elevator)
