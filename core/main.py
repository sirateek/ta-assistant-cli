from display_module.display_module import TaAssisDisplay
import os
import sys
import json


class TaAssistant(TaAssisDisplay):
    def __init__(self):
        self.__job_draft = None

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
        # Process 1 - Validate path
        self.__validate_path(path_to_run)
        # Process 2 - Load file
        count_work = CountWork(path_to_run)
        count_work.run()


class CountWork:
    """
    Count Work

    Return number of zip file in ta dir
        and student data 
    """

    def __init__(self, path_to_run=""):
        self.__work = 0
        self.__student_data = {"run_job": []}
        self.__path_to_run = path_to_run

    @property
    def work(self):
        return self.__work

    @property
    def student_data(self):
        return self.__student_data

    def __read_name(self):
        file_name = []
        for file in os.listdir(self.__path_to_run):
            if file.endswith(".zip"):
                file_name.append(str(file))
        return file_name

    def __split_name(self, file_name):
        stu_data = file_name.split("_")
        stu_id = stu_data[0]
        name = stu_data[1]
        ex = stu_data[2][:3]
        return stu_id, name, ex

    def __count(self):
        filename = self.__read_name()
        self.__work = len(filename)

    def __append_studata(self):
        filename = self.__read_name()
        stu_data = []
        for i in filename:
            file_name = i
            stu_id, name, ex = self.__split_name(i)
            stu_data.append(
                {"file_name": file_name, "student_id": stu_id, "name": name, "ex": ex})

        self.__student_data["run_job"] = stu_data

    def write_json(self, path):
        import json
        with open(path, "w") as filehandel:
            json.dump(self.__student_data, filehandel)

    def run(self):
        self.__append_studata()
        self.__count()
