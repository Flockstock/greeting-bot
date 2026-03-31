import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# main window
app = ctk.CTk()
app.title("Greeting Bot")
app.geometry("800x600")
app.resizable(width=True, height=True)
# frame
box = ctk.CTkFrame(app, width=600, height=600,

                corner_radius=10, border_width=2, fg_color="#DBBBE9")

# box.pack(pady=20, padx=20, fill="both", expand=True)
box.pack(pady=20)
# prevent the frame from shrinking
box.pack_propagate(False)
# Light/Dark mode
ctk.set_appearance_mode("Dark")


def toggle_mode():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

mode_button = ctk.CTkButton(
            master=box,
            text="Toggle Light ☀/Dark Mode 🌃",
            command=toggle_mode
        )
mode_button.pack(pady=20)


# label
label = ctk.CTkLabel(
    master=box,
    text="Enter your name:",
    
    font=("Times New Roman", 24, "bold"),
    text_color="black",
    corner_radius=8)

label.pack(pady=60)

# entry
entry = ctk.CTkEntry(
    master=box,
    placeholder_text="Your Name 😸",
    width=200,
    height=40,
    border_width=2,
    corner_radius=10,
    fg_color="#121212"

)
# country dropdown menu
count_var = tk.StringVar(value="Select your country")
country_dropdown = ctk.CTkOptionMenu(
    master=box,
    variable=count_var,
    width=200,
    height=40,
    corner_radius=10,
    values=["India", "USA", "UK", "Canada", "Australia", "Germany"],
    fg_color="#121212"

)
country_dropdown.pack(pady=10)
entry.pack(pady=10)
# button


def button_clicked():
    name = entry.get()
    country = count_var.get()

    if name =="":
        result_label.configure(text="Please enter your name😅")
        return
    if country == "Select your country":
        result_label.configure(text="Please select your country🌎")
        return
#hide first page
    box.pack_forget()
#show bot page
    bot_frame.pack(pady=20)
#update bot greeting
    
    bot_text.configure(
        text=f"Hello {name} from {country}!❄ 🐾🐾"
    )


button = ctk.CTkButton(master=box, text="Submit",
                    command=button_clicked,
                    height=40,
                    width=120,
                    border_width=0,
                    corner_radius=8,
                    hover=True)
button.pack(pady=10)
# bind enter key to the same function
app.bind("<Return>", lambda event: button_clicked())
result_label = ctk.CTkLabel(
    master=box,
    text="",
    font=("Times New Roman", 20),
    wraplength=400
)
result_label.pack(pady=20)
# MAin-Greeting page:-
bot_frame = ctk.CTkFrame(
    app,
    width=600,
    height=600,
    corner_radius=10,
    border_width=2
)
bot_frame.pack_propagate(False)
bot_image = Image.open("bot.png") #bot image
bot_image = bot_image.resize((200 , 200))
bot_photo = ImageTk.PhotoImage(bot_image)
bot_label = ctk.CTkLabel(
    master = bot_frame,
    image=bot_photo,
    text=""
)
bot_label.image = bot_photo
bot_label.pack(side="left", padx=30)
bot_text = ctk.CTkLabel(
    master=bot_frame,
    text="",
    font=("Times New Roman",22),
    wraplength=300,
    justify="left"
)
bot_text.pack(side="left")
#reset the functions
def go_back():
    bot_frame.pack_forget()
    box.pack(pady=20)
    entry.delete(0,tk.End)
    count_var.set("Select your country")
    result_label.configure(text="")

back_button = ctk.CTkButton(
    master=bot_frame,
    text="↩ Back",
    command=go_back,
    width=120
)
back_button.pack(side="bottom", pady=20)


app.bind("Return",lambda event: go_back())

# run the app
app.mainloop()
