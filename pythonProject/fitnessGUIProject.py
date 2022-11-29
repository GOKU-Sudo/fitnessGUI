import tkinter as tk
import mysql.connector as conn
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  PIL import Image,ImageTk

global ws,root2

#calculator Main


def run():
      
      new.destroy()          
      clearLogin()  
        
      def bpMeasure():
            global bp1,bp2
            bp1=round(float(BPlow_tf.get()),2)
            bp2=round(float(BPhigh_tf.get()),2)
       
            if 60<=bp1<=90 and 60<= bp2 <=90:
                  b1="BP is Low"
                  return b1
            if 90<=bp1<=120 and 90<= bp2 <=120:
                  b1="BP is Normal"
                  return b1
            if 120<=bp1<=150 and 120<= bp2 <=150:
                  b1="BP is High"
                  return b1
            else:
                  b1="Invalid Input"
                  return b1
            
      
      def pulseMeasure():
            global pulse
            pulse=round(float(pulseRate_tf.get()),2)
            if(60<=pulse<=100):
                  pulseReport="%s is Normal"%str(pulse)
                  return pulseReport
            elif(pulse<60):
                  pulseReport="%s is Low"%str(pulse)
                  return pulseReport
            else:
                  pulseReport="%s is High"%str(pulse)
                  return pulseReport
            
      
      def RBCcount(var1):
            global rbc
            if var1==0:
                  rbc=round(float(rbcCount_tf.get()),2)
                  if(4.2<=rbc<=5.4):
                        rbcReport="%s is Normal"%str(rbc)
                        return rbcReport
                  elif(rbc<4.2) :
                        rbcReport="%s is Low"%str(rbc)
                        return rbcReport
                  else:
                        rbcReport="%s is High"%str(rbc)
                        return rbcReport
            elif var1==1:
                  rbc=round(float(rbcCount_tf.get()),2)
                  if(3.6<=rbc<=5):
                        rbcReport="%s is Normal"%str(rbc)
                        return rbcReport
                  elif(rbc<3.6):
                        rbcReport="%s is Low"%str(rbc)
                        return rbcReport
                  else:
                        rbcReport="%s is High"%str(rbc)  
                        return rbcReport      
                        
      def WBCcount():
            global wbc
            wbc=round(float(wbcCount_tf.get()),2)
            if(4.5<=wbc<=11):
                        wbcReport="%s is Normal"%str(wbc)
                        return wbcReport
            elif(wbc<4.5):
                        wbcReport="%s is Low"%str(wbc)
                        return wbcReport
            else:
                        wbcReport="%s is High"%str(wbc)  
                        return wbcReport      
                              
                        
      def platelets():
            global plate
            plate=round(float(platelets_tf.get()),2)
            if(150<=plate<=400):
                  plateletsRecord="%s is Normal"%str(plate)
                  return plateletsRecord
            elif plate<150:
                  plateletsRecord="%s is Low"%str(plate)
                  return plateletsRecord
            else:
                  plateletsRecord="%s is High"%str(plate)
                  return plateletsRecord

      def HB(var1):
            global hb
            if var1==0:
                  hb=round(float(HB_tf.get()),2)
                  if(13.2<=hb<=16.6):
                        hbReport="%s is Normal"%str(hb)
                        return hbReport
                  elif hb<13.2:
                        hbReport="%s is Low"%str(hb)
                        return hbReport
                  else:
                        hbReport="%s is High"%str(hb)
                        return hbReport
            if var1==1:
                  hb=round(float(HB_tf.get()),2)
                  if(11.6<=hb<=15):
                        hbReport="%s is Normal"%str(hb)
                        return hbReport
                  elif hb<13.2:
                        hbReport="%s is Low"%str(hb)
                        return hbReport
                  else:
                        hbReport="%s is High"%str(hb)
                        return hbReport
            

      def uricAcid(var1):
            global uric
      
            if var1==0:
                  
                  uric=round(float(uricAcid_tf.get()),2)
                  if( 3.4<=uric<=7):
                        uricReport="%s is Normal"%str(uric)
                        return uricReport
                  elif uric<3.4:
                        uricReport="%s is Low"%str(uric)
                        return uricReport
                  else:
                        uricReport="%s is High"%str(uric)
                        return uricReport
            if var1==1:
                  
                  uric=round(float(uricAcid_tf.get()),2)
                  if( 2.4<=uric<=6):
                        uricReport="%s is Normal"%str(uric)
                        return uricReport
                  elif uric<2.4:
                        uricReport="%s is Low"%str(uric)
                        return uricReport
                  else:
                        uricReport="%s is High"%str(uric)
                        return uricReport
                  

      def cholestrol():
            global choles
            choles=round(float(cholestrol_tf.get()),2)
            if(5==choles):
                  cholesReport="%s is Normal" %str(choles)
                  return cholesReport
            elif(choles<5):
                  cholesReport="%s is Low(At Risk)" %str(choles)
                  return cholesReport
            else:
                  cholesReport="%s is High(At Risk)" %str(choles)
                  return cholesReport                   
                        

      def reset_entry():
            id_tf.delete(0,'end')
            name_tf.delete(0,'end')
            var.set(None)
            age_tf.delete(0,'end')
            height_tf.delete(0,'end')
            weight_tf.delete(0,'end')
            BPlow_tf.delete(0,'end')
            BPhigh_tf.delete(0,'end')
            pulseRate_tf.delete(0,'end')
            rbcCount_tf.delete(0,'end')
            wbcCount_tf.delete(0,'end')
            HB_tf.delete(0,'end')
            platelets_tf.delete(0,'end')
            uricAcid_tf.delete(0,'end')
            cholestrol_tf.delete(0,'end')
            


      def calculate_bmi():
            kg = float(weight_tf.get())
            m = float(height_tf.get())/100
            bmi = kg/(m*m)
            bmi = round(bmi, 1)
            if  bmi < 18.5:
                  BMI="%d is Underweight" %bmi;
                  return bmi
            elif  bmi > 18.5 and bmi<24.9:
                  return "%d is Normal" %bmi;
            elif bmi > 24.9 and bmi < 29.9:
                  return "%d is Overweight" %bmi;
            elif bmi >29.9:
                  return "%d is Obesity" %bmi;
            else:
                  return "Something Went Wrong"

     

      
      def calculate(event=None):
            var1= var.get()
            bmi=calculate_bmi()
            bp=bpMeasure()
            pulse1=pulseMeasure()
            rbc1=RBCcount(var1); wbc1=WBCcount(); plate1=platelets()
            hb1=HB(var1); uric1=uricAcid(var1); choles1=cholestrol()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS BMI")  
            cursor.execute("use bmi")                                                                    
            commands="show tables"
            cursor.execute(commands)
            li=[]
            for i in cursor:
                  i=str(*i)
                  li.append(i)
                       
            if "bmi" not in li:
                  cursor.execute("Create table bmi(id int(6) primary key, name varchar(25), Sex char(1))")        
                  
            if "bmidata" not in li:  
                  cursor.execute("""Create table bmidata(id int(6),name varchar(25), Sex char(1),bplow float(5,2), bphigh float(5,2), pulse float(5,2), RBC float(4,2), WBC float(5,2),platelets float(5,2),hb float(5,2), uric float(5,2), 
                  cholestrol float(4,2),timestamp timestamp(6))""")
                  
            id1=int(id_tf.get())
            name=name_tf.get()     
            bp1=round(float(BPlow_tf.get()),2)
            bp2=round(float(BPhigh_tf.get()),2)
            pulse=round(float(pulseRate_tf.get()),2)
            
            
            if var1==0:
                  rbc=round(float(rbcCount_tf.get()),2)
                  hb=round(float(HB_tf.get()),2)
                  uric=round(float(uricAcid_tf.get()),2)
                  gender='M'
            else:
                 rbc=round(float(rbcCount_tf.get()),2)
                 hb=round(float(HB_tf.get()),2)
                 uric=round(float(uricAcid_tf.get()),2)
                 gender='F'
                 
            wbc=round(float(wbcCount_tf.get()),2)
            plate=round(float(platelets_tf.get()),2)
            choles=round(float(cholestrol_tf.get()),2)
         
            comm1="select id from bmi"
            cursor.execute(comm1)
            li= tuple(map(lambda x: x[0], cursor.fetchall()))
            
            try:
                  name=name.lower()
                  if id1 in li:
                        sqlCommand2=f"insert into bmidata values({id1},'{name}','{gender}',{bp1},{bp2},{pulse},{rbc},{wbc},{plate},{hb},{uric},{choles},now())"
                        cursor.execute(sqlCommand2)
                        db.commit()
                        messagebox.showinfo('Fitness BMI CALCULATORs', f'BMI = {bmi}\n\n' f'BP = {bp}\n\n' f'Pulse Rate = {pulse1}\n\n'
                                    f'RBC Count = {rbc1}\n\n' f'WBC Count = {wbc1}\n\n' f"Platelets = {plate1}\n\n"
                                    f"haemoglobin = {hb1}\n\n" f"Uric Acid = {uric1}\n\n" f"Cholestrol = {choles1}") 
                        ws.destroy()
                  else:
                        sqlCommand1=f"insert into bmi values({id1},'{name}','{gender}')"
                        cursor.execute(sqlCommand1)
                        sqlCommand2=f"insert into bmidata values({id1},'{name}','{gender}',{bp1},{bp2},{pulse},{rbc},{wbc},{plate},{hb},{uric},{choles},now())"
                        cursor.execute(sqlCommand2)
                        db.commit()
                       
                        
                        messagebox.showinfo('FItness BMI CALCULATORs', f'BMI = {bmi}\n\n' f'BP = {bp}\n\n' f'Pulse Rate = {pulse1}\n\n'
                                    f'RBC Count = {rbc1}\n\n' f'WBC Count = {wbc1}\n\n' f"Platelets = {plate1}\n\n"
                                    f"haemoglobin = {hb1}\n\n" f"Uric Acid = {uric1}\n\n" f"Cholestrol = {choles1}")
                        ws.destroy()
      
                       
            except Exception as e:
                  print(e)
                  
                  messagebox.showerror("Fitness BMI CALCULATOR","Error while inserting Data")
                  db.rollback()
       
                  
      global ws, var         
     
      ws=Toplevel(root)
      ws.title('Fitness BMI CALCULATOR')
      ws.geometry('650x600+500+100')
      ws.config(bg='#856ff8')
      ws.resizable(width=False, height=False)
      # ws.mainloop()
     
      #icon
      icon_image=ImageTk.PhotoImage(file="pics\icon.png")
      ws.iconphoto(False,icon_image)
      


      var = IntVar()
      var.set(0)

      frame = Frame(
      ws,
      padx=35, 
      pady=40,
      )
      frame.pack(expand=True)

      id_lb=Label(frame,
                  text="Enter ID")

      id_lb.grid(row=1,column=1)

      id_tf=Entry(frame)

      id_tf.grid(row=1, column=2,padx=10, pady=5)

      name_lb=Label(
      frame,
      text="Name"
      )

      name_lb.grid(row=1, column=3)

      name_tf = Entry(
      frame, 
      )

      name_tf.grid(row=1, column=4,padx=10, pady=5)


      gen_lb = Label(
      frame,
      text='Select Gender'
      )
      gen_lb.grid(row=2, column=1)

      frame2 = Frame(
      frame
      )
      frame2.grid(row=2, column=2, pady=5)


      female_rb = Radiobutton(
      frame2,
      text = 'Female',
      variable = var,
      value = 1
      )
      female_rb.pack(side=RIGHT)

      male_rb = Radiobutton(
      frame2,
      text = 'Male',
      variable = var,
      value = 0
      )
      male_rb.pack(side=LEFT)

      age_lb = Label(
      frame,
      text="Enter Age (6 - 120)"
      )

      age_lb.grid(row=3, column=1)

      age_tf = Entry(
      frame, 
      )
      age_tf.grid(row=3, column=2, pady=10)




      height_lb = Label(
      frame,
      text="Enter Height (cm)  "
      )
      height_lb.grid(row=3, column=3)

      height_tf = Entry(
      frame,
      )
      height_tf.grid(row=3, column=4, pady=10)

      weight_lb = Label(
      frame,
      text="Enter Weight (kg)  ",

      )
      weight_lb.grid(row=4, column=1)



      weight_tf = Entry(
      frame,
      )
      weight_tf.grid(row=4, column=2, pady=10)

      #BP LOW
      BPlow_lb=Label(
      frame,
      text='BP LOW',
      )

      BPlow_lb.grid(row=4,column=3)

      BPlow_tf=Entry(
      frame,
      )

      BPlow_tf.grid(row=4,column=4,pady=10)

      #BP HIGH

      BPhigh_lb=Label(
      frame,
      text='BP HIGH',
      )

      BPhigh_lb.grid(row=5,column=1)

      BPhigh_tf=Entry(
      frame,
      )

      BPhigh_tf.grid(row=5,column=2,pady=10)

      #pulse rate

      pulseRate_lb=Label(
      frame,
      text='Pulse Rate',
      )

      pulseRate_lb.grid(row=5,column=3)

      pulseRate_tf=Entry(
      frame,
      )

      pulseRate_tf.grid(row=5,column=4,pady=10)

      #RBC count

      rbcCount_lb=Label(
      frame,
      text='RBC Count',
      )

      rbcCount_lb.grid(row=6,column=1)

      rbcCount_tf=Entry(
      frame,
      )

      rbcCount_tf.grid(row=6,column=2,pady=10)

      #WBC count

      wbcCount_lb=Label(
      frame,
      text='WBC Count',
      )

      wbcCount_lb.grid(row=6,column=3)

      wbcCount_tf=Entry(
      frame,
      )

      wbcCount_tf.grid(row=6,column=4,pady=10)

      #platelets

      platelets_lb=Label(
      frame,
      text='Platelets',
      )

      platelets_lb.grid(row=7,column=1)

      platelets_tf=Entry(
      frame,
      )

      platelets_tf.grid(row=7,column=2,pady=10)


      #HB

      HB_lb=Label(
      frame,
      text='haemoglobin',
      )

      HB_lb.grid(row=7,column=3)

      HB_tf=Entry(
      frame,
      )

      HB_tf.grid(row=7,column=4,pady=10)


      #Uric acid

      uricAcid_lb=Label(
      frame,
      text='Uric Acid',
      )

      uricAcid_lb.grid(row=8,column=1)

      uricAcid_tf=Entry(
      frame,
      )

      uricAcid_tf.grid(row=8,column=2,pady=10)


      #cholestrol

      cholestrol_lb=Label(
      frame,
      text='Cholestrol',
      )

      cholestrol_lb.grid(row=8,column=3)

      cholestrol_tf=Entry(
      frame,
      )

      cholestrol_tf.grid(row=8,column=4,pady=10)

      frame3 = Frame(
      frame,
     
      )
      frame3.grid(row=9, columnspan=6, pady=10)

      cal_btn = Button(
      frame3,
      text='Calculate',
      # command=calculate_bmi,
      command=calculate,
      )
      cal_btn.grid(row=9,column=1,padx=10)
      cholestrol_tf.bind('<Return>', calculate)

      

      reset_btn = Button(
      frame3,
      text='Reset',
      command=reset_entry
      )
      reset_btn.grid(row=9,column=2,padx=10)
  

      exit_btn = Button(
      frame3,
      text='Exit',
      command=lambda:ws.destroy()
      )
      exit_btn.grid(row=9,column=3,padx=10)
      # exit_btn.pack(side=RIGHT)
      # ws.mainloop()

   

#record page


def RunRecordPage():
      
      new.destroy()
      clearLogin()
      
      def dataRetrive(event=None):
            global new2
            try:
                  new2.destroy() 
                             
            except:
                  try:
                        new2.destroy()
                  except:
                        pass
            
           
            userid=id2.get()
            usernameid=name2.get()
            usernameid=usernameid.lower()
            if(userid and usernameid):
                        
                        try:
                              userid=int(userid)
                              global cursor
                              cursor.execute("use bmi")
                        
                              comm1="select id,name from bmidata"
                              cursor.execute(comm1)
                        
                          
                              tupRec=cursor.fetchall()
                              
                              j=(userid,usernameid)
                              
                        
                              if j in tupRec:
                                          
                                          
                                          new2 = Toplevel(root2)
                                          icon_image=PhotoImage(file="pics\icon.png")
                                          new2.iconphoto(False,icon_image)
                                          cursor=db.cursor()
                                          # Creating tkinter new
                                          
                                          new2.geometry("1200x280") 
                                          new2.title("Fitness BMI CALCULATOR")  
                                          new2.resizable(width=False,height=False)
                                          # Using treeview widget
                                          trv = ttk.Treeview(new2, selectmode ='browse')
                                          trv.grid(row=1,column=1,padx=37,pady=20)

                                          # number of columns
                                          trv["columns"] = ("1", "2", "3","4","5","6","7","8","9","10","11","12","13")

                                          # Defining heading
                                          trv['show'] = 'headings'

                                          # width of columns and alignment 
                                          trv.column("1", width = 120, anchor ='c')
                                          trv.column("2", width = 80, anchor ='c')
                                          trv.column("3", width = 80, anchor ='c')
                                          trv.column("4", width = 80, anchor ='c')
                                          trv.column("5", width = 80, anchor ='c')
                                          trv.column("6", width = 80, anchor ='c')
                                          trv.column("7", width = 80, anchor ='c')
                                          trv.column("8", width = 80, anchor ='c')
                                          trv.column("9", width = 80, anchor ='c')
                                          trv.column("10", width = 80, anchor ='c')
                                          trv.column("11", width = 80, anchor ='c')
                                          trv.column("12", width = 80, anchor ='c')
                                          trv.column("13", width = 120, anchor ='c')
                                          # Headings  
                                          # respective columns
                                          trv.heading("1", text ="ID")
                                          trv.heading("2", text ="Name")
                                          trv.heading("3", text ="Sex")
                                          trv.heading("4", text ="BPlow")
                                          trv.heading("5", text ="BPhigh")  
                                          trv.heading("6", text ="Pulse")
                                          trv.heading("7", text ="RBC")
                                          trv.heading("8", text ="WBC")
                                          trv.heading("9", text ="Platelets")
                                          trv.heading("10", text ="Hemoglobin")
                                          trv.heading("11", text ="Uric Acid")
                                          trv.heading("12", text ="Cholestrol")
                                          trv.heading("13", text ="Timestamp")

                                          # getting data from MySQL student table
                                          # cursor.execute("use bmi")
                                          
                                          cursor.execute(f'''select id,name,Sex ,bplow , bphigh , pulse , RBC , WBC ,platelets ,hb , uric ,cholestrol ,timestamp from bmidata 
                                                      where id={userid} and name='{usernameid}'  LIMIT 0,10 ''')
                                          # print(cursor)
                                          recordTuple=()
                                          # print(cursor)
                                          for dt in cursor:
                                                recordTuple=recordTuple+(dt,)
                                    
                              
                                          for i in range(len(recordTuple)):
                                                
                                                trv.insert("", 'end',iid=recordTuple[i], text=recordTuple[i],
                                                      values =(recordTuple[i][0],recordTuple[i][1],recordTuple[i][2],recordTuple[i][3],recordTuple[i][4],recordTuple[i][5],recordTuple[i][6],recordTuple[i][7],recordTuple[i][8],recordTuple[i][9],recordTuple[i][10],recordTuple[i][11],recordTuple[i][12]))
                                                
                                          new2.mainloop()  
                              else:
                                    messagebox.showerror("Fitness BMI CALCULATOR","ID and Name does not match")            
                                                                
                        except :
                              # print(e)
                              messagebox.showerror("Fitness BMI CALCULATOR","Error while Fetching Data")
                              
                                               
            else:
                  messagebox.showwarning("Fitness BMI CALCULATOR","Please Enter Credentials") 
                  
                                          
      def clearRecord():
            id2.delete(0,'end')
            name2.delete(0,'end')
            new2.destroy() 

      
      
      global root2

      root2=Toplevel(root)
      root2.geometry("300x200+500+200")
      root2.resizable(width=False, height=False)
      root2.title("Fitness BMI CALCULATOR")
      icon_image=PhotoImage(file="pics\icon.png")
      root2.iconphoto(False,icon_image)

      lblfrstrow = tk.Label(root2, text ="Enter ID -",font=('Helvetica 11 ') )
      lblfrstrow.place(x = 50, y = 20)
      
      global id2
      
      id2= tk.Entry(root2, width = 35,font=('Helvetica 11 '))
      id2.place(x = 150, y = 20, width = 100)

      lblsecrow = tk.Label(root2, text ="Enter Name -",font=('Helvetica 11 '))
      lblsecrow.place(x = 50, y = 50)
      
      global name2
      
      name2= tk.Entry(root2, width = 35,font=('Helvetica 11 '))
      name2.place(x = 150, y = 50, width = 100)

      submi = tk.Button(root2, text ="Submit",
                                    bg ='pink', font=('Helvetica 11 '),command=dataRetrive)
      submi.place(x = 60, y = 135, width = 55)
      name2.bind('<Return>', dataRetrive)
      
      clear=tk.Button(root2,text="clear",bg="pink",font=('Helvetica 11 '),command = clearRecord)
      clear.place(x = 180, y = 135, width = 55)


      root2.mainloop()
      
            
     
      
def open_win():
   global new
   clearLogin()
   new = Toplevel(root)
   new.geometry("300x200+500+200")

   new.resizable(width=False, height=False)
   new.title("Fitness BMI CALCULATOR")
   icon_image=PhotoImage(file="pics\icon.png")
   new.iconphoto(False,icon_image)
   #Create a Label in New window
   
   Label(new, text="WELCOME to Fitness", font=('Helvetica 17 bold')).pack(pady=30)
   
   calButton = tk.Button(new, text ="BMI",
					bg ='pink',font=('Helvetica 11 ') ,command = run)
   calButton.place(x = 50, y = 120, width = 55)
   calButton2 = tk.Button(new, text ="Record",
					bg ='pink',font=('Helvetica 11 '),command=RunRecordPage )
   calButton2.place(x = 170, y = 120, width = 55)                                          

 

# login page
 
def clearLogin():
     Username.delete(0,'end')
     password.delete(0,'end')
  

def submitact(event=None):
      root.state(newstate='iconic')
      user = Username.get()
      passw = password.get()
      logintodb(user, passw)
    

def logintodb(user, passw):
      if (user and passw):
            try:
                  global db
                  db = conn.connect(host ="localhost",
										user = user,
										password = passw,
										    )
              
                  
                  if db.is_connected():
                        try:  
                              # root.destroy()
                              if(new.winfo_ismapped()):
                                    new.destroy()
                              
                              # ws.destroy() 
                             
                        except:
                              try:        
                                    if(ws.winfo_ismapped()):
                                          ws.destroy()
                              except:
                                    try:  
                                          if(root2.winfo_ismapped()):
                                                root2.destroy()
                                         
                                    except:
                                          pass
                                          
                        finally:
                              global cursor
                              cursor = db.cursor()
                              messagebox.showinfo("Fitness BMI CALCULATOR","Successfully Connected to Database")
                              open_win()           
		
            except Exception as e:
                  print(e)
                  messagebox.showerror("Finess BMI CALCULATOR","Error while connecting to Database")         
        
 
      else:
            messagebox.showwarning("WARNING","Please Enter Credentials")
       


root = tk.Tk()
root.geometry("305x250+500+200")
root.resizable(width=False, height=False)
root.title("Fitness BMI CALCULATOR")



# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", font=('Helvetica 11 '))
lblfrstrow.place(x = 50, y = 20)

# global Username

Username = tk.Entry(root, width = 35,font=('Helvetica 11 '))
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -",font=('Helvetica 11 '),pady=10)
lblsecrow.place(x = 50, y = 50)

# global password

password = tk.Entry(root, width = 35,font=('Helvetica 11 '),show=' ')
password.place(x = 150, y = 60, width = 100)

submitbtn = tk.Button(root, text ="Login",
					bg ='pink',font=('Helvetica 11 '), command = submitact)
submitbtn.place(x = 60, y = 135, width = 55)
password.bind('<Return>', submitact )

clearbtn=tk.Button(root,text="clear",bg="pink",font=('Helvetica 11 '),command = clearLogin)
clearbtn.place(x = 180, y = 135, width = 55)

icon_image=PhotoImage(file="pics\icon.png")
root.iconphoto(False,icon_image)

root.mainloop()