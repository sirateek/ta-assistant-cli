from file_manager import FileManager
from zipfile import ZipFile
import unittest
import os


class TestUnZip(unittest.TestCase):
    def test_del_extract(self):
        test_case = []
        predict_case = []
        path_to_run = os.environ["PWD"]
        file_path = path_to_run+"/test"
        f = open(file_path+"/test.txt", "w+")
        for i in range(10):
            f.write(f"This is Test | line: {i+1} \n")
        with ZipFile(file_path+"/Test.zip", "w") as zipObj:
            zipObj.write(os.path.join(file_path, "test.txt"),
                         arcname="test.txt")
        os.remove(file_path+"/test.txt")
        unzip = FileManager()
        unzip.unzip("Test.zip", "test", path_to_run)
        rmdir = FileManager()
        rmdir.del_extract(path_to_run, "Test", "test")
        for file in os.listdir(path_to_run+"/test/ta/cashe"):
            if file == "Test":
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)

    def test_unzip(self):
        test_case = []
        predict_case = ["test.txt"]
        path_to_run = os.environ["PWD"]
        file_path = path_to_run+"/test"
        f = open(file_path+"/test.txt", "w+")
        for i in range(10):
            f.write(f"This is Test | line: {i+1} \n")
        with ZipFile(file_path+"/Test.zip", "w") as zipObj:
            zipObj.write(os.path.join(file_path, "test.txt"),
                         arcname="test.txt")
        os.remove(file_path+"/test.txt")
        unzip = FileManager()
        unzip.unzip("Test.zip", "test", path_to_run)
        for file in os.listdir(file_path+"/ta/cashe/"+"Test"):
            if file.endswith(".txt"):
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)


if __name__ == "__main__":
    unittest.main()
