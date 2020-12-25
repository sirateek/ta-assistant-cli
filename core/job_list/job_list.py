import os


class JobList:
    """
    JobList

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
