class TaAssisDisplay:
    @staticmethod
    def notification(text, notification_icon=None):
        print("({}) ".format(notification_icon or "*") + text)

    @staticmethod
    def input_from_user(text):
        return input("(?) " + text)

    @staticmethod
    def subnotification(status, text):
        print(" |-({}) {}".format(status, text))

    @staticmethod
    def failure(text):
        print("(!!) " + text)

    def title_message(self, core_version, cli_version):
        print("*" + "="*50 + "*")
        print("|{:^50}|".format("TA Assistant CLI"))
        print("|{:^50}|".format("Core Ver: " +
                                core_version + " CLI Ver: " + cli_version))
        print("*" + "="*50 + "*")
        self.notification("Welcome to TA Assistant CLI")

    def report_table(self, report_title, report_data, colList=None):
        self.notification(report_title)
        self.subnotification("i", "Item amounts: " + str(len(report_data)))
        if not colList:
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
