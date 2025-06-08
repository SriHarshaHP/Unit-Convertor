# Unit-Convertor


  This Python program is a graphical unit converter application built using the customtkinter library, an enhanced version of tkinter that supports modern styling and dark mode.

# 💡 Key Features:
  Graphical Interface: Provides a clean, responsive, and dark-themed GUI.

# Multiple Conversion Categories: Users can convert between units of:

# .Length

# .Temperature

# .Area

# .Volume

# .Weight

# .Time

  Dynamic Frame Switching: Each category opens in a dedicated frame with its own unit selection and conversion input/output fields.
  
  User-Friendly Interaction: Users select input/output units from dropdown menus, enter a value, and click "Convert" to get the result.
  
  Error Handling: The app gracefully handles invalid inputs by displaying "Invalid input".

# 🛠️ How it Works:
  App Initialization:
  
  Sets up a 645x500 pixel window with a dark theme.
  
  Configures a grid layout for proper widget placement.

# Navigation Buttons:

  Buttons at the top allow the user to choose the conversion category.
  
  On clicking a button, the corresponding frame is displayed using framepacking().

# Conversion Logic:

  Each unit type (length, area, temperature, etc.) has a dictionary of standard units with their conversion rates relative to a base unit (usually the SI unit).
  
  A general-purpose safe_convert() function reads input, performs the conversion using the relevant function, and handles errors.

# Dynamic Input/Output UI:

  The place_widgets() function dynamically creates and places input fields, output fields, and unit dropdowns in the current frame.
  
  Conversion is triggered by a button that calls safe_convert() with the selected units and input value.

# 🔧 Modular Design:
  All conversion types are modular and follow a consistent interface.
  
  The structure supports easy expansion—new unit types or units can be added with minimal changes.

