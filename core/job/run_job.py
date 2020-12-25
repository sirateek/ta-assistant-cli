import json


class CheckRun:

    def __init__(self) -> None:
        with open('obj.json') as f:
            self.obj = json.load(f)

    @staticmethod
    def add_run_job_in_json(self, job):
        pass

