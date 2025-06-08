import customtkinter as ctk

#Creating UI
app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.geometry("645x500")
app.title("Unit Converter")


app.grid_columnconfigure (7, weight=1)
app.grid_rowconfigure (7, weight=1)

#changing Frames



def safe_convert(val_str, to_output_raw, unit_in, unit_out, convert_func):
    try:
        val = float(val_str)
        converted = convert_func(val, unit_in, unit_out, )
        to_output_raw.set(f"{converted:.6f}")  
    except ValueError:
        to_output_raw.set("Invalid input")
        


def place_widgets(current_frame,values_in, unit_convert):
    from_input_raw = ctk.StringVar()
    to_output_raw = ctk.StringVar()
    
    
    from_label = ctk.CTkLabel(current_frame, text = "From:", font = ("",20))
    from_label.grid(row = 0, column = 0, sticky = "w", padx = 10)
    to_label = ctk.CTkLabel(current_frame, text="To:", font = ("",20))
    to_label.grid(row = 0, column = 1, sticky = "w", padx = 10)

    input_entry = ctk.CTkEntry(current_frame, corner_radius=5, height = 40, width = 200, textvariable=from_input_raw, font = ("",18))
    input_entry.grid(row = 1, column = 0, sticky = "we", padx = 10)


    output_entry = ctk.CTkEntry(current_frame, corner_radius=5, height = 40, width = 200, textvariable=to_output_raw, font = ("",18))
    output_entry.grid(row = 1, column = 1, sticky = "we", padx = 10)

    input_option_menu = ctk.CTkOptionMenu(current_frame,values = values_in,corner_radius= 5,height = 35,font = ("",16,"bold"),dropdown_font= ("",16,"bold") )
    input_option_menu.grid(row = 2, column = 0, pady = 10, sticky = "we", padx = 10)


    output_option_menu = ctk.CTkOptionMenu(current_frame, values = values_in, corner_radius= 5, height= 35, font = ("",16,"bold"),dropdown_font= ("",16,"bold") )
    output_option_menu.grid(row = 2, column = 1, pady = 10, sticky = "we", padx = 10)


    convert_button = ctk.CTkButton(current_frame,
                                   text = "Convert",
                                   font = ("",18),
                                   corner_radius= 5,
                                   height = 40,
                                   command=lambda: safe_convert(
                                            from_input_raw.get(),
                                            to_output_raw,
                                            input_option_menu.get(),
                                            output_option_menu.get(),
                                            unit_convert
                                        ))
                                                                                                                                            
    convert_button.grid(row = 3, columnspan = 2, pady = 10)







def framepacking (frame1, frame2):
    frame1.grid_forget()
    frame2.grid(rowspan = 7, columnspan=7, sticky = "nsew" )

def len_conversion():
    global cur_frame
    framepacking(cur_frame, len_frame)
    cur_frame = len_frame
    len_values = ["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Inch","Foot"]
    place_widgets(len_frame, len_values, len_convert)

    
    
    

def temp_conversion():
    global cur_frame
    framepacking(cur_frame, temp_frame)
    cur_frame = temp_frame
    temp_values = ["Celsius", "Kelvin", "Fahrenheit"]
    place_widgets(temp_frame, temp_values, temp_convert)


def area_conversion():
    global cur_frame
    framepacking(cur_frame,area_frame)
    cur_frame = area_frame
    area_values = ["Square Meter", "Square Kilometer", "Square Centimeter", "Hectare", "Square Mile", "Square Inch", "Acre"]
    place_widgets(area_frame, area_values, area_convert)


def volume_conversion():
    global cur_frame
    framepacking(cur_frame, volume_frame)
    cur_frame = volume_frame
    volume_values = ["Liter", "Millileter", "Gallon", "Pint", "Cubic Meter", "Cubic Kilometer", "Cubic Mile" ]
    place_widgets(volume_frame, volume_values, volume_convert)


def weight_conversion():
    global cur_frame
    framepacking (cur_frame, weight_frame)
    cur_frame = weight_frame
    weight_values = ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce", "Atomic mass unit"]
    place_widgets(weight_frame, weight_values, weight_convert)

    
def time_conversion():
    global cur_frame
    framepacking (cur_frame, time_frame)
    cur_frame = time_frame
    time_values = ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]
    place_widgets(time_frame, time_values, time_convert)

    
#CONVERTING FUNCTION

def len_convert(val, unit_in, unit_out):
    SI = {
        'Millimeter': 0.001,
        'Centimeter': 0.01,
        'Meter': 1.0,
        'Kilometer': 1000.0,
        'Inch': 0.0254,
        'Mile': 1609.344,
        'Micrometer':0.000001,
        'Nanometer': 0.000000001,
        'Foot': 0.305
    }
    return val * SI[unit_in] / SI[unit_out]

    
    
def temp_convert(val, unit_in, unit_out):
    if unit_in == "Celsius":
        if unit_out == "Fahrenheit":
            return val * 1.8 + 32
        elif unit_out == 'Kelvin':
            return val + 273.15
        else:
            return val
    elif unit_in == 'Fahrenheit':
        if unit_out == 'Celsius':
            return (val - 32) / 1.8
        elif unit_out == 'Kelvin':
            return (val + 459.67) * 5 / 9
        else:
            return val
    elif unit_in == 'Kelvin':
        if unit_out == 'Celsius':
            return val - 273.15
        elif unit_out == 'Fahrenheit':
            return val * 9 / 5 - 459.67
        else:
            return val
    else:
        return val
    
def area_convert(val, unit_in, unit_out):
    
    SI = {"Square Meter": 1.0,
          "Square Kilometer": 1000000,
          "Square Centimeter": 0.0001,
          "Hectare": 10000,
          "Square Mile": 2589990,
          "Square Inch": 0.00064516,
          "Acre":4046.8564224,
          }
    return val * SI[unit_in] / SI[unit_out]
    

def volume_convert(val, unit_in, unit_out):
    SI = {
        "Liter":1,
        "Millileter":0.001,
        "Gallon":3.78541,
        "Pint" : 0.47317625,
        "Cubic Meter": 1000,
        "Cubic Kilometer" : 1000000000000,
        "Cubic Mile" : 4168180000000
        }
    return val * SI[unit_in] / SI[unit_out]
    
    
def weight_convert(val, unit_in, unit_out):
    SI = {
        "Kilogram" : 1,
        "Gram" : 0.001,
        "Milligram" : 0.000001,
        "Metric Ton" : 1000,
        "Pound" : 0.453592,
        "Ounce" : 0.0283495,
        "Atomic mass unit" : 1.660540199E-27,   
    }    
    return val * SI[unit_in] / SI[unit_out]


def time_convert(val, unit_in, unit_out):
    SI = {
        "Second" : 0.0166666667,
        "Minute" : 1,
        "Hour" : 60,
        "Day" : 1440,
        "Week" : 10080,
        "Month" : 43830,
        "Year" : 525960,
    }
    return val * SI[unit_in] / SI[unit_out]





    
#Defining buttons

len_button = ctk.CTkButton(app,text = "Length",height = 40,width= 100, corner_radius=0,font = ("",20),command= len_conversion)
temp_button = ctk.CTkButton(app,text = "Temparature",height = 40,width= 100, corner_radius=0,font = ("",20),command= temp_conversion)
area_button = ctk.CTkButton(app,text = "Area",height = 40,width= 100, corner_radius=0,font = ("",20),command= area_conversion)
volume_button = ctk.CTkButton(app,text = "Volume",height = 40,width= 100, corner_radius=0,font = ("",20),command= volume_conversion)
weight_button = ctk.CTkButton(app,text = "Weight",height = 40,width= 100, corner_radius=0,font = ("",20),command= weight_conversion)
time_button = ctk.CTkButton(app,text = "Time",height = 40,width= 100, corner_radius=0,font = ("",20),command= time_conversion)


#Placing buttons

len_button.grid(row = 0, column = 0,padx = 2, pady = 5)
temp_button.grid(row = 0, column = 1,padx = 2, pady = 5)
area_button.grid(row = 0, column = 2,padx = 2, pady = 5)
volume_button.grid(row = 0, column = 3,padx = 2, pady = 5)
weight_button.grid(row = 0, column = 4,padx = 2, pady = 5)
time_button.grid(row = 0, column = 5,padx = 2, pady = 5)

#Frames...

len_frame = ctk.CTkFrame(app, corner_radius= 0)
temp_frame = ctk.CTkFrame(app, corner_radius= 0)
area_frame = ctk.CTkFrame(app, corner_radius= 0)
weight_frame = ctk.CTkFrame(app, corner_radius= 0)
volume_frame = ctk.CTkFrame(app, corner_radius= 0)
time_frame = ctk.CTkFrame(app, corner_radius= 0)

cur_frame = len_frame

frames = [len_frame, temp_frame, area_frame, weight_frame, volume_frame, time_frame]
for frame in frames:
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)



len_conversion()


#Lenght conversion...


app.mainloop()