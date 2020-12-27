from zipfile import ZipFile
import os


class UnZip:

    def unzip(self, file_name, path_to_run):
        """[UnZip]

        Args:
            file_name (str): name of file.zip you want to extract
            path_to_run (str): root dir path

        Extract:
            file.zip --+ ~/ta/cashe
        """
        with ZipFile(path_to_run+"/"+file_name, "r") as zipObj:
            zipObj.extractall(path_to_run+"/ta/cashe")

    def delete_zipfile(self, file_name, path_to_run):
        """[UnZip]

        Args:
            file_name (str): name of file.zip you want to remove
            path_to_run (str): root dir path

        Remove:
            file.zip --- [ ]
        """
        os.remove(path_to_run+"/"+file_name)
        print("File" + file_name + "Removed")
