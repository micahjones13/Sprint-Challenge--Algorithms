class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def move_back_to_start(self):
        # go back to start
        while self.can_move_left():
            self.move_left()
        # get away from none
        self.move_right()
        print(self._position, 'moving left')

    def sort(self):
        """
        Sort the robot's list.
        OK: any methods above
        OK: for, while, break, continue
        OK: if and or not
        OK: < > <= >= ect
        NOT OK: storing variables
        NOT OK: self.anything
        NOT OK: sorted, sort, ect
        NOT OK: modififying above methods

        PLAN: start at begining of list, pick up that card. Go to next item, compare current card to that card.
        If current card is greater than that of which we are comparing, move to next item and repeat.
        If the card we are comparing is greater, swap, and compare that card to the next.
        Need to check if the robot can move right everytime, though
        Light might mean working vs finished
        """
        # Fill this out
        # replace none with first item in list, none is always < an actual num
        # [5, 3, 4, 1, 2]
        # self.swap_item()
        # # [none, 3, 4, 1, 2]
        # # print(self._item)
        # # move right so he doesn't compare the num he picked up to none
        # self.move_right()
        # [none[0], 3[1], 4[2] 2[3]]

        # want to start with light on to know we are going and to set an end condition
        self.set_light_on()
        while self.light_is_on():
            self.set_light_off()
            # as long as it can move right go right, and start comparing
            while self.can_move_right():
                # inital swap to get a value
                self.swap_item()
                # move right, don't compare to value you just dropped
                self.move_right()
                # if held item is greater, swapt that item, move left and place it there, move back right
                # if it reaches the end and is greater, turn light on to restart with next value
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()
                # else if the held item is less than comparison item
                # place the held item down BEFORE the comparision item
                # no light change here, we aren't done
                if self.compare_item() == -1:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                # else if item is the same value as comparison
                # put the held item down by the same value item, move back right to comparison item
                if self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            # this if keeps the chain moving
            # light is only on if the one round of sorting is complete,
            if self.light_is_on():
                while self.can_move_left():
                    self.move_left()

        #! Can definitley do it easier with self._list, lol
        # for i in range(len(self._list)):
        #     for j in range(0, len(self._list)-1):
        #         if self._list[j] > self._list[j+1]:
        #             self._list[j], self._list[j +
        #                                       1] = self._list[j+1], self._list[j]
        # return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

#     robot = SortingRobot(l)
    small_list = [5, 3, 4, 1, 2]
    test = SortingRobot(small_list)
    test.sort()
    print(test._list)
    # robot.sort()
    # print(robot._list)
