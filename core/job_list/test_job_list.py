from job_list import JobList
import unittest
import os
import sys


class test_job_list(unittest.TestCase):
    def test_load_file(self):
        job_list = JobList(
            path_to_run=os.getenv('TAASSISTANT_RUN_PATH'),
            job_draft={
                "zip_file_draft": "{student_id}_{name}_{ex}.zip",
                "output_draft": ["student_id", "name", "ex", "score1", "score2", "comment"]
            }
        )

        # Simmulated Job File Data
        job_file_data = {
            "run_job": [
                {
                    "file_name": "12345678_test_ex1.zip",
                    "student_id": "12345678",
                    "name": "test",
                    "ex": "ex1",
                    "score1": "10",
                    "score2": "1",
                    "comment": "This is a comment"
                },
                {
                    "file_name": "12345679_test2_ex1.zip",
                    "student_id": "12345679",
                    "name": "test2",
                    "ex": "ex1",
                    "score1": "10",
                    "score2": "1",
                    "comment": "This is a comment for job 2"
                }
            ]
        }
        job_list.load_jobs(job_file_data)
        list_a = [
            item.generate_dict_report() for item in job_list.jobs
        ]
        list_a.sort(
            key=lambda data: data["file_name"])
        list_b = [
            {'file_name': '6310546062_vitvara_ex1.zip',
             'student_id': '6310546062', 'name': 'vitvara', 'ex': 'ex1'},
            {'file_name': '6310546063_vitvara_ex1.zip', 'student_id': '6310546063',
             'name': 'vitvara', 'ex': 'ex1'},
            {'file_name': '6310546064_vitvara_ex1.zip',
             'student_id': '6310546064', 'name': 'vitvara', 'ex': 'ex1'},
            {'file_name': '6310546065_vitvara_ex1.zip',
             'student_id': '6310546065', 'name': 'vitvara', 'ex': 'ex1'},
            {'file_name': '6310546066_vitvara_ex1.zip',
             'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1'}
        ]
        self.assertEqual(list_a, list_b)
        self.assertEqual(job_list.unknown_files,
                         ['Unknown File.zip']
                         )


if __name__ == "__main__":
    unittest.main()
