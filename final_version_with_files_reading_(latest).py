from tkinter import *
import tkinter as tk
import mysql.connector
import hashlib
import os
import re
import mysql.connector
from tkinter.filedialog import askdirectory, askopenfile
from tkinter import filedialog, messagebox
from tkinter import Tk, Button, PhotoImage, Label
from PIL import ImageTk, Image
import webbrowser
import tempfile, shutil
import time

from mysql.connector import connection
####### Database where you can store images in binary ######




def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1672005aA.",
        database = "Users_database",
    )

    my_cursor = mydb.cursor(buffered=True) ####buffered=True
    
    path  = "D:/billa/Bureau/new_version_with_name/images/"

    window = Tk()
    #window.iconbitmap(path + "logo.ico")
    window.geometry("295x640")
    window.configure(bg = "#ffffff")
    window.title("App")

    def on_closing():
        if messagebox.askquestion("Quit", "Do you want to quit?"):   #if messagebox.askquestion("Quit", "Do you want to quit?"):  #if messagebox.askokcancel("Quit", "Do you want to quit?"):
            for temp_files in list_of_temp_files:
                os.remove(temp_files)
        window.destroy()
    
    home_screen = tk.Frame(window,bg="#ffffff")
    home_screen.place(x=0,y=0,width=1920,height=640)

    signup_screen = tk.Frame(window,bg="#ffffff")
    signup_screen.place(x=0,y=0,width=1920,height=640)

    login_screen = tk.Frame(window,bg="#ffffff")
    login_screen.place(x=0,y=0,width=1920,height=640)

    manage_screen = tk.Frame(window,bg="#ffffff")
    manage_screen.place(x=0,y=0,width=1920,height=640)

    signup_name_screen = tk.Frame(window,bg="#ffffff")
    signup_name_screen.place(x=0,y=0,width=1920,height=640)

    files_screen = tk.Frame(window,bg="#ffffff")
    files_screen.pack(fill='both', expand=True, side='left')  ###### ou p


    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    #d#ef show_frame(frame_to_raise):
        #frame_to_raise.tkraise()

    def show_frame_signup_name():
        signup_name_screen.tkraise()

    def show_frame_signup():
        signup_screen.tkraise()

    def show_frame_login():
        login_screen.tkraise()

    def show_frame_home():
        home_screen.tkraise()

    def show_frame_manage():
        manage_screen.tkraise()

    def show_frame_files_screen():
        files_screen.tkraise()
    list_of_temp_files = []
    class Button_:
        def __init__(self, filename, a, b, a_,b_, canvas_files):
            self.filename = filename
            #print(self.filename)
            self.file_____name, file_extension = os.path.splitext(filename)
            match file_extension: ###### ajouter pleins d'autres cas sinon il y aura des erreurs d'atributs
                case ".png":
                    self.logo = "image.png"
                case ".jpg":
                    self.logo = "image.png"
                case ".jpeg":
                    self.logo = "image.png"
                case ".mp4":
                    self.logo = "video.png"
                case ".docx":
                    self.logo = "word.png"
                case ".txt":
                    self.logo = "notepad.png"
                case ".gif":
                    self.logo = "image.png"
                case another:
                    self.logo = "image.png"
            self.filename_len = len(filename)
            if self.filename_len > 11:
                self.font_size_filename=4
            else:
                self.font_size_filename=6
            self.image = Image.open(path + self.logo)
            self.pic = ImageTk.PhotoImage(self.image)
            #self.button = tk.Button(canvas ,image= self.pic, borderwidth = 0, highlightthickness = 0, relief = "flat", command= lambda file=file, file_extension= file_extension: self.open_vid(file, file_extension))#lambda:self.open_vid(file, self.file_extension))
            self.button = tk.Button(canvas_files ,image= self.pic, borderwidth = 0, highlightthickness = 0, relief = "flat", command= lambda filename=filename, file_extension= file_extension: self.open_vid(filename, file_extension))#lambda:self.open_vid(file, self.file_extension))
            canvas_files.create_window(b, a, anchor='nw', window=self.button,width = 50 , height=50)  ####### Pour centrer il faudrait eventuellement modifier anchor = 'nw
            self.button.image = self.pic
            self.instructions = tk.Label(canvas_files, text=filename, font=("SF Pro Rounded", self.font_size_filename), fg="#292d3e", bg="#ffffff", border=0)
            self.window_button = canvas_files.create_window(b_, a_, anchor='nw', window=self.instructions, width = 50 , height=10)  ####### Pour centrer il faudrait eventuellement modifier anchor = 'nw'
            #dct_window = {self.window_button:self.filename}
            #self.window_button = str(self.window_button)
            #list_of_windows.append(self.window_button)
            #list_of_windows.append(int(self.window_button))
            #print(str(self.window_button))
            self.menu_ = Menu(canvas_files, tearoff = 0)
            
            self.menu_.add_command(label = "Télécharger", command = lambda: self.writevideo(self.filename))
            self.menu_.add_command(label = "Supprimer", command = lambda: self.delete_file(self.filename))
            def do_popup(event):
                try:
                    self.menu_.tk_popup(event.x_root, event.y_root)
                finally:
                    self.menu_.grab_release()
                
            self.button.bind("<Button-3>", do_popup)
    #files = 20*["Denmark.png"]+20*["Greece.mp4"]
    #all_file_names = "he"

    

    
        def write_file(self, data, filename):
            self.filename___ = filename
            with open(self.filename___, 'wb') as file_:
                file_.write(data)

        def readBLOB(self, image_id, photo_path):
            #print("Reading BLOB data from table")
            self.image_id__ = image_id
            self.photo_path = photo_path
            #print(f"L'id de l'image est.......{self.image_id}")
            #global file_extension
            self.sql_fetch_blob_query = (f"SELECT * from {user_id} where image_id = '{self.image_id__}'")
            #print(self.sql_fetch_blob_query)
            my_cursor.execute(self.sql_fetch_blob_query)
            self.record = my_cursor.fetchall()
            for row in self.record:
                #print("Id = ", self.row[0], )
                self.image = row[1]
                self.file_extension = row[2]
            self.write_file(self.image, self.photo_path)


        def readvideo(self, filename, file_extension):
            #my_cursor.execute("SELECT file_extension from user_1 where image_id = %s" % (image_id)) ###### LE "WHERE IMAGE ID EST IMPORTANT ET PEUT CAUSER DES ERREURS/BUGS"
            #file_extension = my_cursor.fetchone()
            #file_extension = file_extension[0]
            #print(file_extension)
            #global temp
            #global filename
            #print(self.file)
            self.filename = filename
            #print(self.filename)
            my_cursor.execute(f"SELECT image_id from {user_id} where filename = '{self.filename}'")
            self.image_id_ = my_cursor.fetchone()
            self.image_id_ = self.image_id_[0]
            print(self.image_id_)
            #print(f"L'id de l'image est.......{image_id}")
            self.temp = tempfile.NamedTemporaryFile(suffix=self.file_extension, delete=False) # , delete=False
            #temp.close()
            self.filename = self.temp.name
            list_of_temp_files.append(self.filename)
            #print(self.filename)
            self.readBLOB(self.image_id_, self.filename)
            webbrowser.open(self.filename)
        

        def writevideo(self, filename):
            #self.filename = filename
            #my_cursor.execute(f"SELECT image_id from {user_id} where filename = '{self.filename}'")
            #self.image_id = my_cursor.fetchall()
            #self.image_id = self.image_id[0]
            #print(type(image_id))
            #image_id = image_id[0]
            #my_cursor.execute("SELECT file_extension from user_1 where image_id = %s" % (self.image_id)) ###### LE "WHERE IMAGE ID EST IMPORTANT ET PEUT CAUSER DES ERREURS/BUGS"
            #self.file_extension_ = my_cursor.fetchone()
            #self.file_extension_ = self.file_extension_[0]
            #print(self.file_extension_)
            #type_ = self.file_extension_.replace('.', '')
            #type_ = type_.upper()
            self.filename = filename
            my_cursor.execute(f"SELECT image_id from {user_id} where filename = '{self.filename}'")
            self.image_id___ = my_cursor.fetchone()[0]
            #self.image_id___ = [row[0] for row in my_cursor.fetchall()]
            #self.image_id___ = self.image_id___[0]
            #print(self.image_id___)
            #self.image_id = self.image_id[0] ###### Erreur, on ne peut pas utiliser fetchone car il peut y avoir plusieurs fichiers avec le même nom donc il faut pense a rajouter un (1), (2), (3), etc... au moment d'importer le fichier dans la base de données
            #for self.image_id in my_cursor.fetchall():
                #self.image_id = self.image_id[0]
            #print(self.filename)
            #print(self.image_id)
            #global filename
            my_cursor.execute(f"SELECT file_extension from {user_id} where image_id = '{self.image_id___}'") ###### LE "WHERE IMAGE ID EST IMPORTANT ET PEUT CAUSER DES ERREURS/BUGS"
            #self.file_extension_ = my_cursor.fetchone()
            #self.file_extension_ = self.file_extension_[0]
            filename_we_wont_use, self.file_extension_ = os.path.splitext(self.filename)
            #print(self.file_extension_)
            self.type_ = self.file_extension_.replace('.', '')
            self.type_ = self.type_.upper()
            
            #self.file_extension_ = self.file_extension_[0]
            self.path_save = filedialog.asksaveasfilename(initialdir = "D:/billa/Bureau", defaultextension= self.file_extension_, filetypes=[(self.type_,self.file_extension_),("Tout fichier",""),])
            #print(path_save)
            self.readBLOB(self.image_id___, self.path_save)
            #print(self.file_extension_)
            #type_ = self.file_extension_.replace('.', '')
            #type_ = type_.upper()
            #path_save = filedialog.asksaveasfilename(initialdir = "D:/billa/Bureau", defaultextension= self.file_extension_, filetypes=[(type_,self.file_extension_),("Tout fichier",""),])
            #print(path_save)
            #self.readBLOB(image_id, path_save)


        def open_vid(self, filename , file_extension):
            self.file_extension = file_extension
            self.filename = filename
            #print(file_extension)
            self.readvideo(self.filename, self.file_extension)
        
        def delete_file(self, filename):
            self.filename_to_delete = filename
            if messagebox.askokcancel("Supprimer", f"Voulez-vous vraiment supprimer {self.filename_to_delete} ?"):
                my_cursor.execute(f"DELETE FROM {user_id} WHERE filename = '{self.filename_to_delete}'")
                mydb.commit()
                refresh_files()
        


    def check_names():
        def check_surname():
            if len(entry1_signup_name.get()) ==  0:
                canvas_signup_name.itemconfig(error_text_signup_name, text="Veuillez entrer un nom", font=("Tahoma", 9))
                signup_name_screen.after(5000, lambda :canvas_signup_name.itemconfig(error_text_signup_name, text=""))
                
            else:
                canvas_signup_name.itemconfig(error_text_signup_name, text="")
                global surname_signup
                surname_signup = entry1_signup_name.get()
                show_frame_signup()
                
        if len(entry0_signup_name.get()) == 0:     
            canvas_signup_name.itemconfig(error_text_signup_name, text="Veuillez entrer un prénom", font=("Tahoma", 9))
            signup_name_screen.after(5000, lambda :canvas_signup_name.itemconfig(error_text_signup, text=""))   

        else:
            global name_signup
            name_signup = entry0_signup_name.get()
            canvas_signup_name.itemconfig(error_text_signup_name, text="")            
            check_surname()

    def manage_text(name, number_of_files):
        welcome_message = canvas_manage.create_text(210,90, fill="#15C2D6")
        canvas_manage.itemconfig(welcome_message, text = name, font=("SF Pro Text", 20))
        if number_of_files == 0:
            files_message = f"Vous n'avez aucun fichier"
        elif number_of_files == 1:
            files_message = f"Vous avez {number_of_files} fichier"
        elif number_of_files > 1:
            files_message = f"Vous avez {number_of_files} fichiers"    
        canvas_manage.itemconfig(message_number_of_files, text = files_message, font=("SF Pro Text", 15))

    
    def manage_from_signup(user_id):  
        #global all_file_names
        my_cursor.execute("SELECT * from %s" % (user_id))
        number_of_files = my_cursor.fetchone()
        try:
            number_of_files = number_of_files[0]
        except TypeError:
            number_of_files = 0
        #print(number_of_files)
        if number_of_files > 0:
            all_file_names = my_cursor.execute("SELECT filename from %s" % (user_id))
            for filelol in all_file_names:
                print(filelol)
        my_cursor.execute("SELECT name FROM users_info WHERE email = '%s'" % (email_signup))
        name_from_db = my_cursor.fetchone()
        name_from_db = (name_from_db[0])
        name_from_db = str(name_from_db)
        manage_text(name_from_db, number_of_files)
        show_frame_manage()   
        show_frame_manage()



    def effective_signup():
        global email_signup
        email_signup = entry0_signup.get()
        if re.fullmatch(regex, email_signup):
            my_cursor.execute("SELECT email FROM users_info WHERE email = '%s'" % (email_signup))
            if my_cursor.fetchone():
                canvas_signup.itemconfig(error_text_signup, text=("Un compte existe déjà sous l'adresse " + email_signup), font=("Tahoma", 7))
                signup_screen.after(5000, lambda :canvas_signup.itemconfig(error_text_signup, text=""))
                #signup()
            else:
                def choose_pass_signup():
                    global user_id
                    if len(entry1_signup.get()) == 0:
                        canvas_signup.itemconfig(error_text_signup, text="Veuillez entrer un mot de passe", font=("Tahoma", 10))
                        signup_screen.after(5000, lambda :canvas_signup.itemconfig(error_text_signup, text=""))    
                    else:
                        if len(entry1_signup.get()) <5:
                            canvas_signup.itemconfig(error_text_signup, text="Utilisez 5 caractères ou plus pour votre mot de passe.", font=("Tahoma", 7))
                            signup_screen.after(5000, lambda :canvas_signup.itemconfig(error_text_signup, text=""))    
                        else:
                            new_password_user = entry1_signup.get()
                            salt_signup = os.urandom(32)
                            key_signup = hashlib.pbkdf2_hmac('sha256', new_password_user.encode('utf-8'), salt_signup, 100000)
                            key_signup=(key_signup.hex())
                            my_cursor.execute("INSERT INTO users_info(email, password, salt, name, surname) VALUES (%s, %s, %s, %s, %s)", (email_signup, key_signup, salt_signup, name_signup, surname_signup)) 
                            mydb.commit()
                            my_cursor.execute("SELECT user_id FROM users_info WHERE email = '%s'" % (email_signup))
                            user_id_from_db = my_cursor.fetchone()
                            user_id_from_db = int(user_id_from_db[0])
                            user_id = (f"user_{user_id_from_db}")
                            my_cursor.execute("CREATE TABLE %s (`image_id` int NOT NULL AUTO_INCREMENT, `image` longblob NOT NULL, `file_extension` varchar(45) NOT NULL, PRIMARY KEY (`image_id`), `filename` varchar(45) NOT NULL)" % (user_id))
                            
                            mydb.commit()
                            my_cursor.execute("SELECT * FROM users_info WHERE email = '%s' AND password = '%s' AND name = '%s' AND surname = '%s'" % (email_signup, key_signup, name_signup, surname_signup))    
                            if my_cursor.fetchone():
                                canvas_signup.itemconfig(error_text_signup, text=("Compte créé, Bienvenue ! \nVous êtes connecté sous l'adresse mail " + email_signup), font=("Tahoma", 7))
                                mydb.commit()      
                                signup_screen.after(1000, lambda :manage_from_signup(user_id))
                                #show_frame_home()
                            else:
                                canvas_signup.itemconfig(error_text_signup, text="Erreur", font=("Tahoma", 10))
                                signup_screen.after(5000, lambda :canvas_signup.itemconfig(error_text_signup, text=""))
                        #else:
                            #print("Les mots de passe ne correspondent pas, veuillez réessayer")
                            #choose_pass_signup()    
                choose_pass_signup()
        else:
            #print("Adresse e-mail invalide, veuillez réessayer")
            canvas_signup.itemconfig(error_text_signup, text="Adresse e-mail invalide, veuillez réessayer", font=("Tahoma", 10))
            signup_screen.after(5000, lambda :canvas_signup.itemconfig(error_text_signup, text=""))

    global loop_in_files
    def loop_in_files(a,b,a_,b_, all_file_names):
        for file in all_file_names: ####for file in all_file_names:
            #filename = file[0]
            #extension = file[1]
            #print(file)
            dct_ = {file: Button_(file, a, b, a_, b_, canvas_files)}
            b=b+65
            b_ = b_+65
            if b>220: ####### si une ligne est remplie
                b=25
                a=a+75
            if b_>230:
                b_=25
                a_=a_+75
    
        configure_scroll(a)   
        show_frame_files_screen()        
            
    def effective_login():
        global email_login
        global user_id
        email_login = entry1_login.get()
        if re.fullmatch(regex, email_login):
            #my_cursor.execute("SELECT email FROM users_info WHERE email = '%s'" % (email_login))
            #if my_cursor.fetchone():
                if len(entry0_login.get()) == 0:
                    canvas_login.itemconfig(error_text_login, text="Veuillez entrer votre mot de passe", font=("Tahoma", 10))
                    login_screen.after(5000, lambda :canvas_login.itemconfig(error_text_login, text=""))    
                else:
                    my_cursor.execute("SELECT email FROM users_info WHERE email = '%s'" % (email_login))
                    if my_cursor.fetchone():
                        my_cursor.execute("SELECT salt FROM users_info WHERE email = '%s'" % (email_login))
                        salt_from_db = my_cursor.fetchone()
                        salt_from_db= (salt_from_db[0])
                        user_password = entry0_login.get()
                        key_login = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt_from_db, 100000)
                        key_login=(key_login.hex())
                        #print(key_login)
                        my_cursor.execute("SELECT * FROM users_info WHERE email = '%s' AND password = '%s'" % (email_login, key_login))
                        if my_cursor.fetchone():
                            my_cursor.execute("SELECT user_id FROM users_info WHERE email = '%s'" % (email_login))
                            user_id_from_db = my_cursor.fetchone()
                            user_id_from_db = int(user_id_from_db[0])
                            user_id = (f"user_{user_id_from_db}")
                            #print("Bienvenue", prenom, nom, "vous êtes connecté !")
                            canvas_login.itemconfig(error_text_login, text=("Vous êtes connecté sous l'adresse " + email_login +  "\nBienvenue"), font=("Tahoma", 7))
                            #global name_from_db
                            login_screen.after(1000, lambda :manage_from_login())
                        else:
                            canvas_login.itemconfig(error_text_login, text=("Mot de passe incorrect, veuillez réessayer"), font=("Tahoma", 10))
                            login_screen.after(5000, lambda :canvas_login.itemconfig(error_text_login, text=""))
                    else:
                        canvas_login.itemconfig(error_text_login, text=("Aucun compte n'existe sous l'adresse " + email_login + " \nVeuillez réessayer ou créez un compte"), font=("Tahoma", 7))
                        login_screen.after(5000, lambda :canvas_login.itemconfig(error_text_login, text=""))
        else:
            canvas_login.itemconfig(error_text_login, text=("E-mail invalide, veuillez réessayer"), font=("Tahoma", 10))
            login_screen.after(5000, lambda :canvas_login.itemconfig(error_text_login, text=""))
    ########## canvas.delete("Error_text") #########
    
        def manage_from_login():
            global a
            my_cursor.execute("SELECT name FROM users_info WHERE email = '%s'" % (email_login))
            name_from_db = my_cursor.fetchone()
            name_from_db = (name_from_db[0])
            name_from_db = str(name_from_db)
            my_cursor.execute("SELECT * from %s" % (user_id))
            number_of_files = my_cursor.rowcount
            if number_of_files > 0:
                my_cursor.execute(f"SELECT filename from {user_id}")
                all_file_names = [row[0] for row in my_cursor.fetchall() if row[0] ]
                manage_text(name_from_db, number_of_files)
                show_frame_manage()
                a=25
                b=25
                a_ = 79
                b_ = 25
                #all_file_names = 20*["Denmark.png"]+20*["Greece.mp4"]
                global loop_in_files
                def loop_in_files(a,b,a_,b_, all_file_names):
                    for file in all_file_names: ####for file in all_file_names:
                        #filename = file[0]
                        #extension = file[1]
                        #print(file)
                        dct_ = {file: Button_(file, a, b, a_, b_, canvas_files)}
                        b=b+65
                        b_ = b_+65
                        if b>220: ####### si une ligne est remplie
                            b=25
                            a=a+75
                        if b_>230:
                            b_=25
                            a_=a_+75
                
                    configure_scroll(a)   
                    show_frame_files_screen()
                loop_in_files(a,b,a_,b_, all_file_names)
            elif number_of_files == 0:
                    manage_text(name_from_db, number_of_files)
                    show_frame_manage()
             
                #time.sleep(4)
                #while True:
            global refresh_files
            def refresh_files():    #####number_of_files
                #my_cursor.execute("SELECT * from %s" % (user_id))
                #number_of_files = my_cursor.rowcount ####### important de placer ça avant mydb.commit
                mydb.commit()       ######### permet de rafraichir la database voir (https://stackoverflow.com/questions/52380528/python-mysql-not-refreshing)
                #my_cursor.execute("SELECT * from %s" % (user_id))  ######### ajouter un bouton pour mettre a jour les fichiers
                #print(my_cursor.rowcount)
                #if my_cursor.rowcount != number_of_files:        ####### si le nombre est différent avec !=
                    #print(" Il y a du nouveau ! :) ")
                    #canvas_files.delete('all')
                list_of = canvas_files.find_all()
                for window_ in list_of:
                    #print(str(window_))
                    canvas_files.delete(window_)
                #number_of_files = my_cursor.rowcount
                my_cursor.execute(f"SELECT filename from {user_id}")
                all_file_names = [row[0] for row in my_cursor.fetchall() if row[0] ]
                a=25
                b=25
                a_ = 79
                b_ = 25
                my_cursor.execute("SELECT * from %s" % (user_id))  ######### ajouter un bouton pour mettre a jour les fichiers
                number_of_files___ = my_cursor.rowcount
                if my_cursor.rowcount == 0:
                    manage_text(name_from_db, number_of_files___)
                    show_frame_manage()
                else:
                    loop_in_files(a,b,a_,b_, all_file_names)
                #window.after(4000, refresh_files, number_of_files)
                #elif number_of_files == 0:
                    #manage_text(name_from_db, number_of_files)
                    #show_frame_manage()
             
                #update_thing()
                #for z in range(0, 50):
                
                    #my_cursor.execute(f"SELECT filename from {user_id}")
                    #all_file_names = [row[0] for row in my_cursor.fetchall() if row[0] ]
                    #loop_in_files(a,b,a_,b_)
                    #time.sleep(2)
                    #Button_(manage_screen, all_file_names)
                    #for filename in all_file_names:
                        #i = i+40
                        #print(i)
                        #txtbox = canvas_manage.create_text(147.5, i, fill="#15C2D6")
                        #canvas_manage.itemconfig(txtbox, text= filename, font=("Tahoma", 14))

            
 
            #show_files_screen()
    


    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    
    def insertBLOB(image, file_extension, file_name):
        print("Inserting BLOB into table_image table")
        try:
            sql_insert_blob_query = (f"INSERT INTO {user_id} (image, file_extension, filename) VALUES (%s,%s,%s)")
            #print(sql_insert_blob_query)
            image = convertToBinaryData(image)
            #print(user_id)
            # Convert data into tuple format
            insert_blob_tuple = (image, file_extension, file_name)
            result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            mydb.commit()
            print("Image and file inserted successfully as a BLOB into table", result)

        except mysql.connector.Error as error:
            print("Failed inserting BLOB data into MySQL table {}".format(error))
        
    
    def import_():
        files_to_insert =  filedialog.askopenfilenames(initialdir="D:/billa/Bureau", filetypes=[("Tout fichier" , "*.*")])
        if files_to_insert:    
            for file_he in files_to_insert:
                file_____name, file_extension = os.path.splitext(file_he)
                file_name = os.path.basename(file_he)
                insertBLOB(file_he, file_extension, file_name)
                mydb.commit()
                refresh_files()
                show_frame_files_screen()
            




############################# Home Frame ####################    
    canvas_home = Canvas(
        home_screen,
        bg = "#037dff",
        height = 640,
        width = 295,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_home.place(x = -0, y = 0)

    background_img_home = PhotoImage(file = path + "background_home.png")
    background = canvas_home.create_image(
        147.5, 320.0,
        image=background_img_home)

    img0_home = PhotoImage(file = path + "img0_home.png")
    b0_home = Button(
        home_screen,
        image = img0_home,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_signup_name,
        relief = "flat")

    b0_home.place(
        x = 35, y = 346,
        width = 223,
        height = 68)


    img1_home = PhotoImage(file = path + "img1_home.png")
    b1_home = Button(
        home_screen,
        image = img1_home,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_login,
        relief = "flat")

    b1_home.place(
        x = 35, y = 434,
        width = 223,
        height = 68)

    ############################# Signup_name Frame ####################

    canvas_signup_name = Canvas(
        signup_name_screen,
        bg = "#ffffff",
        height = 640,
        width = 295,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_signup_name.place(x = 0, y = 0)

    background_img_signup_name = PhotoImage(file = path + "background_signup_name.png")
    background_signup_name = canvas_signup_name.create_image(
        147.5, 320.0,
        image=background_img_signup_name)

    img0_signup_name = PhotoImage(file = path + "img0_signup.png")
    b0_signup_name = Button(
        signup_name_screen,
        image = img0_signup_name,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_home,
        relief = "flat")

    b0_signup_name.place(
        x = 18, y = 24,
        width = 47,
        height = 40)

    img1_signup_name = PhotoImage(file = path + "img1_signup.png")
    b1_signup_name = Button(
        signup_name_screen,
        image = img1_signup_name,
        borderwidth = 0,
        highlightthickness = 0,
        command = check_names,
        relief = "flat")

    b1_signup_name.place(
        x = 37, y = 414,
        width = 223,
        height = 68)


    entry0_img_signup_name = PhotoImage(file = path + "img_textBox0_signup.png")
    entry0_bg_signup_name = canvas_signup_name.create_image(
        147.5, 264.0,
        image = entry0_img_signup_name)

    entry0_signup_name = Entry(
        signup_name_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0_signup_name.place(
        x = 31.67521381378174, y = 244,
        width = 231.64957237243652,
        height = 41)




    entry1_img_signup_name = PhotoImage(file = path + "img_textBox1_signup.png")
    entry1_bg_signup_name = canvas_signup_name.create_image(
        147.5, 356.0,
        image = entry1_img_signup_name)

    entry1_signup_name = Entry(
        signup_name_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1_signup_name.place(
        x = 31.67521381378174, y = 336,
        width = 231.64957237243652,
        height = 41)


    error_text_signup_name = canvas_signup_name.create_text(147.5,400, fill="darkblue",font="Tahoma")




    #############################Signup Frame####################

    canvas_signup = Canvas(
        signup_screen,
        bg = "#ffffff",
        height = 640,
        width = 295,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_signup.place(x = 0, y = 0)

    background_img_signup = PhotoImage(file = path + "background_signup.png")
    background_signup = canvas_signup.create_image(
        147.5, 320.0,
        image=background_img_signup)

    img0_signup = PhotoImage(file = path + "img0_signup.png")
    b0_signup = Button(
        signup_screen,
        image = img0_signup,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_home,
        relief = "flat")

    b0_signup.place(
        x = 18, y = 24,
        width = 47,
        height = 40)

    img1_signup = PhotoImage(file = path + "img1_signup.png")
    b1_signup = Button(
        signup_screen,
        image = img1_signup,
        borderwidth = 0,
        highlightthickness = 0,
        command = effective_signup,
        relief = "flat")

    b1_signup.place(
        x = 37, y = 414,
        width = 223,
        height = 68)


    entry0_img_signup = PhotoImage(file = path + "img_textBox0_signup.png")
    entry0_bg_signup = canvas_signup.create_image(
        147.5, 264.0,
        image = entry0_img_signup)

    entry0_signup = Entry(
        signup_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0_signup.place(
        x = 31.67521381378174, y = 244,
        width = 231.64957237243652,
        height = 41)




    entry1_img_signup = PhotoImage(file = path + "img_textBox1_signup.png")
    entry1_bg_signup = canvas_signup.create_image(
        147.5, 356.0,
        image = entry1_img_signup)

    entry1_signup = Entry(
        signup_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        show="•")

    entry1_signup.place(
        x = 31.67521381378174, y = 336,
        width = 231.64957237243652,
        height = 41)


    error_text_signup = canvas_signup.create_text(147.5,400, fill="darkblue",font="Tahoma")





    ########################Login Frame#####################



    canvas_login = Canvas(
        login_screen,
        bg = "#ff0000",
        height = 640,
        width = 295,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_login.place(x = 0, y = 0)

    background_img_login = PhotoImage(file = path + "background_login.png")
    background_login = canvas_login.create_image(
        147.5, 320.0,
        image=background_img_login)

    img0_login = PhotoImage(file = path + "img0_login.png")
    b0_login = Button(
        login_screen,
        image = img0_login,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_home,
        relief = "flat")

    b0_login.place(
        x = 18, y = 24,
        width = 47,
        height = 40)

    img1_login = PhotoImage(file = path + "img1_login.png")
    b1_login = Button(
        login_screen,
        image = img1_login,
        borderwidth = 0,
        highlightthickness = 0,
        command = effective_login,
        relief = "flat")

    b1_login.place(
        x = 45, y = 421,
        width = 205,
        height = 54)

    entry0_img_login = PhotoImage(file = path + "img_textBox0_login.png")
    entry0_bg_login = canvas_login.create_image(
        147.5, 356.0,
        image = entry0_img_login)

    entry0_login = Entry(
        login_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        show="•")

    entry0_login.place(
        x = 31.67521381378174, y = 336,
        width = 231.64957237243652,
        height = 41)

    entry1_img_login = PhotoImage(file = path +  "img_textBox1_login.png")
    entry1_bg_login = canvas_login.create_image(
        147.5, 264.0,
        image = entry1_img_login)

    entry1_login = Entry(
        login_screen,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1_login.place(
        x = 31.67521381378174, y = 244,
        width = 231.64957237243652,
        height = 41)

    error_text_login = canvas_login.create_text(147.5,400, fill="darkblue",font="Tahoma")


    ######################## Manage Frame #####################




    canvas_manage = Canvas(
        manage_screen,
        bg = "#ffffff",
        height = 640,
        width = 295,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_manage.place(x = 0, y = 0)

    background_img_manage = PhotoImage(file = path + "background_manage.png")
    
    background = canvas_manage.create_image(
        147.5, 320.0,
        image=background_img_manage)

    img0_manage = PhotoImage(file = path + "img0_manage.png")
    b0_manage = Button(
        manage_screen,
        image = img0_manage,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_frame_home,
        relief = "flat")

    b0_manage.place(
        x = 18, y = 24,
        width = 47,
        height = 40)
    

    img1_manage = PhotoImage(file = path + "img1_manage.png")
    b1_manage = Button(
        manage_screen,
        image = img1_manage,
        borderwidth = 0,
        highlightthickness = 0,
        command= lambda:import_(),
        relief = "flat")

    b1_manage.place(
        x = 35, y = 500,
        width = 223,
        height = 68)

    message_number_of_files = canvas_manage.create_text(147.5,150, fill="#15C2D6") 


    #manage_screen.tkraise()
    home_screen.tkraise()

    ######################## Files Frame #####################
    
    canvas_files = Canvas(files_screen, width=295, height=640)
    vsb = Scrollbar(canvas_files, orient="vertical", command=canvas_files.yview)
    canvas_files.configure(yscrollcommand=vsb.set)
    #canvas_files.configure(scrollregion=(0,0,10000,a)) ######## si problème: canvas_files.configure(scrollregion=(0,0,10000,10000))
    
    def configure_scroll(y_value):
        canvas_files.configure(scrollregion=(0,0,10000,y_value))
    canvas_files.pack(fill='both', expand=True, side='left')
    vsb.pack(fill='y', side='right')
    #canvas_files.bind("<MouseWheel>", lambda event: canvas_files.configure(scrollregion=canvas_files.bbox("all"))) ####### L'emplacement de cette ligne est très important
    def _on_mousewheel(event):
        canvas_files.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas_files.bind_all("<MouseWheel>", _on_mousewheel)
    #canvas_files.update()
    #window.update()          ################# Update le canvas et la fenêtre peut être une solution
    ### ajouter un clic droit qui ouvre une pop-up pour enregistrer le fichier      
    
    
    refresh_pic = PhotoImage(file = path + "refresh.png")
    refresh_btn = Button(
    canvas_files,
    image = refresh_pic,
    borderwidth = 0,
    highlightthickness = 0,
    command= lambda:refresh_files(),       #######loopyy(number_of_files)
    relief = "flat")
    refresh_btn.place(
    x = 230, y = 590,
    width = 48,
    height = 41)

    window.protocol("WM_DELETE_WINDOW", on_closing)    
    #window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()