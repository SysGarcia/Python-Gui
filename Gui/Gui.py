import customtkinter as ctk
import Utils as U

def App_Instance():
    app = ctk.CTk()
    return app

def App_Widgets():
    button = ctk.CTkButton(app, text="my button", command=U.get_path_origen)
    button.pack(padx=20, pady=20)

def Run_App(app):
    DIMENSIONS = {'height':400, 'width':150} 
    app.geometry(f"{DIMENSIONS["height"]}x{DIMENSIONS["width"]}")

    App_Widgets()

    app.mainloop()

app = App_Instance()
Run_App(app)