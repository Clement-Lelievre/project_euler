"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit"""

# observations: the number I'm looking for must end with a 0 and be between 1121314151617181910 and 1929394959697989990
import re


PAT = re.compile(r"^1.2.3.4.5.6.7.8.9.0$")
lower_bound = (int((1121314151617181910**0.5 + 1) / 10) + 1) * 10
upper_bound = int(1929394959697989990**0.5) + 1
for nb in range(lower_bound, upper_bound + 1, 10):
    if PAT.match(str(nb**2)):
        print(nb)
        break
