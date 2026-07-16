subjects=["Maths","java","python","English", "c","c++"]
marks=[]

for i in subjects:
    submarks=int(input(f"{i} :"))
    marks.append(submarks)
for sub,mark in zip(subjects,marks):
    print(sub,";",mark)
max_marks=int(input("Enter maximum marks:"))
def totm(mark):
    return (sum(mark)) 
X=totm(marks)
print("total:",X)
def ave(nums):
    return X/len(nums)
Y=ave(marks)
print("Total average:",Y)
def tot_per(t):
    return X/max_marks * 100
tp=tot_per(marks)
print(" Total percentage:",tp,"%")
def tgrade(total):
    if total >= 90:
        return "Total grade:A Grade"
    elif total >= 75 :
        return  "Total grade:B Grade"
    elif total >= 60:
        return "Total grade:C Grade"
    elif total >= 35:
        return "Total grade:D Grade"
    else:
        if total < 35:
            return "Fail"
print(tgrade(tp))

submaxm=int(input("sub.Maximum marks:"))
print()
def grade(total):
    if total >= 90:
        return "A Grade"
    elif total >= 75 :
        return  "B Grade"
    elif total >= 60:
        return "C Grade"
    elif total >= 35:
        return "D Grade"
    else:
        if total < 35:
            return "Fail"
for sub,mark in zip(subjects ,marks):
    per=(mark/submaxm * 100)
    g=grade(per)
    print(sub)
    print("Marks:",mark)
    print("Sub Percentage:",per,"%")
    print("Sub Grade:",g)
    print()

def failedsub(subj,mar):
    fail_count= 0

    for sub,mark in zip(subjects,marks):
        if mark < 35:
            print(sub,"Fail")
            fail_count +=1
    print("No of failed subj:",fail_count)
failedsub(subjects,marks)

