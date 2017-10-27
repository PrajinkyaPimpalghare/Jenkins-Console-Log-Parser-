"""=======================================================================================
INFORMATION ABOUT CODE  Coding Standars: ISO9001:2015
==========================================================================================
For fetching the console output of jenkins job and print it in another job.

Author: Prajinkya Pimpalghare(L&T)

Date: 27-10-2017
Version: 1.0
Input Variable: Target Name| Job_name | Jenkins URL | user details
==========================================================================================="""
from jenkinsapi.jenkins import Jenkins


class JobValidator(object):
    """For fetching the console output for specific job"""

    def __init__(self, target_name, job_name, jenkins_url, user, password):
        """
        Initialising default variables for searching and validating the job.
        :param target_name:
        :param job_name:
        :param jenkins_url:
        :param user:
        :param password:
        """
        self.target_name = target_name
        self.job_name = job_name
        self.url = jenkins_url
        self.user = user
        self.password = password
        self.console_output = ""

    def validator(self):
        """
        It validates the job according to target parameter and prints its console output
        """
        try:
            jenkins = Jenkins(baseurl=self.url, username=self.user,
                              password=self.password, lazy=True)
            job = jenkins.get_job(jobname=self.job_name)
            build_number = job.get_last_buildnumber()
            for i in range(build_number - 5, build_number):  # For last 5 build
                if "Target_Name" in job.get_build(i).get_params() and \
                                job.get_build(i).get_params()["Target_Name"] == self.target_name:
                    self.console_output = job.get_build(i).get_console()
            if self.console_output:
                print(self.console_output)
            else:
                print("Target parameter not found")
        except BaseException as error:
            print("Error : ", error)


if __name__ == '__main__':
    JOB = JobValidator(target_name="target-name", job_name="test_job_name"
                       , jenkins_url="http://myjenkinsurl:portno", user="username",
                       password="password")
    JOB.validator()
