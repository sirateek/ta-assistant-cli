class Job:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.state = "not checked"
        self.job_var = {}
        self.score = {}