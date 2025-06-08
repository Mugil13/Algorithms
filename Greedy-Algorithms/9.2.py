def jobScheduling(jobs, time):
    size = len(jobs)
    for i in range(size):
        for j in range(size - 1 - i):
            if jobs[j][2] < jobs[j + 1][2]:
                jobs[j], jobs[j + 1], = jobs[j + 1], jobs[j]
    
    time_slot = [False] * time
    sequence = ['-1'] * time
    total_profit = 0
    
    for i in range(len(jobs)):
        for j in range(min(time - 1, jobs[i][1] - 1), -1, -1):
            if time_slot[j] is False:
                time_slot[j] = True
                sequence[j] = jobs[i][0]
                total_profit += jobs[i][2]
                break
    return sequence, total_profit

numberOfJobs = int(input("Enter the number of jobs: "))
print("\n")
jobs = []
deadline_list = []
for i in range(numberOfJobs):
    job = []
    jobName = str(input("Enter the job name: "))
    deadline = int(input("Enter the deadline: "))
    deadline_list.append(deadline)
    profit = int(input("Enter the profit: "))
    job.append(jobName)
    job.append(deadline)
    job.append(profit)
    jobs.append(job)
    print("\n")

timeLimit = max(deadline_list)
resultSequence, maxProfit = jobScheduling(jobs, timeLimit)
print("JOB SEQUENCE: ", resultSequence)
print("MAXIMUM PROFIT: ", maxProfit)
