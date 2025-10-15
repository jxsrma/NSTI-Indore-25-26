# And Operator
# Passing for P is 60 and T is 33
P = 70
T = 60

Pass = (P >= 60) and (T >= 33)

print("Result of Trainee: ", Pass)

# Or Operator

Aadhar = False
PAN = False
Voter = False

eligible = Aadhar or PAN or Voter
print("Creating ID: ", eligible)

# Not
# Re Examination eligibility
re_examination = not Pass
print("Re-examination: ", re_examination)
