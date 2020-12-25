from display_module.display_module import TaAssisDisplay
from job_list.job_list import JobList
import os
import sys
import json


class TaAssistant(TaAssisDisplay):
    def __init__(self):
        self.__version = "0.1.0"
        self.__job_draft = None
        self.__job_list = None

    def __validate_path(self, path_to_run):
        self.notification("Starting Path validation process")

        # Validate path_to_run
        validate_name = "Validate Path"
        if not os.path.isdir(path_to_run):
            self.subnotification("X", validate_name)
            self.failure("Path not found")
            sys.exit(1)
        self.subnotification("/", validate_name)

        # Validate draft file
        validate_name = "Validate Draft File (`/ta/draft/draft.json`)"
        if not os.path.isfile(path_to_run + "/ta/draft/draft.json"):
            self.subnotification("X", validate_name)
            self.failure("Draft file not found")
            sys.exit(1)

        draft_file = open(path_to_run + "/ta/draft/draft.json")
        read_draft_file = json.load(draft_file)

        if read_draft_file.get("zip_file_draft", "") == "" or\
                read_draft_file.get("output_draft", "") == "":
            self.subnotification("X", validate_name)
            self.failure("Invalid Draft file structure")
            sys.exit(1)

        self.__job_draft = read_draft_file
        self.subnotification("/", validate_name)

        # Validate job file
        validate_name = "Validate Job File (`/ta/job/job.json`)"
        if not os.path.isfile(path_to_run + "/ta/job/job.json"):
            jobFile = open(path_to_run + "/ta/job/job.json", "w")
            json.dump({}, jobFile)
            self.subnotification("C", validate_name)
        else:
            self.subnotification("/", validate_name)

    def start(self, path_to_run, cli_version):
        # Process 0 - Welcome user
        self.title_message(self.__version, cli_version)
        self.notification("Starting the job on " + path_to_run)

        # Process 1 - Validate path
        self.__validate_path(path_to_run)

        # Process 2 - Load file
        self.notification("Loading Job list")
        self.__job_list = JobList(path_to_run)
        print(self.__job_draft)
        self.__job_list.run()


if __name__ == "__main__":
    run = TaAssistant()
    run.start("example_dir/ex1", "0.1.0")
