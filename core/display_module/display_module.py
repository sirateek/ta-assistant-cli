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
