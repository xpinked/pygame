print(
"""
###
WELCOME TO HELL
Ha KDDING, THIS IS A MONOTONIC SUB SEQUENCES CHECKER
AND IF ITS A CONVEGING SEQUENCE, ALSO GIVES ESTIMATION
FOR THE LIMIT
ENJOY!
Credit: Pinkie
###
""");
#Please Define your Sequence Here:
def My_n_Place(var1,k):
    import decimal
    decimal.getcontext().prec = 1000
    x=decimal.Decimal(var1)

    for i in range(1,k):
        x = decimal.Decimal(3)-x.sqrt()

    return x

#Your sub sequence holder
Increasing=[]
Decreasing=[]
#Checks Your Seuqnece Elements for its Monotonic Behavior
#And adds to the sub sequences holder
for i in range(1,100):
	if My_n_Place(1,i)<My_n_Place(1,i+1):
		Increasing.append("a%d" %(i))
	else:
		Decreasing.append("a%d" %(i))
#When Finsishes prints your sub sequence
if len(Increasing)== 0 and len(Decreasing) == 0:
        print "There Are no Monotonic Sub Sequences"
else:
        print "Here Is Your Increasing Sub_Sequence: \n",Increasing
        print "Here Is Your Decreasing Sub_Sequence: \n",Decreasing
#Cheks for the Limit, only for Converging Sequences        
while True:
        Limit=raw_input("""Would you like to check the limit?\n***Works only if your Sequence Converge***\n""")
        if Limit in ['yes','y','Yes','YES']:
                print My_n_Place(1,i+1000)
                break
        else:
                print "My Work here is Done."
                break
