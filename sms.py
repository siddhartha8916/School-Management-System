import pandas as pd
import matplotlib.pyplot as plt

path = "F:\Student_Management_System\students.csv"
term1path = "F:\Student_Management_System\markstermi.csv"
term2path = "F:\Student_Management_System\markstermii.csv"

def Menu():
    print("-------------------------------------------------------------------")
    print("\t\tWELCOME TO SCHOOL MANAGEMENT SYSTEM")
    print("-------------------------------------------------------------------")
    print("Please select from the below options : ")
    print("1. Show all Students Record")
    print("2. Search for a Student")
    print("3. Add a New Student ")
    print("4. Delete a Student ")
    print("5. Update any Student Details")
    print("6. Display Term I Result ")
    print("7. Display Term II Result ")
    print("8. Display / Input Marks of Term - I")
    print("9. Display / Input Marks of Term - II")
    print("10. Display Graphs")

def ShowAllRecord():
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    print("Displaying Record of All Students . . .")
    print()
    print(dfStu)
    

def ShowT1Result():
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    print("Displaying Marks of Term - I ")
    print()
    print(dfTerm1)

def ShowT2Result():
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm',)
    print("Displaying Marks of Term - II ")
    print()
    print(dfTerm2)


def AddStudent():
    adm = int(input("Enter the Admission Number : "))
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    if adm in dfStu.index:
        print("Admission Number",adm,"already alloted to another student. . .")
        print("Try Again . . . ")
    else:
        name = input("Enter Student's Name : ") ; name = name.upper()
        Class = input("Enter Student's Class : ") ; Class = Class.upper()
        father = input("Enter Father's Name : ") ;  father = father.upper()
        mother = input("Enter Mother's Name : ") ; mother = mother.upper()
        
        con = True
        while (con==True):
            contact = int(input("Enter the Contact Number : "))
            if len(str(contact))!=10:
                print("Enter 10 digit contact number ...")
                print("Try Again . . .")
            else:
                con = False

        con=True
        while (con==True):
            DOB = input("Enter the Date of Birth (DD-MM-YYYY) :")
            if len(DOB) != 10:
                print("Enter Date of Birth as DD-MM-YYYY")
                print("Try Again . . .")
            else:
                con=False

        gender = input("Gender (Male/Female) : "); gender = gender.upper()
        address = input("Enter the Address : "); address = address.upper()

        dfStu.at[adm,:] = [name,Class,father,mother,contact,DOB,gender,address]
        dfStu.to_csv(path)

        dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
        dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
        dfTerm1.at[adm,:] = [name,Class,0,0,0,0,0]
        dfTerm2.at[adm,:] = [name,Class,0,0,0,0,0]
        dfTerm1.to_csv(term1path)
        dfTerm2.to_csv(term2path)
        print("Student Added Successfully. . .")


def StudentSearch():
    print("Press 1 for searching by Name")
    print("Press 2 for searching by Admission Number")
    ch = int(input("Enter your choice : "))
    if ch==1:
        name = input("Enter Student's Name : ") ; name = name.upper()
        dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
        df = dfStu.loc[dfStu["name"]==name]
        if df.empty:
            print("Student doesnot exist ...")
        else:
            print("Student details are as below : ")
            print(df)
            
    elif ch==2:
        adm = int(input("Enter the Admission Number : "))
        dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
        if adm in dfStu.index:
            df = dfStu.loc[adm]
            print("Student Details are as below : \n")
            print(df)
        else:
            print("No Student Exists with the above mentioned Admission Number ...")
    else:
        print("Invalid Choice . . .")


def DeleteStudent():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    df = dfStu.loc[dfStu["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df[['name','class','father','mother']])
    adm = int(input("Enter the Admission Number to be deleted : "))
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
    dfStu = dfStu.drop(adm,axis=0)
    dfTerm1 = dfTerm1.drop(adm,axis=0)
    dfTerm2 = dfTerm2.drop(adm,axis=0)
    dfTerm1.to_csv(term1path)
    dfTerm2.to_csv(term2path)
    dfStu.to_csv(path)
    print("Student Deleted Successfully. . .")
    

def UpdateStudentDetails():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
    df = dfStu.loc[dfStu["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df)
    adm = int(input("Enter the Admission Number to be updated : "))
    print("Enter from below options : \nName\nClass\nFather\nMother\nContact\nDOB\nGender\nAddress")
    change = input("Enter your choice : ") ; change =change.lower()
    
    if change == 'name':
        name = input("Enter Student's Updated Name : ") ; name = name.upper()
        dfStu.loc[adm,[change]] = name
        dfTerm1.loc[adm,[change]] = name
        dfTerm2.loc[adm,[change]] = name
    elif change == 'class':
        Class = input("Enter Student's Updated Class : ") ; Class = Class.upper()
        dfStu.loc[adm,[change]] = Class
        dfTerm1.loc[adm,[change]] = Class 
        dfTerm2.loc[adm,[change]] = Class
    elif change =='father':
        father = input("Enter Father's Name : ") ;  father = father.upper()
        dfStu.loc[adm,[change]] = father
        
    elif change == 'mother':
        mother = input("Enter Mother's Name : ") ; mother = mother.upper()
        dfStu.loc[adm,[change]] = mother
        
    elif change == 'contact':
        con = True
        while (con==True):
            contact = int(input("Enter the Contact Number : "))
            if len(str(contact))!=10:
                print("Enter 10 digit contact number ...")
                print("Try Again . . .")
            else:
                dfStu.loc[adm,[change]] = contact
                con = False
                
    elif change == 'dob':
        con=True
        while (con==True):
            DOB = input("Enter the Date of Birth (DD-MM-YYYY) :")
            if len(DOB) != 10:
                print("Enter Date of Birth as DD-MM-YYYY")
                print("Try Again . . .")
            else:
                con=False
                dfStu.loc[adm,[change]] = DOB
              
    elif change == 'gender':
        gender = input("Gender (Male/Female) : "); gender = gender.upper()
        dfStu.loc[adm,[change]] = gender

    elif change == 'address':
        address = input("Enter the Address : "); address = address.upper()
        dfStu.loc[adm,[change]] = address

    else:
        print("Wrong Choice . . .")
            
    dfTerm1.to_csv(term1path)
    dfTerm2.to_csv(term2path)
    dfStu.to_csv(path)
    print("Student Details Updated Sucessfully . . .")

def UpdateTerm1Marks():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    df = dfTerm1.loc[dfTerm1["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df[['name','class']])
        adm = int(input("Enter the Admission Number of the Student : "))
        df = df.loc[adm,:]
        print(df)
        ch = input("Do you want to update the marks (Y/N) : ") ; ch = ch.upper()
        if ch=='Y':
            name = df['name']
            Class = df['class']
            eng = float(input("Enter the marks in English : "))
            hindi = float(input("Enter the marks in Hindi : "))
            maths = float(input("Enter the marks in Maths : "))
            sci = float(input("Enter the marks in Science : "))
            sst = float(input("Enter the marks in SST : "))
            dfTerm1.loc[adm,:]=[name,Class,eng,hindi,maths,sci,sst]
            dfTerm1.to_csv(term1path)
            print("Marks added successfully . . .")
        else:
            print("Thanks . . .")
    

def UpdateTerm2Marks():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
    df = dfTerm2.loc[dfTerm2["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df[['name','class']])
        adm = int(input("Enter the Admission Number of the Student : "))
        df = df.loc[adm,:]
        print(df)
        ch = input("Do you want to update the marks (Y/N) : ") ; ch = ch.upper()
        if ch=='Y':
            name = df['name']
            Class = df['class']
            eng = float(input("Enter the marks in English : "))
            hindi = float(input("Enter the marks in Hindi : "))
            maths = float(input("Enter the marks in Maths : "))
            sci = float(input("Enter the marks in Science : "))
            sst = float(input("Enter the marks in SST : "))
            dfTerm2.loc[adm,:]=[name,Class,eng,hindi,maths,sci,sst]
            dfTerm2.to_csv(term2path)
            print("Marks added successfully . . .")
        else:
            print("Thanks . . .")
         

def ShowGraphs():
    print()
    print("Select from the below option . . . \n")
    print("1. Student's Location Graph ")
    print("2. Class Count Graph ")
    print("3. Gender Graph ")
    print("4. Term - I Class Wise Marks ")
    print("5. Term - II Class Wise Marks ")
    print("6. Individual Student Term - I Graph ")
    print("7. Individual Student Term - II Graph ")
    print("8. School Academic Graph ")
    op = int(input("Enter Your Choice : "))
    if op==1:
        StuLocGraph()
    elif op==2:
        StuClassCount()
    elif op==3:
        StuGender()
    elif op==4:
        ClassTerm1Graph()
    elif op==5:
        ClassTerm2Graph()
    elif op==6:
        StuTerm1Graph()
    elif op==7:
        StuTerm2Graph()
    elif op==8:
        SchAcadGraph()
    else:
        print("Invalid Choice . . . ")


def StuLocGraph():
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    df = dfStu['address'].value_counts()
    print(df)
    df.plot(kind='barh',color=['r','b','g','y','c','m'],width=0.9)
    plt.title("Student Address Graph")
    plt.xlabel("No. of Students ")
    plt.ylabel("Location")
    plt.show()

def StuClassCount():
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    df = dfStu['class'].value_counts()
    print(df)
    df.plot(kind='line',color=['b','r','y','g','m','c'],marker='D',linestyle='-.')
    plt.title("Class Count")
    plt.xlabel("Classes ")
    plt.ylabel("No. of students")
    plt.show()

def StuGender():
    dfStu = pd.read_csv(path,index_col = 'adm',\
                usecols = ['adm','name','class','father','mother','contact','dob','gender','address'])
    df = dfStu['gender'].value_counts()
    print(df)
    df.plot(kind='bar',color=['y','g'],width=0.9)
    plt.title("Gender Count")
    plt.xlabel("Gender ")
    plt.ylabel("No. of students")
    plt.grid(True)
    plt.show()

def ClassTerm1Graph():
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    Class = input("Enter the class : ") ; Class = Class.upper()
    df = dfTerm1.loc[dfTerm1["class"]==Class]
    print(df)
    df.plot(kind='bar',x='name')
    plt.xlabel("Student's Name")
    plt.ylabel("Marks Scored out of 60")
    plt.title("Term - I Marks Analysis of Class "+Class)
    plt.show()

def ClassTerm2Graph():
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
    Class = input("Enter the class : ") ; Class = Class.upper()
    df = dfTerm2.loc[dfTerm2["class"]==Class]
    print(df)
    df.plot(kind='bar',x='name')
    plt.xlabel("Student's Name")
    plt.ylabel("Marks Scored out of 60")
    plt.title("Term - II Marks Analysis of Class "+Class)
    plt.show()

def StuTerm1Graph():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm')
    df = dfTerm1.loc[dfTerm1["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df[['name','class']])
        adm = int(input("Enter the Admission Number of the Student : "))
        df = df.loc[adm,['eng','hindi','maths','science','sst']]
        df.plot(kind='bar',color=['r','g','c','m','y'],width=0.8)
        plt.title("Term - I Marks Report of "+name)
        plt.xlabel("Subjects")
        plt.ylabel("Marks Scored out of 60")
        plt.show()


def StuTerm2Graph():
    name = input("Enter Student's Name : ") ; name = name.upper()
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm')
    df = dfTerm2.loc[dfTerm2["name"]==name]
    if df.empty:
        print("Student doesnot exist ...")
    else:
        print("Student details are as follows : ")
        print(df[['name','class']])
        adm = int(input("Enter the Admission Number of the Student : "))
        df = df.loc[adm,['eng','hindi','maths','science','sst']]
        df.plot(kind='bar',color=['r','g','c','m','y'],width=0.8)
        plt.title("Term - II Marks Report of "+name)
        plt.xlabel("Subjects")
        plt.ylabel("Marks Scored out of 60")
        plt.show()
        
def SchAcadGraph():
    dfTerm1 = pd.read_csv(term1path,index_col = 'adm',\
                          usecols = ['adm','eng','hindi','maths','science','sst'])
    dfTerm2 = pd.read_csv(term2path,index_col = 'adm',\
                          usecols = ['adm','eng','hindi','maths','science','sst'])
    df = dfTerm1+dfTerm2
    df2 = df.mean()
    df2.plot(kind='bar',color=['r','g','c','m','y'],width=0.8,edgecolor='black',linestyle='--')
    plt.xlabel("Subjects")
    plt.ylabel("Average")
    plt.title("School Academic Performance",fontsize=20)
    plt.show()


    
while True:
    print()
    print()
    Menu()
    ch = int(input("Enter your choice : "))
    if ch==1:
        ShowAllRecord()
    elif ch==2:
        StudentSearch()
    elif ch==3:
        AddStudent()
    elif ch==4:
        DeleteStudent()
    elif ch==5:
        UpdateStudentDetails()
    elif ch==6:
        ShowT1Result()
    elif ch==7:
        ShowT2Result()
    elif ch==8:
        UpdateTerm1Marks()
    elif ch==9:
        UpdateTerm2Marks()
    elif ch==10:
        ShowGraphs()
    else:
        print("Wrong Choice . . .")
        break
 

input()
