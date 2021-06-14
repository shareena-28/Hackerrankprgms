#set.add()
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
print(len(countries))
"""
input(stdin)
7
Uk
China
USA
France
New Zealand
UK
France
Your output(stdout)
5
Expected Output
5
"""
