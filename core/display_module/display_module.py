class TaAssisDisplay:
    @staticmethod
    def notification(text, notification_icon=None):
        """Method for displaying the notificaiton to user
        """
        print("({}) ".format(notification_icon or "*") + text)

    @staticmethod
    def input_from_user(text):
        """Method for input the user_input
        """
        return input("(?) " + text)

    @staticmethod
    def subnotification(status, text):
        """Method for displaying the sub-notification to user
        """
        print(" |-({}) {}".format(status, text))

    @staticmethod
    def failure(text):
        """Method for displaying the failure-notification to user
        """
        print("(!!) " + text)

    def title_message(self, core_version, cli_version):
        """Method for displaying the welcome message to user
        """
        print("*" + "="*50 + "*")
        print("|{:^50}|".format("TA Assistant CLI"))
        print("|{:^50}|".format("Core Ver: " +
                                core_version + " CLI Ver: " + cli_version))
        print("*" + "="*50 + "*")
        self.notification("Welcome to TA Assistant CLI")

    def report_table(self, report_title, report_data):
        """Method for display the report_table to the user
        Note: 1) The report_data must be a list of dict.
              2) The report_table will dynamically adjust the table size related to the inputted report_data

        Data Structure `report_data`:
        [
            {
                "name": "a",
                "score": "1"
            },
            {
                "name": "a",
                "score": "1"
            }
        ]
        """
        self.notification(report_title)
        self.subnotification("i", "Item amounts: " + str(len(report_data)))

        colList = list(report_data[0].keys() if report_data else [])
        myList = [colList]
        for item in report_data:
            myList.append([str(item[col] if item[col] is not None else '')
                           for col in colList])
        colSize = [max(map(len, col)) for col in zip(*myList)]
        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
        myList.insert(0, ['-' * i for i in colSize])
        myList.insert(2, ['-' * i for i in colSize])
        myList.append(['-' * i for i in colSize])
        for item in myList:
            print(formatStr.format(*item))
