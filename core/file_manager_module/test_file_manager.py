from file_manager import FileManager
from zipfile import ZipFile
import unittest
import os


class TestFileManager(unittest.TestCase):
    def test_del_extract(self):
        test_case = []
        predict_case = []
        path_to_run = os.environ["PWD"]+"/test/test_file_manager"
        unzip = FileManager()
        unzip.unzip(path_to_run, "Test.zip")
        rmdir = FileManager()
        rmdir.del_extract(path_to_run, "Test")
        for file in os.listdir(path_to_run+"/ta/cache"):
            if file == "Test":
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)

    def test_unzip(self):
        test_case = []
        predict_case = ["test.txt"]
        path_to_run = os.environ["PWD"] + "/test/test_file_manager"
        unzip = FileManager()
        unzip.unzip(path_to_run, "Test.zip")
        for file in os.listdir(path_to_run+"/ta/cache/"+"Test"):
            if file.endswith(".txt"):
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)


if __name__ == "__main__":
    unittest.main()
