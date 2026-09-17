# 42. Student Performance File Analyzer
#
# Read student records from a text file containing `name,subject,marks`. Handle
# malformed records without crashing. Produce student totals/averages,
# topper, subject-wise averages, grade distribution, and write a summary report to a new file.
#
# Concepts: File handling, dictionaries, comprehensions, functions, exceptions
print("NOTE THIS STDUENT RECORDS ONLY ACCEPT SUBJECTS TILL 3 TO 5 DO NOT GIVE BELOW OR ABOVE SUBJECTS")
print("Please give record format like (Name,Subject1,Marks,Subject2,Marks,Subject3,Marks,Etc....")
from os import path
summary="Summary.txt"
class SubjectLimitExceedError(Exception):
     pass
class StudentRecord():
       def __init__(self,filex):
           self.file = filex
           self.studentrecords = {}
           self.dump = []
           self.avgofstudent={}
           self.gradedistribution={}

       def isfileon(self):
           try:
               if path.exists(self.file):
                   return True
               else:
                   raise FileNotFoundError

           except FileNotFoundError:
               print("File not found")
               return False

       def FileReader(self):
           with open(self.file,"r") as f :
               x=f
               for i in x.readlines() :
                   self.dump.append(i.strip())
           try:
               for i in self.dump:
                   x=i.split(",")
                   if len(x)==7:
                       self.studentrecords[x[0]]={x[1]:int(x[2]),x[3]:int(x[4]),x[5]:int(x[6])}
                   elif len(x)==9:
                       self.studentrecords[x[0]] = {x[1]: int(x[2]), x[3]: int(x[4]), x[5]: int(x[6]),x[7]:int(x[8])}
                   elif len(x)==11:
                       self.studentrecords[x[0]] = {x[1]: int(x[2]), x[3]: int(x[4]), x[5]: int(x[6]), x[7]: int(x[8]),x[9]:int(x[10])}
                   elif len(x)>11:
                       print("This records only accept subjects until 3 to 5 do not give 6 subjects please")
                       raise SubjectLimitExceedError

                   x.clear()
           except IndexError:
               print("Please give the format like")
               print("Name,subject1,marks,subject2,marks,subject3,marks")
           except SubjectLimitExceedError:
               print("Please give Student Record in proper mentioned Format")
           except Exception:
               print("Something went wrong please try again later")
       def topper(self):
            sumx=0
            checker=0
            topper={}
            for k,v in self.studentrecords.items():
                sumx = 0
                for i,w in v.items():
                    sumx=sumx+w
                if sumx > checker:
                    checker=sumx
                    topper.clear()
                    topper[k]=sumx

            print("Topper = ",topper)
            with open (summary,"a") as f:
               f.write(f"Topper in current batch is {topper}\n")
       def average(self):
            avg=0
            i=0
            for k,v in self.studentrecords.items():
                for x , w in v.items():
                    avg+=w
                    i+=1
                self.avgofstudent[k]=avg/i
                avg=0
                i=0

            print(self.avgofstudent)
            with open(summary,"a") as f:
                f.write(f"{self.avgofstudent}\n")
       def subjectwiseavg(self):
           avg=0
           i=0
           avgofs=0
           avgofmath=0
           s=0
           m=0
           for k , v in self.studentrecords.items():
               for x,y in v.items():
                 if x == "English":
                     avg+=y
                     i += 1
                 elif x=="Science":
                     avgofs+=y
                     m+=1
                 elif x == "Math":
                     avgofmath+=y
                     s+=1

           avg=avg/i
           avgofs=avgofs/m
           avgofmath=avgofmath/s
           print(f"Total average of English ={avg}")
           print(f"Total Average of Science ={avgofs}")
           print(f"Total Average of math ={avgofmath}")

       def grades(self):
           for k , v in self.avgofstudent.items():
               if v >= 90:
                   self.gradedistribution[k]="A"
               elif v>=80:
                   self.gradedistribution[k] = "B"
               elif v>=60 :
                   self.gradedistribution[k] = "C"
               elif v>=40:
                   self.gradedistribution[k] = "D"
               elif v < 40:
                   self.gradedistribution[k] = "FAIL"
           for k ,v in self.gradedistribution.items():
               print(f"{k} Grade = {v}")
               if v !="FAIL":
                   with open(summary, "a") as f:
                       f.write(f"Student {k} Has {v} Grade \n")
               else:
                   with open(summary, "a") as f:
                       f.write(f"Student {k} Has failed \n")






x=StudentRecord("StudentxxRecord.csv")
if x.isfileon():
    x.FileReader()
    # x.topper()
    # x.average()
    # x.grades()
    x.subjectwiseavg()
else:
    print("File not exist")