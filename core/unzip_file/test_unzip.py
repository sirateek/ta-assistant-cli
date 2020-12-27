from unzip import UnZip
from zipfile import ZipFile
import unittest
import os


class TestUnZip(unittest.TestCase):

    def test_unzip(self):
        test_case = []
        predict_case = ["test.txt"]
        env_var = os.environ["PWD"]
        file_path = env_var+"/core/unzip_file/test_unzip"
        f = open(file_path+"/test.txt", "w+")
        for i in range(10):
            f.write(f"This is Test | line: {i+1} \n")
        with ZipFile(file_path+"/Test.zip", "w") as zipObj:
            zipObj.write(os.path.join(file_path, "test.txt"),
                         arcname="test.txt")
        os.remove(file_path+"/test.txt")
        unzip = UnZip()
        unzip.unzip("Test.zip", file_path)
        for file in os.listdir(file_path+"/ta/cashe"):
            if file.endswith(".txt"):
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)

    def test_delete_file(self):
        test_case = []
        predict_case = []
        env_var = os.environ["PWD"]
        file_path = env_var+"/core/unzip_file/test_unzip"
        del_file = UnZip()
        del_file.delete_zipfile("Test.zip", file_path)
        for file in os.listdir(file_path):
            if file.endswith("Test.zip"):
                test_case.append(str(file))
        self.assertEqual(test_case, predict_case)


if __name__ == "__main__":
    unittest.main()
