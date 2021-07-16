# if文

age = 19
age_alchol =20
if age >= age_alchol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer.")
    
age_drive = 18
if age >= age_alchol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive.")
else:
    print("You are not allowed to drink beer but you can drive only if you have driver's lisence.")
    
if not 0 < age < 120:
    print("The value is invalid!")
    
# challenge
balance = 2000000
withdraw = 23000
# if balance > withdraw:
#     balance -= withdraw
#     print("Your new balance id {}".format(balance))
# else:
#     print("You don't have money.")

max_withdraw = 1000000
if withdraw > max_withdraw:
    print("The withdraw limit is {}".format(max_withdraw))
elif balance > withdraw:
    balance -= withdraw
    print("Your new balance id {}".format(balance))
else:
    print("You don't have money.")