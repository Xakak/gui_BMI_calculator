import tkinter as tk
from PIL import ImageTk, Image

def calculate_bmi():
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    height_in_m = height / 100

    bmi = weight / (height_in_m * height_in_m)

    bmi_result_label.config(text=f"Your BMI is: {bmi:.2f}.")

    if age >= 2 and age <= 20:
        if bmi < 18.5:
            category = "Underweight"
        elif bmi >= 18.5 and bmi <= 24.5:
            category = "Normal"
        elif bmi > 24.5 and bmi <= 30:
            category = "Overweight"
        elif bmi > 30:
            category = "Obese"
    else:
        if bmi < 18.5:
            category = "Underweight"
        elif bmi >= 18.5 and bmi <= 25:
            category = "Normal"
        elif bmi > 25 and bmi <= 30:
            category = "Overweight"
        elif bmi > 30:
            category = "Obese"

    category_result_label.config(text=f"According to your BMI, You are {category}.")

# Create a new Tkinter window
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(400,200)
window.maxsize(400,200)
#background img:
img=Image.open("/home/rayan/Documents/Python/gui_bmi_calculator/pic1.jpg")
resized_img=img.resize((400,200))
img=ImageTk.PhotoImage(resized_img)

bg_label = tk.Label(window, image=img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)





# Create labels and entry fields
age_label = tk.Label(window, text="Enter your age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

weight_label = tk.Label(window, text="Enter your weight in kg:")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Enter your height in cm:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

bmi_result_label = tk.Label(window, text="")
bmi_result_label.pack()

category_result_label = tk.Label(window, text="")
category_result_label.pack()



# Run the Tkinter event loop
window.mainloop()