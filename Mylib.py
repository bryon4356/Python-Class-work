# This is the flower box and it should at the beginning of each assignment
# Program name : Wk7_bryon_barnes_mylib.py
# Student Name : bryon barnes
# Course : ENTD220
# Instructor : david gunderman
# Date : 1/20/23
# Copy Wrong : This is my work
# Description : This code will be a looping calculator where it has a lower and higher range. Will not allow division by zero.

# Copy Wrong : This is my work
class calc1:
   def add(self,x,y):
      answer=x+y
      return answer
   def sub(self,x,y):
      answer=x-y
      return answer
   def mult(self,x,y):
      answer=x*y
      return answer
   def div(self,x,y):
      answer=x/y
      return answer
   def isin(self,lv,hv,n1,n2):
      if n1<=lv:
         return 'the input values are outside the range'
      elif n2>=hv:
         return 'the input values are outside the range'
   def scalc(self,p1):
      istring=p1.split(",")
      if istring[2]=="+":
         res = self.add(int(istring[0]), int(istring[1]))
      elif istring[2]=="-":
         res = self.sub(int(istring[0]), int(istring[1]))
      elif istring[2]=="*":
         res = self.mult(int(istring[0]), int(istring[1]))
      elif istring[2]=="/":
         res = self.div(int(istring[0]), int(istring[1]))
      return res
        
class Wrfile:
   def writeF(self,f,h):
      with open("testfile.txt","w")as out_file:
         out_file.write('These are the results of the previous calculations\n')
         out_file.write(f)
         out_file.writh(h)
   def readF(self):
      f=open("testfile.txt","r")
      if f.mode=="r":
         contents=f.read()
         print(contents)



        
    
        
