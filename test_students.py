import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    """
    * Create a new test mothod called test_apply_extension
    * Inside test_apply_extension, store the current end_date for our student instance in a varible called old_end_date
    * Call a method maned apply_extension that will take anumber of days as an argument on the student instance to update the end_date
    * Assert whether the instance's end_date equals the old end date plus the days plus the days argument that was passed in using timedelta
    * Run the tests to confirm that the new method is failing
    * In the Student class, created a new method called apply_extension that has a parameter called days
    * Use the timedelta method from datetime to update the end_date property
    * Run the tests to confirm they are working.
    """
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedalta(days=5))
        """
        The method below is also great! But keep in mid that it will
        only be correct if a student has received 1 extension. If they
        receive a second - it  would return false

        self.student.apply_extension(5
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
        """

    def tast_course_schedule_success(self):
        with patch("student.request.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == '__main__':
    unittest.main()

