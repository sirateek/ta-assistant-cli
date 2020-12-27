from zipfile import ZipFile
import os
import shutil


class FileManager:

    @staticmethod
    def unzip(file_name, exdirname, path_to_run):
        """[UnZip]

        Args:
            file_name (str): name of file.zip you want to extract
            exdirname (str) : name of exercise directory
            path_to_run (str): root dir path

        Extract:
            file.zip --+ ~/ta/cashe
        """
        with ZipFile(path_to_run+"/"+exdirname+"/"+file_name, "r") as zipObj:
            zipObj.extractall(path_to_run+"/"+exdirname +
                              "/"+"/ta/cache/"+file_name[:-4])

    @staticmethod
    def del_extract(path_to_run, dirname, exdirname):
        """[delete directory]
            delete extracted file
        Args:
            path_to_run (str): root dir path
            dirname str : ditectory name
            exdirname :name of exercise directory

        Remove:
            dirname
        """
        shutil.rmtree(path_to_run+"/"+exdirname+"/ta/cache/"+dirname)

        print("Directory" + str(dirname) + "Removed")
