from zipfile import ZipFile
import os
import shutil


class FileManager:

    @staticmethod
    def unzip(path_to_run, file_name):
        """[UnZip]

        Args:
            file_name (str): name of file.zip you want to extract
            path_to_run (str): run path

        Extract:
            file.zip --+ ~/ta/cashe
        """
        with ZipFile(path_to_run+"/"+file_name, "r") as zipObj:
            zipObj.extractall(path_to_run +
                              "/ta/cache/" + file_name[:-4])

    @staticmethod
    def del_extract(path_to_run, dirname):
        """[delete directory]
            delete extracted file
        Args:
            path_to_run (str): run path
            exdirname :name of exercise directory

        Remove:
            dirname
        """
        shutil.rmtree(path_to_run+"/ta/cache/"+dirname)

        print("Directory" + str(dirname) + "Removed")
