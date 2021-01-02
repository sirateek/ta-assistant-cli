import os
import json


class JobList:
    """
    JobList

    Return number of zip file in ta dir
    and student data
    """

    def __init__(self, path_to_run="", job_draft=""):
        """
        Args:
            path_to_run (str): path to run
            job_draft (str): job_draft.json
        """
        self.__path_to_run = path_to_run
        self.__job_draft = job_draft
        self.__jobs = []
        self.__jobs_all = []
        self.__jobs_run = []
        self.__unknown_files = []

    @property
    def jobs(self):
        """[jobs]
        Data Structure:
        [
            `Job Object`
        ]
        Returns:
            List: Contain the List of the `Job` Object (Job List to workon)
        """
        return self.__jobs

    @property
    def unknown_files(self):
        """[invalid file name]

        Data Structure:
        [
            "{File Name}.zip"
        ]

        Returns:
            list : Contain the file name that can't be parsed by using the `job_draft.zip_file_draft`
        """
        return self.__unknown_files

    @property
    def job_runs(self):
        """[rated student]
        Data Structure:
        [
            Job Object
        ]

        Returns:
            list : List of the job object that has already been run.
        """
        return self.__jobs_run

    def __read_jobs_file(self):
        """[read name]

        Returns:
            list : list of full name of given file in exercise directory
        """
        file_name = []
        for file in os.listdir(self.__path_to_run):
            if file.endswith(".zip"):
                file_name.append(str(file))
        return file_name

    def __check_file_name(self, stu_data, file_name, split_list):
        """[check file name]

        Args:
            stu_data (list): dictionary of student data that keep | the following the given draft.json [zip_file_draft]
            file_name (string): name of the file to be check

        Returns:
            bool : if the are not following the given draft return false
        """
        for i in stu_data:
            if ".zi" in i:
                self.__unknown_files.append(file_name)
                return False
            for j in split_list:
                if j in i:
                    self.__unknown_files.append(file_name)
                    return False
        return True

    def __split_name(self, file_name, split_list):
        """[split name]
            split file so it can be classification
        Args:
            file_name (string): file name that you want to seperate

        Returns:
            list : list of string that following that draft.json (zip_file_draft)
        """
        stu_data = []
        for i in split_list:
            value_splited = file_name[:file_name.find(i)]
            stu_data.append(value_splited)
            file_name = file_name[file_name.find(i)+1:]

        return stu_data

    def __split(self):
        """[split]
        Analyze what the sample is given, what keys, and what classifications are required
        """
        key_list = []
        split_list = []
        zip_draft = self.__job_draft["zip_file_draft"]
        n = zip_draft.count("}")
        for _ in range(n):
            key = zip_draft[zip_draft.find("{")+1: zip_draft.find("}")]
            key_list.append(key)
            split_list.append(
                zip_draft[zip_draft.find("}")+1:zip_draft.find("}")+2])
            zip_draft = zip_draft[zip_draft.find("}")+1:]
        return (key_list, split_list)

    def __read_jobs_from_dir(self, key_list, split_list):
        """[append student data]
        put the information that has been categorized into the list/json (self.__student_data)
        """
        filename = self.__read_jobs_file()
        for i in filename:
            file_name = i
            job_vars = {}
            if self.__check_file_name(self.__split_name(i, split_list), i, split_list) is False:
                continue
            for j, k in zip(self.__split_name(i, split_list), key_list):
                job_vars[k] = j
            self.__jobs.append(Job(file_name=file_name, job_vars=job_vars))

    def __categorize_job(self, job_file):
        """[check job done]
        check that which student have been rated and remove them form self.__student_data
        Args:
            job_file (job.json): list of student that has been rated
        """
        # Convert Job File to Job object
        for item in job_file["run_job"]:
            file_name = item["file_name"]
            item.pop("file_name")
            job_vars = item
            self.__jobs_run.append(Job(file_name=file_name, job_vars=job_vars))

        intersect_list = [
            value for value in self.__jobs if value in self.__jobs_run]
        for item in intersect_list:
            self.__jobs.pop(self.__jobs.index(item))

    def load_jobs(self, job_file):
        key_list, split_list = self.__split()
        self.__read_jobs_from_dir(key_list, split_list)
        self.__categorize_job(job_file)


class Job:

    def __init__(self, file_name="", job_vars={}):
        """The Constructure Object of Job
        """
        self.__file_name = file_name
        self.__job_vars = job_vars
        self.__is_run = False

    def add_job_vars(self, key, val):
        self.__job_vars[key] = val

    def write_job_vars(self):
        pass

    def generate_dict_report(self):
        dict_data = {
            "file_name": self.__file_name
        }
        dict_data.update(self.__job_vars)
        return dict_data

    def toggle_is_run(self):
        self.__is_run = True

    def __eq__(self, compare):
        """The descript the Equality of the object
        By using `file_name`
        """
        return compare.file_name == self.__file_name

    def __hash__(self):
        return hash(str(self))

    @property
    def is_run(self):
        """The Property to prevent non-successfully job to be written in the Job File (job.json)
        """
        # The Property of is_run attribute
        return self.__is_run

    @property
    def file_name(self):
        # The Property of file_name attribute
        return self.__file_name

    @property
    def job_vars(self):
        # The Property of job_vars attribute
        return self.__job_vars
