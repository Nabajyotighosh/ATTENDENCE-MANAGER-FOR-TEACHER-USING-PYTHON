import datetime
import os
import sqlite3
import time
from array import array
import pyttsx3

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)
engine.setProperty("volume",1000)


clear = lambda:os.system('cls')
def username():
    clear()
    print("                                        *******************************************USERNAME REGISTRATION  PAGE***********************************************")
    a = int(input("\nENTER TEACHER ID(SHOULD BE IN DIGIT):-"))
    ab=str(a)
    MySchool=sqlite3.connect('user.db')
    sql="SELECT * from teacher WHERE Teacherid='"+ab+"';"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    record=curschool.fetchone()
    MySchool.close()
    if record is not None:
        print("\n                         TEACHER ID ALREADY EXISTS!!\n")
        print("\a")
        n=int(input("\n                   PRESS 1 FOR REGISTER NEW USERNAME  2 FOR SIGN UP PAGE:-"))
        if n==1:
            username()
        else:
            login(2)
    b = input("ENTER NAME    :-")
    g = input("ENTER GENDER  :-")
    g=g.lower()
    c = input("ENTER USERNAME:-")
    MySchool=sqlite3.connect('user.db')
    sql="SELECT * from teacher WHERE username='"+c+"';"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    record=curschool.fetchone()
    MySchool.close()
    if record is not None:
        print("\n                         USERNAME ALREADY EXISTS!!\n")
        print("\a")
        n=int(input("\n                   PRESS 1 FOR REGISTER NEW USERNAME  2 FOR SIGN UP PAGE:-"))
        if n==1:
            username()
        else:
            login(2)
    d = input("ENTER PASSWORD:-")
    e = input("RE ENTER PASSWORD:-")
    if e==d:
        fr = input("ENTER FAVOURITE FRUIT(FOR SECUIRITY):-")
        bo= input("ENTER FAVOURITE BOOK NAME(FOR SECUIRITY):-")
        f = input("ENTER BEST FRIEND NAME(FOR SECUIRITY):-")
        MySchool=sqlite3.connect('user.db')
        curschool=MySchool.cursor()  
        curschool.execute("INSERT INTO teacher (Teacherid,name,username,password,gender,book,fruit,friend)VALUES (?,?,?,?,?,?,?,?);", (a,b,c,d,g,bo,fr,f))
        MySchool.commit()
        MySchool.close()
        print("               **USER ID CREATED SUCCESFULLY**        ")
        MySchool.close()
        MySchool=sqlite3.connect(c+'.db')
        curschool=MySchool.cursor()
        curschool.execute('''CREATE TABLE stu (roll INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT (20) NOT NULL,attandance INTEGER NOT NULL);''')
        curschool.execute('''CREATE TABLE  date (sl INTEGER,date TEXT (20) NOT NULL);''')
        MySchool.close()
        time.sleep(2)
        login(2)
    else:
        print("                                                                  PLEASE ENTER SAME PASSWORD IN BOTH CASES!!!!")
        print("\a")
        time.sleep(2)
        username()




def login(li):
    clear()
    print("                                                          ********************************** SIGN UP PAGE*******************************\n")
    if li==1:
        speak("welcome to attendence maneger signup page plese login to use it!!")
    print("                                                                                     1.USER NAME REGISTRATION")
    print("                                                                                     2.LOG IN ")
    print("                                                                                     3.FORGOT PASSWORD")
    print("                                                                                     4.EXIT FROM THE PORTAL\n")
    at = int(input("                                                                                      ENTER CHOICE:-"))
    if at==1:
        username()
    elif at==3:
        forgot()
    elif at==2:
        login2()
    elif at==4:
        exit()
    else:
        speak("please choose option correctly")
        login(2)





def login2():
    clear()
    print("                                                          ********************************** WELCOME TO LOG IN PAGE*******************************\n")
    u = input("ENTER USERNAME:-")
    MySchool=sqlite3.connect('user.db')
    sql="SELECT * from teacher WHERE username='"+u+"';"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    record=curschool.fetchone()
    MySchool.close()
    if record is None:
        print("\n                         USERNAME IS NOT AVAILABLE!!\n")
        print("\a")
        er =int(input("                   PRESS 1 TO GO TO SIGN UP PAGE 2 FOR NEXT ATTEMPT:-"))
        if er==1:
            login(2)
        elif er==2:
            login2()
        else:
            login(2)
    else:
        p = input("ENTER PASSWORD:-")
        MySchool=sqlite3.connect('user.db')
        sql="SELECT * from teacher WHERE username='"+u+"';"
        curschool=MySchool.cursor()
        curschool.execute(sql)
        record=curschool.fetchone()
        MySchool.close()
        if record[3]==p:
            print("\n     PLEASE WAIT A SECOND ......")
            time.sleep(2)
            mainp(record,1)
        else:
            print("\n                      LOG IN FAILED!!")
            print("\a")
            print("\n                      PASSWORD IS INCORRECT!!...")
            print("\n                      PLEASS WAIT A SECOND......")
            time.sleep(2)
            login(2)


def mainp(record,li):
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                   *@*@*@*@*@*@*@*@*@*@*@ WELCOME TO ATTENDENCE MANEGER SOFTWARE @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("welcome to attendence maneger software main page dear sir!!")
        else:
            speak("welcome to attendence maneger software main page dear mam!!")

    print("                                                                                          1.ATTENDENCE MANAGER")
    print("                                                                                          2.DISPLAY ALL STUDENTS ATTENDENCE")
    print("                                                                                          3.DISPLAY ANY STUDENT DETAILS")
    print("                                                                                          4.ENTER NEW STUDENTS DETAILS")
    print("                                                                                          5.CHANGE PASSWORD")
    print("                                                                                          6.DELETE ALL RECORDS")
    print("                                                                                          7.LOG OUT\n")
    gf = int(input("                                                                                           CHOOSE ANY ACTION:-"))
    if gf==6:
        speak(" you have choosen DELETE ALL RECORDS option")
        delete(record,1)
    elif gf==1:
        speak("you have choosen ATTENDENCE MANAGER option")
        attendence(record,1)
    elif gf==2:
        speak("you have choosen DISPLAY ALL STUDENTS ATTENDENCE option")
        display1(record,1)
    elif gf==3:
        speak("you have choosen DISPLAY ANY STUDENT DETAILS option")
        display2(record,1)
    elif gf==4:
        speak("you have choosen NEW STUDENTS DETAILS entry option ")
        entry(record,1)
    elif gf==5:
        speak('you have choosen CHANGE PASSWORD option')
        change(record,1)
    elif gf==7:
        speak("logging out ..please wait")
        login(2)
    else:
        speak("please choose correct option")
        mainp(record,2)


def attendence(record,li):
    apt=1
    am = array('i',[])
    t=0
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                   *@*@*@*@*@*@*@*@*@*@*@  ATTENDENCE MANEGER PAGE @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE  :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is attendence maneger page..sir!!..")
        else:
            speak("this is attendence page ..mam!!..")

    strDate=datetime.date.today()
    MySchool=sqlite3.connect(str(record[2])+'.db')
    sp="SELECT * from date;"
    curschool=MySchool.cursor()
    curschool.execute(sp)
    st=curschool.fetchall()
    for er in st:
        if str(er[1])==str(strDate):
            t=1
    if t==0:
        
        MySchool=sqlite3.connect(str(record[2])+'.db')
        sql="SELECT * from stu;"
        curschool=MySchool.cursor()
        curschool.execute(sql)
        result=curschool.fetchone()
        if result is None:
            print("\n        SORRY NO DETAILS FOUND PLEASE ENTER STUDENTS DETAILS!! ")
            print("\a")
            ar= int(input("\n        PRESS 1 TO ENTER DETAILS OF STUDENT 2 FOR MAIN PAGE:-"))
            if ar==1:
                entry(record,1)
            elif ar==2:
                mainp(record,2)
            else:
                mainp(record,2)
                
        else:
            sql="SELECT * from stu;"
            curschool=MySchool.cursor()
            curschool.execute(sql)
            result=curschool.fetchall()
            print("ENTER 1 FOR PRESENT AND ENTER 0 FOR ABSENT\n")
            print("ROLL NUMBER : NAME OF THE STUDENT : ATTENDENCE")
            for re in result:
                x =int(input(" " +str(re[0])+" "*(11-len(str(re[0])))+": "+str(re[1])+" "*(20-len(str(re[1])))+  ": "))
                am.append(x)
            j=0
            print(am[j])
            for re in result:
                if am[j] ==1 or am[j] ==0:
                    pass
                else:
                    print("                                                       PLEASE ENTER ATTENDENCE CORRECTLY SOME ATTENDENCE HAVE BEEN ENTERED EXCEPT 1 OR 0!!")
                    print("\a")
                    time.sleep(2)
                    apt=25
                    break
                j+=1
            if apt==25:
                attendence(record,2)
            w=int(input("\n                   PRESS 5 FOR SUBMIT THE ATTENDENCE:-"))
            if w==5:
                clear()
                print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
                print("                                                                   *@*@*@*@*@*@*@*@*@*@*@  ATTENDENCE MANEGER PAGE @*@*@*@*@*@*@*@*@*@*@*")
                print("\n")
                print("TEACHER ID   : "+str(record[0]))
                print("TEACHER NAME :"+str(record[1]))
                strDate=datetime.date.today()
                print("TODAY'S DATE :"+str(strDate))
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print("SERVER TIME  :"+str(strTime))
                print("\n")
                print("ROLL NUMBER : NAME OF THE STUDENT : ATTENDENCE")
                i=0
                for re in result:
                    print(" "+str(re[0])+" "*(11-len(str(re[0])))+ ": "+str(re[1])+" "*(20-len(str(re[1])))+": "+str(am[i]))
                    i+=1
                w=int(input("\n              PRESS 6 TO FINAL SUBMIT OF ATTENDENCE 7 FOR TAKING FRESH ATTENDENCE:-"))
                t=1
                if w==6:
                    i=0
                    for re in result:
                        MySchool=sqlite3.connect(str(record[2])+'.db')
                        sq="SELECT * from stu WHERE roll='"+str(re[0])+"';"
                        curschool=MySchool.cursor()
                        curschool.execute(sq)
                        r=curschool.fetchone()
                        aw=am[i]
                        am[i]=int(r[2])+am[i]
                        sql="UPDATE stu SET attandance='"+str(am[i])+"' WHERE roll='"+str(re[0])+"';"
                        curschool.execute(sql)
                        MySchool.commit()
                        curschool=MySchool.cursor()
                        i+=1
                        school=sqlite3.connect(str(re[0])+'.db')
                        cur=school.cursor()
                        cur.execute("INSERT INTO att (date,at)VALUES(?,?);",(strDate,aw))
                        school.commit()
                        school.close()
                    curschool=MySchool.cursor()
                    sp="SELECT * from date;"
                    curschool.execute(sp)
                    st=curschool.fetchone()
                    if st is None:
                        curschool.execute("INSERT INTO date (sl,date)VALUES(0,'nbvjh');")
                        MySchool.commit()
                    sp="SELECT * from date;"
                    curschool.execute(sp)
                    st=curschool.fetchall()
                    for er in st:
                        s=er[0]
                    sl=1+int(s)
                    curschool.execute("INSERT INTO date(sl,date)VALUES(?,?);",(sl,strDate))
                    MySchool.commit()
                    print("\n                         @@@@@@     ATTENDENCE UPDATE COMPLETE     @@@@@")
                    speak("ATTENDENCE UPDATE COMPLETE")
                    time.sleep(2)
                    mainp(record,2)  
                if w==7:
                    t=0
                    attendence(record,2)  
                else:
                    print("\a")
                    attendence(record,2)
    elif t>=1:
        print("\n")
        print("                                                                                          OPPS!!!!!!!")
        print("                                                                     @@@@@@@   ATTENDENCE ALREADY HAS BEEN SUBMITTED!!  @@@@@@@ ")
        print("                                                                                 PLEASE TRY ON  NEXT DATE!!!!!!!!!!")
        print("\a")
        time.sleep(2)
        re=record
        mainp(re,2)



def entry(record,li):
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                         *@*@*@*@*@*@*@*@*@*@*@  STUDENT DETAILS ENTRY PAGE  @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is student details entry page.. sir!!..")
        else:
            speak("this is student details entry page .. mam!!..")

    Q=int(input("                           HOW MANY STUDENTS   :-"))
    print("\n")
    for i in range(Q):
        na=input("                        ENTER STUDENT NAME  :-")
        ro=int(input("                        ENTER ROLL NUMBER   :-"))
        se=input("                        ENTER SEMESTAR      :-")
        ad=input("                        ENTER ADDRESS       :-")
        mo=input("                        ENTER MOBILE NUMBER :-")
        print("\n")
        atu=0
        Myschool=sqlite3.connect(str(record[2])+'.db')
        curschool=Myschool.cursor()
        curschool.execute("INSERT INTO stu(roll,name,attandance)VALUES(?,?,?);",(ro,na,atu))
        Myschool.commit()
        school=sqlite3.connect(str(ro)+'.db')
        curschool=school.cursor()
        curschool.execute("CREATE TABLE detail (roll INTEGER PRIMARY KEY,name TEXT (20) NOT NULL,sem TEXT (10),mob TEXT (15),addres TEXT (20) );")
        curschool.execute("CREATE TABLE att (date TEXT(20),at INTEGER);")
        curschool.execute("INSERT INTO detail (roll,name,sem,mob,addres)VALUES(?,?,?,?,?);",(ro,na,se,mo,ad))
        school.commit()
        curschool.execute("INSERT INTO att (date,at)VALUES(?,?);",(strDate,atu))
        school.commit()
        school.close()
    print("\n                                        @@@@@@@@  RECORD UPDATED SUCCESSFULLY @@@@@@@@")
    speak("RECORD UPDATED SUCCESSFULLY")
    time.sleep(3)
    mainp(record,2)


def display1(record,li):
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                   *@*@*@*@*@*@*@*@*@*@*@       STUDENTS ATTENDENCE DETAILS PAGE      @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is student  attendence details  page..sir!!")
        else:
            speak("this is student attendence  details page  ..mam!!")
    MySchool=sqlite3.connect(str(record[2])+'.db')
    sp="SELECT * from date;"
    curschool=MySchool.cursor()
    curschool.execute(sp)
    st=curschool.fetchone()
    if st is None:
        print("                                                                         !!!! NO ATTENDENCE TAKEN TILL NOW !!!!")
        print("\a")
        time.sleep(2)
        mainp(record,2)
    sql="SELECT * from stu;"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    result=curschool.fetchone()
    if result is None:
        print("\n                                   SORRY NO DETAILS FOUND PLEASE ENTER STUDENTS DETAILS!! ")
        print("\a")
        ar= int(input("\n                       PRESS 1 TO ENTER DETAILS OF STUDENT 2 FOR MAIN PAGE:-"))
        if ar==1:
            entry(record,1)
        elif ar==2:
            mainp(record,2)
        else:
            mainp(record,2)
    else:
        sql="SELECT * from stu;"
        curschool=MySchool.cursor()
        curschool.execute(sql)
        result=curschool.fetchall()
        sq="SELECT * from date"
        curschool=MySchool.cursor()
        curschool.execute(sq)
        r=curschool.fetchall()
        for d in r:
            sl=d[0]
        print("                                                                                                 STUDENT DETAILS\n ")
        print("                                                                             ROLL NUMBER : NAME OF THE STUDENT : ATTENDENCE : PERCENTAGE")
        for re in result:
            pe=(int(re[2])/sl)*100
            print("                                                                                 "+str(re[0])+" "*(11-len(str(re[0])))+ ": "+str(re[1])+" "*(20-len(str(re[1])))+": "+str(re[2])+" "*(11-len(str(re[2])))+": "+str(pe)+" %")
        print("\n                                                                                   TOTAL CLASS TAKEN  "+str(sl)+"  UPTO DATE:  "+str(d[1]))
        print("\n")
        AS=int(input("                                                                              PLEASE PRESS 1 TO GO BACK TO MAIN PAGE:-"))    
        if AS==1:
            mainp(record,2)
        else:
            mainp(record,2)


def display2(record,li):
    clear()
    t=1
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                         *@*@*@*@*@*@*@*@*@*@*@  STUDENT FULL DETAILS PAGE  @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is student full details page sir..search using roll  number")
        else:
            speak("this is student full details page mam..search using roll number")
    ro=int(input("ENTER STUDENT ROLL NUMBER:-"))
    MySchool=sqlite3.connect(str(record[2])+'.db')
    sql="SELECT * from stu;"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    result=curschool.fetchall()
    for re in result:
        if int(re[0])==ro:
            clear()
            print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
            print("                                                                         *@*@*@*@*@*@*@*@*@*@*@  STUDENT FULL DETAILS PAGE  @*@*@*@*@*@*@*@*@*@*@*")
            print("\n")
            print("TEACHER ID   : "+str(record[0]))
            print("TEACHER NAME :"+str(record[1]))
            strDate=datetime.date.today()
            print("TODAY'S DATE :"+str(strDate))
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("SERVER TIME  :"+str(strTime))
            print("\n")
            school=sqlite3.connect(str(ro)+'.db')
            st="SELECT * from  detail ;"
            cur=school.cursor()
            cur.execute(st)
            stu=cur.fetchone()
            print("                                                                                             STUDENT'S BASIC INFORMATION\n")
            print("                                                                                           NAME OF THE STUDENT: "+str(stu[1]))
            print("                                                                                           ROLL NUMBER        : "+str(stu[0]))
            print("                                                                                           SEMESTAR           : "+str(stu[2]))
            print("                                                                                           MOBILE NUMBER      : "+str(stu[3]))
            print("                                                                                           ADDRESS            : "+str(stu[4]))
            print("\n                                                                                           STUDENTS'S ATTENDENCE DETAILS")
            print("\n")
            sc="SELECT * from att;"
            cur=school.cursor()
            cur.execute(sc)
            su=cur.fetchall()
            school.close()
            print("                                                                                                 DATE      : ATTENDENCE\n")
            for s in su:
                print("                                                                                                 "+str(s[0])+" "*(10-len(str(s[0])))+":   "+str(s[1]))
            t=2
            break
    
    if t==1:
        print("\n")
        print("\n                                 SORRY MAY BE THE STUDENT ROLL NUMBER IS NOT RECORDED OR YOU HAVE NO PERMISSION TO ACCESS THIS DETAILS!!")
        print("\a")
        time.sleep(3)
        mainp(record,2)
    elif t==2:
        p=int(input("\n                                                                                                   PRESS 1 TO SEE OTHER STUDENT DETAILS OR PRESS 2 TO GO BACK TO MAIN PAGE:-"))
        if p==1:
            display2(record,2)
        else:
            mainp(record,2)

def change(record,li):
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                             *@*@*@*@*@*@*@*@*@*@*@  PASSWORD CHANGING PAGE  @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is password changing page..dear sir!!..")
        else:
            speak("this is password changing .. mam!!..")
    pa=input("                                                                                                      ENTER OLD PASSWORD:-")
    if record[3]==pa:
        np=input("                                                                                                     ENTER NEW PASSWORD:-")
        co=input("                                                                                                     CONFIRM PASSWORD  :-")
        if np==co:
            MySchool=sqlite3.connect('user.db')
            sql="UPDATE teacher SET password='"+str(np)+"' WHERE Teacherid='"+str(record[0])+"';"
            curschool=MySchool.cursor()
            curschool.execute(sql)
            MySchool.cursor()
            MySchool.commit()
            se="SELECT * from teacher WHERE Teacherid='"+str(record[0])+"';"
            curschool=MySchool.cursor()
            curschool.execute(se)
            record=curschool.fetchone()
            MySchool.close()
            print("\n                                                                                                     $$$$$$$ PASSWORD UPDATED SUCCESSFULLY $$$$$$$")
            print("\n                                                                                                                YOUR PASSWORD IS : "+str(record[3]))
            print("                                                                                                                   PLEASE LOG OUT AND LOG IN IF YOU WANT TO CHECK!!")
            time.sleep(4)
            mainp(record,2)
        else:
            print("                                                                                                                                 OPPS!!!")
            print("\n                                                                                                       NEW PASSWORD AND CONFIRM PASSWORD IS NOT MATCHING!!!")
            print("\a")
            time.sleep(3)
            change(record,2)
    else:
        print("                                                                                                               PASSWORD IS NOT MATCHING!!!")
        print("\a")
        w=int(input("                                                                                                   PRESS 1 TO GO BACK TO MAIN PAGE OR 2 TO TRY AGAIN:-"))
        if w==2:
            change(record,2)
        else:
            mainp(record,2)


def delete(record,li):
    clear()
    print("                                                    ####################################-> NATIONAL INSTITUTE OF TECHNOLOGY AGARTALA <-#######################################\n")
    print("                                                                             *@*@*@*@*@*@*@*@*@*@*@  DELETION OF RECORD  PAGE  @*@*@*@*@*@*@*@*@*@*@*")
    print("\n")
    print("TEACHER ID   : "+str(record[0]))
    print("TEACHER NAME :"+str(record[1]))
    strDate=datetime.date.today()
    print("TODAY'S DATE :"+str(strDate))
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("SERVER TIME  :"+str(strTime))
    print("\n")
    if li==1:
        if str(record[4])=='male':
            speak("this is student record delete page..sir!!")
        else:
            speak("this is student record delete page..mam!!")
    MySchool=sqlite3.connect(str(record[2])+'.db')
    sql="SELECT * from stu;"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    result=curschool.fetchone()
    if result is None:
        print("\n        SORRY NO DETAILS FOUND TO DELETE! ")
        print("\a")
        ar= int(input("\n        PRESS 1 TO ENTER DETAILS OF STUDENT 2 FOR MAIN PAGE:-"))
        if ar==1:
            entry(record,1)
        else:
            mainp(record,2)
    else:
        sql="SELECT * from stu;"
        curschool=MySchool.cursor()
        curschool.execute(sql)
        result=curschool.fetchall()
        sq="SELECT * from date"
        curschool=MySchool.cursor()
        curschool.execute(sq)
        r=curschool.fetchall()
        for d in r:
            sl=d[0]
        print("                                                                                                 STUDENT DETAILS\n ")
        print("                                                                             ROLL NUMBER : NAME OF THE STUDENT : ATTENDENCE : PERCENTAGE")
        for re in result:
            pe=(int(re[2])/sl)*100
            print("                                                                                 "+str(re[0])+" "*(11-len(str(re[0])))+ ": "+str(re[1])+" "*(20-len(str(re[1])))+": "+str(re[2])+" "*(11-len(str(re[2])))+": "+str(pe))
        print("\n                                                                                   TOTAL CLASS TAKEN  "+str(sl)+"  UPTO DATE:  "+str(d[1]))
        print("\n")
        de=int(input("                                                                                            ARE YOU SURE ABOUT DELETING THE RECORD IF YES THEN PRESS 1 OR ELSE PRESS 2:-"))
        if de==1:
            for re in result:
                curschool=MySchool.cursor()
                se="DELETE from stu  WHERE roll='"+str(re[0])+"';"
                curschool.execute(se)
                MySchool.commit()
                a="C:\\Users\\user\\Desktop\\python\\"+str(re[0])+".db"
                os.remove(a)
            da=1
            for t in r:
                curschool=MySchool.cursor()
                sp="DELETE from date  WHERE sl='"+str(da)+"';"
                curschool.execute(sp)
                MySchool.commit()
                da+=1
            print("\n                                                                                                                      RECORD DELETED SUCCESSFULLY")
            time.sleep(3)
            mainp(record,2)
        else:
            mainp(record,2)

def forgot():
    clear()
    print("                                        ******************************************* FORGOT PASSWORD  PAGE***********************************************")
    x=int(input("       ENTER TEACHER ID:-"))
    MySchool=sqlite3.connect('user.db')
    sql="SELECT * from teacher WHERE Teacherid='"+str(x)+"';"
    curschool=MySchool.cursor()
    curschool.execute(sql)
    record=curschool.fetchone()
    MySchool.close()
    if record is None:
        print("\n                         TEACHER ID IS NOT AVAILABLE!!\n")
        print("\a")
        er =int(input("                   PRESS 1 TO GO TO SIGN UP PAGE 2 FOR NEXT ATTEMPT:-"))
        if er==1:
            login(2)
        elif er==2:
            forgot()
    bo=input("ENTER FAVOURITE BOOK NAME:-")
    if str(bo)==str(record[5]):
        fr=input("ENTER FAVOURITE FRUIT NAME:-")
        if str(fr)==str(record[6]):
            f=input("ENTER BEST FRIEND NAME:-")
            if str(f)==str(record[7]):
                print("\nSECUIRITY CHECKING COMPLETED SUCCESSFULLY!!!")
                print("\nYOUR USERNAME    :"+str(record[2]))
                print("YOUR PASSWORD    :"+str(record[3]))
                print("\n                                          PLEASE REMIND THE USERNAME AND PASSWORD CAREFULLY!!!!!!")
                ty=int(input("                                      PRESS 1 TO GO TO SIGN UP PAGE:-"))
                if ty==1:
                    login(2)
                else:
                    login(2)
            else:
                print("\nBEST FRIEND NAME IS NOT MATCHING PLEASE ENTER ALL THE INFORMATION AGEAIN FOR SECUIRITY!!\n")
                print("\a")
                ty=int(input("ENTER 1 TO GO BACK TO SIGNUP PAGE 2 TO RE ENTER INFORMATION:-"))
                if ty==2:
                    forgot()
                else:
                    login(2)
        else:
            print("\nFAVOURITE FRUIT NAME IS NOT MATCHING PLEASE ENTER ALL THE INFORMATION AGEAIN FOR SECUIRITY!!\n")
            print("\a")
            ty=int(input("ENTER 1 TO GO BACK TO SIGNUP PAGE 2 TO RE ENTER INFORMATION:-"))
            if ty==2:
                forgot()
            else:
                login(2)        
    else:
        print("\nFAVOURITE BOOK NAME IS NOT MATCHING PLEASE ENTER ALL THE INFORMATION AGEAIN FOR SECUIRITY!!\n")
        print("\a")
        ty=int(input("ENTER 1 TO GO BACK TO SIGNUP PAGE 2 TO RE ENTER INFORMATION:-"))
        if ty==2:
            forgot()
        else:
            login(2)


if __name__ == "__main__":
    login(1)