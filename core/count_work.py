import os
"""
Count Work

Return number of zip file in ta dir
       and student data 
"""

class CountWork:
    def __init__(self):
        self.__work = 0
        self.__student_data = {"un_check_job":[]}
        
    @property
    def work(self):
        return self.__work
    
    @property
    def student_data(self):
        return self.__student_data

    def __read_name(self):
        file_name = []
        for file in os.listdir("example_dir/ex1"):
            if file.endswith(".zip"):
                file_name.append(str(file))
        return file_name

    def __split_name(self,file_name):
        stu_data = file_name.split("_")
        stu_id = stu_data[0]
        name = stu_data[1]
        ex = stu_data[2][:3]
        return stu_id, name,ex

    def __count(self):
        filename = self.__read_name()
        self.__work = len(filename)

    def __append_studata(self):
        filename = self.__read_name()
        stu_data = []
        for i in filename:
            file_name = i
            stu_id,name,ex = self.__split_name(i)
            stu_data.append({"file_name":file_name,"student_id":stu_id,"name":name,"ex":ex})
    
        self.__student_data["un_check_job"] = stu_data
    
    def __write_json(self):
        import json
        with open("example_dir/ex1/ta/job/un_check_job.json","w") as filehandel:
            json.dump(self.__student_data,filehandel)

    def run(self):
        self.__append_studata()
        self.__count()
        self.__write_json()



if __name__ == "__main__":
    test = CountWork()
    test.run()
    a = test.student_data
    b = test.work
    print(a)
    print(b)
