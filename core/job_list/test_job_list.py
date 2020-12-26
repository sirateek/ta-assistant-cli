import unittest
import os
from job_list import JobList


class test_job_list(unittest.TestCase):
    def test_load_file(self):
        job_list = JobList(
            path_to_run=os.getenv('TAASSISTANT_RUN_PATH'),
            job_draft={
                "zip_file_draft": "{student_id}_{name}_{ex}.zip",
                "output_draft": ["student_id", "name", "ex", "score1", "score2", "comment"]
            }
        )

        job_list.run()
        job_list.student_data["run_job"].sort(
            key=lambda data: data["student_id"])
        self.assertEqual(job_list.student_data["run_job"],
                         [
                             {'file_name': '12345678_test_ex1.zip',
                                 'student_id': '12345678', 'name': 'test', 'ex': 'ex1'},
                         {'file_name': '12345679_test2_ex1.zip',
                             'student_id': '12345679', 'name': 'test2', 'ex': 'ex1'},
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
                         )
        self.assertEqual(job_list.invalid_file_name,
                         ['Unknown File.zip']
                         )

    def test_recover_app_state(self):
        job_list = JobList(
            path_to_run=os.getenv('TAASSISTANT_RUN_PATH'),
            job_draft={
                "zip_file_draft": "{student_id}_{name}_{ex}.zip",
                "output_draft": ["student_id", "name", "ex", "score1", "score2", "comment"]
            }
        )

        job_list.run()

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
        job_list.check_job_done(job_file_data)
        job_list.student_data["run_job"].sort(
            key=lambda data: data["student_id"])
        self.assertEqual(job_list.student_data["run_job"],
                         [
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
        )
        self.assertEqual(job_list.invalid_file_name,
                         ['Unknown File.zip']
                         )


if __name__ == "__main__":
    unittest.main()
