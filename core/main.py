from display_module.display_module import TaAssisDisplay
from display_module.menu import Menu
from job_list.job_list import JobList
from file_manager_module.file_manager import FileManager
import os
import sys
import json


class TaAssistant(TaAssisDisplay):
    def __init__(self):
        self.__version = "0.1.0"
        # Keep the loaded job draft file info.
        # (/ta/draft/draft.json)
        self.__job_draft = None
        # Keep the loaded job file info.
        # (/ta/job/job.json)
        self.__job_file = None
        # Hold the JobList Object
        self.__job_list = None
        # Hold the value to tell that user accept the loaded job list
        self.__is_accept_job_list = False

    def __validate_path(self, path_to_run):
        """Path validation process (Process 1)
        """
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
            json.dump({"run_job": []}, jobFile)
            self.__job_file = {"run_job": []}
            self.subnotification("C", validate_name)
        else:
            jobFile = open(path_to_run + "/ta/job/job.json", "r")
            self.__job_file = json.load(jobFile)
            self.subnotification("/", validate_name)

    def __trigger_accept_attribute(self):
        """Method to trigger the is_accept_job_list value to True
        """
        self.__is_accept_job_list = True

    def __decline_job_list(self):
        """Method to use when user decline the loaded job list
        Note: It used to print the failure message and call exit with code 1
        """
        self.failure("You've decline the job list. Stopping the process.")
        sys.exit(1)

    def __ask_user_to_accept_job_list(self):
        """Method to ask the user to review the loaded job list
        """
        # the ask user menu
        accept_job_menu = Menu({
            "a": ("Accept", lambda: self.__trigger_accept_attribute()),
            "d": ("Decline", lambda: self.__decline_job_list()),
            "j": ("JobList", lambda: self.report_table("Job List", [item.generate_dict_report() for item in self.__job_list.jobs])),
            "u": ("UnknownList", lambda: self.report_table("Unknown file Result",
                                                           [{"file_name": item}
                                                               for item in self.__job_list.unknown_files]
                                                           )),
            "z": ("Zip File Draft", lambda: self.notification("Zip File Draft: " + self.__job_draft["zip_file_draft"], "i")),
            "o": ("Output Draft", lambda: self.notification("Output Draft: " + str(self.__job_draft["output_draft"]), "i"))
        },
            "Review Job list menu"
        )
        print("")
        self.notification(
            "Please review the job list result and accept to continue")
        while not self.__is_accept_job_list:
            accept_job_menu.pick()
        self.notification(
            "You've accepted the job list. Starting the job process now.")

    def __add_job_vars(self, job_obj):
        self.notification("Job vars:")
        for i in self.__job_draft["output_draft"]:
            if i in job_obj.job_vars:
                self.subnotification(
                    "i", "{0} : {1}".format(i, job_obj.job_vars[i]))
            else:
                user_input = self.input_from_user(
                    "Enter a value for {}: ".format(i))
                job_obj.add_job_vars(i, user_input)

    def __write_job_vars(self, job_obj):
        pass

    def __show_job_vars(self, job_obj):
        data = [job_obj.job_vars]
        self.report_table("Current job variables", data)

    def __job_vars_input(self, job_obj):
        manage_job_menu = Menu({
            "a": ("Add job vars", lambda: self.__add_job_vars(job_obj)),
            "c": ("Show current job vars", lambda: self.__show_job_vars(job_obj)),
            "w": ("Write job", lambda: self.__write_job_vars(job_obj)),
            "s": ("Skip this job", lambda: "s")
        },
            "Job management"
        )
        while True:
            manage_job_menu.pick()

    def __run_all_job(self, path_to_run):
        fm = FileManager
        job_count = 1
        for item in self.__job_list.jobs:
            self.notification("Job ({})".format(job_count))
            self.subnotification("i", item.file_name)
            fm.unzip(path_to_run, item.file_name)
            # os.system(
            #     "code {0}/ta/cache/{1}".format(path_to_run, item.file_name[:-4]))
            self.__job_vars_input(item)
            job_count += 1

    def start(self, path_to_run, cli_version):
        # Process 0 - Welcome user
        self.title_message(self.__version, cli_version)
        self.notification("Starting the job on " + path_to_run)

        # Process 1 - Validate path
        self.__validate_path(path_to_run)

        # Process 2 - Load file
        self.notification("Loading Job list")
        self.__job_list = JobList(path_to_run, self.__job_draft)
        self.__job_list.load_jobs(self.__job_file)
        self.subnotification("/", "Job list load successfully")

        # Process 3 - Print the result and ask for job confirmation
        self.__ask_user_to_accept_job_list()

        # Process 4 - Run  all the job
        self.__run_all_job(path_to_run)
