from os import path, makedirs, remove, rmdir, listdir
from uuid import uuid4

db = "database/jobs"
dbProposals = "database/proposals"

# getFreelancers() - list all freelancers on the system
# From the freelancers.txt file, read all freelancers and print them
# name - the client name

def getFreelancers(name):
    if not path.exists("database/users/freelancers.txt"):
        print("❌ | There is no freelancers on the system")
        return main(name)
    freelancersFile = open("database/users/freelancers.txt")
    freelancers = freelancersFile.readlines()
    for freelancer in freelancers:
        print(freelancer.split("\n")[0])
    return main(name)

# addJob() - add a job to the system
# The function will ask the user to enter the job title, description and required skills
# The function will create a folder with the job title and the client name
# The function will create a file with the job title and the client name
# The function will write the job title, description, required skills
# The function will add the job title to the jobs.txt file
# name - the client name

def addJob(name):
    if not path.exists(db):
        makedirs(db)
    id = uuid4()
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    skills = input("Enter required skills (skill 1, skill 2, ...): ")
    if path.exists(f"{db}/{title}-{name}"):
        print("❌ | There is job with that title")
        return addJob()
    makedirs(f"{db}/{title}-{name}")
    fileName = f"{db}/{title}-{name}/{title}.txt"
    jobFile = open(fileName, "w")
    jobFile.writelines(f"{id}\n{title}\n{description}\n{skills}\n")
    jobFile.close()
    if not path.exists(f"{db}/jobs.txt"):
        jobsFile = open(f"{db}/jobs.txt", "w")
        jobsFile.writelines(f"{title}\n")
        jobsFile.close()
    else:
        jobsFile = open(f"{db}/jobs.txt", "a")
        jobsFile.writelines(f"{title}\n")
        jobsFile.close()
    print("✅ | Job added")
    return main(name)

# removeJob() - remove a job from the system
# The function will ask the user to enter the job title
# The function will remove the job folder
# The function will remove the job title from the jobs.txt file
# name - the client name

def removeJob(name):
    title = input("Enter job title: ")
    job = f"{db}/{title}-{name}"
    if not path.exists(job):
        print("❌ | This job doesn't exists")
        return removeJob(name)
    remove(f"{job}/{title}.txt")
    rmdir(job)
    jobsMainFileRead = open(f"{db}/jobs.txt", "r")
    data = jobsMainFileRead.readlines()
    jobsMainFileWrite = open(f"{db}/jobs.txt", "w")
    for line in data:
        if line.split("\n")[0] != title:
            jobsMainFileWrite.write(line)
    print("✅ | Job removed")
    return main(name)

# getJobs() - list all jobs for a client
# The function will ask the user to enter the client name
# The function will list all jobs for the client
# name - the client name

def getJobs(name):
    for nameFromDir in listdir(db):
        if path.isdir(f"{db}/{nameFromDir}"):
            client = nameFromDir.split("-")[1]
            if client == name:
                print(nameFromDir.split("-")[0])
    option = input("Enter job title to view its proposals: ")
    getProposals(option, name)
    return main(name)

# getProposals() - list all proposals for a job
# The function will ask the user to enter the job title
# The function will list all proposals for the job
# job - the job title
# name - the client name

def getProposals(job, name):
    if not path.exists(dbProposals):
        print("❌ | There is no proposals")
        return main(name)
    for proposal in listdir(dbProposals):
        titleJob = proposal.split("-")[1]
        titleJob = titleJob.split(".")[0]
        print(titleJob)
        print(job)
        if job == titleJob:
            proposalFile = open(f"{dbProposals}/{proposal}")
            proposalData = proposalFile.readlines()
            freelancer = proposalData[0].split("\n")[0]
            skill = proposalData[2].split("\n")[0]
            status = proposalData[3].split("\n")[0]
            print(f"Freelancer name: {freelancer}")
            print(f"Skill: {skill}")
            print(f"Status: {status}")
            print("--------------------")
            proposalFile.close()
        else:
            print("❌ | There is no proposals for this job")
            return main(name)
    selectProposal(job, name)

# selectProposal() - select a proposal for a job
# The function will ask the user to enter the freelancer name
# The function will change the proposal status to "Accepted" or "Rejected"
# job - the job title
# name - the client name

def selectProposal(job, name):
    freelancer = input("Enter freelancer name to accept/reject his proposal: ")
    option = input("Enter 1 to accept or 2 to reject: ")
    if option != "1" and option != "2":
        print("❌ | Invalid option")
        return selectProposal(job, name)
    if not path.exists(f"{dbProposals}/{freelancer}-{job}.txt"):
        print("❌ | This proposal doesn't exists")
        return selectProposal(job, name)
    proposalFile = open(f"{dbProposals}/{freelancer}-{job}.txt")
    proposalData = proposalFile.readlines()
    if option == "2":
        proposalData[3] = "Rejected"
    elif option == "1":
        proposalData[3] = "Accepted"
    proposalFileWrite = open(f"{dbProposals}/{freelancer}-{job}.txt", "w")
    proposalFileWrite.writelines(proposalData)
    proposalFileWrite.close()
    print("✅ | Proposal accepted/rejected")
    return main(name)


# Main function - this function will be called when the user logs in and it client
# It will show the client options and call the functions based on the option
# name - the client name

def main(name):
    print("(1) List all freelancers \n(2) Add job \n(3) Remove job \n(4) View your jobs")
    option = input("Select option: ")
    if option == "1":
        getFreelancers(name)
    elif option == "2":
        addJob(name)
    elif option == "3":
        removeJob(name)
    elif option == "4":
        getJobs(name)
    else:
        print("❌| Invalid option")
        return main(name)