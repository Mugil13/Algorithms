def advisorPrefersScholar(prefer, advisor, scholar, current_scholar):
    for i in range(no_scholars):
        if prefer[advisor][i] == current_scholar:
            return False
        if prefer[advisor][i] == scholar:
            return True
    return False

def galeShapley(prefer):
    advisor_match = [-1 for _ in range(no_scholars)]
    scholar_free = [False for _ in range(no_scholars)]
    free_scholars_count = no_scholars

    while free_scholars_count > 0:
        scholar = 0
        while scholar < no_scholars:
            if not scholar_free[scholar]:
                break
            scholar += 1

        for i in range(no_scholars):
            if scholar_free[scholar]:
                break
            advisor = prefer[scholar][i]
            advisor_index = advisor - no_scholars
            if advisor_match[advisor_index] == -1:
                advisor_match[advisor_index] = scholar
                scholar_free[scholar] = True
                free_scholars_count -= 1
            else:
                current_scholar = advisor_match[advisor_index]
                if advisorPrefersScholar(prefer, advisor, scholar, current_scholar):
                    advisor_match[advisor_index] = scholar
                    scholar_free[scholar] = True
                    scholar_free[current_scholar] = False

    print("\nResearch Scholars \t Advisors")
    for i in range(no_scholars):
        print(advisor_match[i], "\t\t\t", i + no_scholars)

no_scholars = int(input("Enter the number of scholars: "))

research_scholars = []
advisors = []

for i in range(no_scholars):
    research_scholars.append(i)
for k in range(no_scholars, 2 * no_scholars):
    advisors.append(k)

print("Research scholars are: ", research_scholars)
print("Advisors/Guides are: ", advisors)

print("\n")
prefer = []
for i in range(2 * no_scholars):
    prefs = list(map(int, input(f"Enter preferences for {'research scholar' if i < no_scholars else 'advisor'} {i % no_scholars + 1}: ").split()))
    prefer.append(prefs)

galeShapley(prefer)
