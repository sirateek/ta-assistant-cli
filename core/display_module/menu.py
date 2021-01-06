from display_module.display_module import TaAssisDisplay


class Menu(TaAssisDisplay):
    def __init__(self, menu_item, menu_title):
        # Date Structure for menu_item
        # {
        #   "selection_char": ("description", Call Back Method)
        # }
        self.__menu_item = menu_item
        self.__menu_title = menu_title

    def pick(self):
        """Method to start the menu picking process
        """
        print("")
        self.notification(self.__menu_title)
        for key, value in self.__menu_item.items():
            self.subnotification(key, value[0])
        while True:
            selection = self.input_from_user("Your Selection: ")
            print("")
            if selection not in self.__menu_item:
                self.failure(
                    "Invalid input. Please input only the char in the Parenthesis")
                continue
            return self.__menu_item[selection][1]()

