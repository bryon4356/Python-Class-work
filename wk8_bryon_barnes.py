# This is the flower box and it should at the beginning of each assignment
# Program name : Wk8_bryon_barnes.py
# Student Name : bryon barnes
# Course : ENTD220
# Instructor : david gunderman
# Date : 1/29/23
# Copy Wrong : This is my work
# Description : This code will be a looping calculator where it has a lower and higher range. Will not allow division by zero.

# Copy Wrong : This is my work

def calc():
    try:
        import Mylib
        lv=float(input("Enter Low Range Value: "))
        hv=float(input("Enter High Range Value: "))
        n1=float(input("Enter First Value: "))
        n2=float(input("Enter Second Value: "))
        operation=str(input("enter problem string like this n1,n2,operator"))
        choices=["1)add","2)sub","3)multiply","4)divide","5)scalc","6)all in one","7)write to file","8)read from file"]
        print(choices)
        user_choice=input("enter a number for the operation")
        calc1=Mylib.calc1()
        myfile=Mylib.WrFile()
        res={
            '+':calc1.add(n1,n2),
            '-':calc1.sub(n1,n2),
            '*':calc1.mult(n1,n2),
            '/':calc1.div(n1,n2)
            }
    except ValueError:
            print("You must enter a number")
    else:
        if n1>=lv and n2<=hv:
            if user_choice=='1':
                print(res['+'])
            elif user_choice=='2':
                print(res['-'])
            elif user_choice=='3':
                print(res['*'])
            elif user_choice=='4':
                try:
                    print(res['/'])
                except ZeroDivisionError:
                    print("you cant divide by zero")
            elif user_choice=='5':
                import Mylib
                print(calc1.scalc(operation))
            elif user_choice=='6':
                import Mylib
                print(res,calc1.sclac(operation))
            elif user_choice=='7':
                myfile.writeF(str(res),str(calc1.scalc(operation)))
            elif user_choice=='8':
                myfile.readf()
                
        else:
            import Mylib
            print(calc.isin(lv,hv,n1,n2))
        again()
def again():
    calc_again=str(input("do you want to calculate again? (Y/N):"))
    if calc_again=='y':
        calc()
    elif calc_again=='n':
        print("thanks for using my calculator")
    else:
        quit()
calc()
        
