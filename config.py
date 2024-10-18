import os

class Config:
    JENKINS_URL = os.getenv("JENKINS_URL", "http://localhost:8080")
    JENKINS_USER = os.getenv("JENKINS_USER", "admin")
    JENKINS_TOKEN = os.getenv("JENKINS_TOKEN","11277cd5c411a8d5e4bc281a170a805bc7")
    # JENKINS_JOB_NAME = os.getenv("JENKINS_JOB_NAME","my-sil-ci-job")
    JENKINS_JOB_NAME = os.getenv("JENKINS_JOB_NAME", "GithubPipeline")
    # JENKINS_JOB_NAME = os.getenv("JENKINS_JOB_NAME", "NewPipeline")
    # JENKINS_JOB_NAME = os.getenv("JENKINS_JOB_NAME", "JenkinPipeline")