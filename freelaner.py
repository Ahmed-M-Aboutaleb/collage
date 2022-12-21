from os import path, listdir, mkdir

dbJobs = "database/jobs"
dbProposals = "database/proposals"

# This function will get all jobs from the database
# name: the name of the freelancer

def getAllJobs(name):
    if not path.exists(f"{dbJobs}/jobs.txt"):
        print("❌ | There is no jobs right now")
        return main()
    jobsFile = open(f"{dbJobs}/jobs.txt")
    jobs = jobsFile.readlines()
    for job in jobs:
        print(job.split("\n")[0])
    return main(name)

# This function will find a job by title
# title: the title of the job
# name: the name of the freelancer

def findJobByTitle(title, name):
    for nameFromDir in listdir(dbJobs):
        if path.isdir(f"{dbJobs}/{nameFromDir}"):
            titleFromDir = nameFromDir.split("-")[0]
            if titleFromDir == title:
                job = open(f"{dbJobs}/{nameFromDir}/{title}.txt")
                jobData = job.readlines()
                description = jobData[2].split("\n")[0]
                skills = jobData[3].split("\n")[0]
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Skills: {skills}")
    return main(name)

# This function will validate the job title
# title: the title of the job

def validateTitle(title):
    if(title == ""):
        print("❌ | Invalid title")
        return True
    if not path.exists(f"{dbJobs}/jobs.txt"):
        print("❌ | There is no jobs right now")
        return True

# This function will validate the job title
# title: the title of the job

def validateJob(title):
    jobsFile = open(f"{dbJobs}/jobs.txt")
    jobs = jobsFile.readlines()
    for job in jobs:
        if job.split("\n")[0] == title:
            return True
    print("❌ | Job not found")
    return False

# This function will search for a job
# name: the name of the freelancer

def searchJobs(name):
    title = input("Enter job title: ")
    if validateTitle(title):
        return searchJobs()
    if validateJob(title):
        findJobByTitle(title, name)
    return main(name)

# This function will add a proposal to the database
# name: the name of the freelancer

def addProposal(name):
    title = input("Enter job title: ")
    if validateTitle(title):
        return addProposal()
    if not validateJob(title):
        return addProposal()
    skill = input("Enter your perfect skill: ")
    if skill == "":
        print("❌ | Invalid skill")
        return addProposal()
    if not path.exists(dbProposals):
        mkdir(dbProposals)
    if path.exists(f"{dbProposals}/{name}-{title}.txt"):
        print("❌ | You already have a proposal for this job")
        return main(name)
    proposal = open(f"{dbProposals}/{name}-{title}.txt", "w")
    proposal.write(f"{name}\n{title}\n{skill}\nPending")
    proposal.close()
    print("✅ | Proposal added")
    return main(name)

# This function will get all the proposals of the freelancer
# name: the name of the freelancer

def getMyProposals(name):
    if not path.exists(dbProposals):
        print("❌ | You don't have any proposals")
        return main(name)
    proposals = listdir(dbProposals)
    for proposal in proposals:
        if proposal.split("-")[0] == name:
            proposalFile = open(f"{dbProposals}/{proposal}")
            proposalData = proposalFile.readlines()
            title = proposalData[1].split("\n")[0]
            skill = proposalData[2].split("\n")[0]
            status = proposalData[3].split("\n")[0]
            print(f"Title: {title}")
            print(f"Skill: {skill}")
            print(f"Status: {status}")
    return main(name)

# Main function - this function will be called when the user logs in and it freelancer
# It will show the client options and call the functions based on the option selected
# name: the name of the freelancer

def main(name):
    print("(1) All job posts \n(2) Search in job posts \n(3) Add proposal \n(4) My proposals")
    option = input("Select option: ")
    if option == "1":
        getAllJobs(name)
    elif option == "2":
        searchJobs(name)
    elif option == "3":
        addProposal(name)
    elif option == "4":
        getMyProposals(name)
    else:
        print("❌ | Invalid option")
        return main(name)