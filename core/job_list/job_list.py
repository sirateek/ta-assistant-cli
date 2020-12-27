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

        self.__work = 0
        self.__student_data = {"run_job": []}
        self.__invalid_file_name = []
        self.__key_list = []
        self.__split_list = []
        self.__rated_student = []

    @property
    def work(self):
        """[work]

        Returns:
            int : amount or work
        """
        return self.__work

    @property
    def student_data(self):
        """[student data]

        Returns:
            dict(.json): dictionary of student data that keep | the following the given draft.json [zip_file_draft]
        """
        return self.__student_data

    @property
    def invalid_file_name(self):
        """[invalid file name]

        Returns:
            list : list of the file.zip with the name is invalid
        """
        return self.__invalid_file_name

    @property
    def rated_student(self):
        """[rated student]

        Returns:
            list : list of student that has been rated     
        """
        return self.__rated_student

    def __read_name(self):
        """[read name]

        Returns:
            list : list of full name of given file in exercise directory
        """
        file_name = []
        for file in os.listdir(self.__path_to_run):
            if file.endswith(".zip"):
                file_name.append(str(file))
        return file_name

    def __check_file_name(self, stu_data, file_name):
        """[check file name]

        Args:
            stu_data (list): dictionary of student data that keep | the following the given draft.json [zip_file_draft]
            file_name (string): name of the file to be check

        Returns:
            bool : if the are not following the given draft return false
        """
        for i in stu_data:
            if ".zi" in i:
                self.__invalid_file_name.append(file_name)
                return False
            for j in self.__split_list:
                if j in i:
                    self.__invalid_file_name.append(file_name)
                    return False
        return True

    def __split_name(self, file_name):
        """[split name]
            split file so it can be classification
        Args:
            file_name (string): file name that you want to seperate

        Returns:
            list : list of string that following that draft.json (zip_file_draft)
        """
        split_list = self.__split_list
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
        for i in range(n):
            key = zip_draft[zip_draft.find("{")+1: zip_draft.find("}")]
            key_list.append(key)
            split_list.append(
                zip_draft[zip_draft.find("}")+1:zip_draft.find("}")+2])
            zip_draft = zip_draft[zip_draft.find("}")+1:]
        self.__key_list = key_list
        self.__split_list = split_list

    def __count(self):
        """[count]
        count amount of work and keep it in self.__work
        """
        filename = self.__read_name()
        self.__work = len(filename)

    def __append_studata(self):
        """[append student data]
        put the information that has been categorized into the list/json (self.__student_data)
        """
        filename = self.__read_name()
        stu_data = []
        for i in filename:
            person_data = {}
            person_data["file_name"] = i
            if self.__check_file_name(self.__split_name(i), i) is False:
                continue
            for j, k in zip(self.__split_name(i), self.__key_list):
                person_data[k] = j
            stu_data.append(person_data)
        self.__student_data["run_job"] = stu_data

    def run(self):
        self.__split()
        self.__append_studata()
        self.__count()

    def check_job_done(self, job_file):
        """[check job done]
        check that which student have been rated and remove them form self.__student_data
        Args:
            job_file (job.json): list of student that has been rated
        """
        job_list = job_file["run_job"]
        for done_stu in job_list:
            for stu in self.__student_data["run_job"]:
                if done_stu["student_id"] == stu["student_id"]:
                    self.__rated_student.append(self.__student_data["run_job"].pop(
                        self.__student_data["run_job"].index(stu)))


if __name__ == "__main__":
    run = JobList("example_dir/ex1", {"zip_file_draft": "{student_id}_{name}_{ex}.zip",
                                      "output_draft": ["student_id", "name", "ex", "score1", "score2", "comment"]})
    run.run()
    run.check_job_done("example_dir/ex1/ta/job/job.json")
    print(run.rated_student)
