class TaAssisDisplay:
    @staticmethod
    def notification(text):
        print("(*) " + text)

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
