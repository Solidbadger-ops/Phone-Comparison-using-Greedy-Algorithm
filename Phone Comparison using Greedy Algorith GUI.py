import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Phone Comparison Tool")

# set up the input fields and labels
tk.Label(root, text="iPhone 14 Pro Max price:").grid(row=0, column=0, padx=5, pady=5)
iphone_price_entry = tk.Entry(root)
iphone_price_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra price:").grid(row=1, column=0, padx=5, pady=5)
samsung_price_entry = tk.Entry(root)
samsung_price_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="iPhone 14 Pro Max storage (GB):").grid(row=2, column=0, padx=5, pady=5)
iphone_storage_entry = tk.Entry(root)
iphone_storage_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra storage (GB):").grid(row=3, column=0, padx=5, pady=5)
samsung_storage_entry = tk.Entry(root)
samsung_storage_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="iPhone 14 Pro Max camera (MP):").grid(row=4, column=0, padx=5, pady=5)
iphone_camera_entry = tk.Entry(root)
iphone_camera_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra camera (MP):").grid(row=5, column=0, padx=5, pady=5)
samsung_camera_entry = tk.Entry(root)
samsung_camera_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="iPhone 14 Pro Max battery (mAh):").grid(row=6, column=0, padx=5, pady=5)
iphone_battery_entry = tk.Entry(root)
iphone_battery_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra battery (mAh):").grid(row=7, column=0, padx=5, pady=5)
samsung_battery_entry = tk.Entry(root)
samsung_battery_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Label(root, text="iPhone 14 Pro Max screen size (inches):").grid(row=8, column=0, padx=5, pady=5)
iphone_screen_size_entry = tk.Entry(root)
iphone_screen_size_entry.grid(row=8, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra screen size (inches):").grid(row=9, column=0, padx=5, pady=5)
samsung_screen_size_entry = tk.Entry(root)
samsung_screen_size_entry.grid(row=9, column=1, padx=5, pady=5)

tk.Label(root, text="iPhone 14 Pro Max weight (g):").grid(row=10, column=0, padx=5, pady=5)
iphone_weight_entry = tk.Entry(root)
iphone_weight_entry.grid(row=10, column=1, padx=5, pady=5)

tk.Label(root, text="Samsung Galaxy S23 Ultra weight (g):").grid(row=11, column=0, padx=5, pady=5)
samsung_weight_entry = tk.Entry(root)
samsung_weight_entry.grid(row=11, column=1, padx=5, pady=5)

# create a function to calculate the best purchase
def calculate_purchase():
    # get the input values
    iphone_price = float(iphone_price_entry.get())
    samsung_price = float(samsung_price_entry.get())
    iphone_storage = float(iphone_storage_entry.get())
    samsung_storage = float(samsung_storage_entry.get())
    iphone_camera = float(iphone_camera_entry.get())
    samsung_camera = float(samsung_camera_entry.get())
    iphone_battery = float(iphone_battery_entry.get())
    samsung_battery = float(samsung_battery_entry.get())
    iphone_screen_size = float(iphone_screen_size_entry.get())
    samsung_screen_size = float(samsung_screen_size_entry.get())
    iphone_weight = float(iphone_weight_entry.get())
    samsung_weight = float(samsung_weight_entry.get())
   
    # calculate a score for each phone
    iphone_score = (iphone_storage * 2) + (iphone_camera * 3) + (iphone_battery * 1.5) + (iphone_screen_size * 0.5) + (2000 / iphone_weight)
    samsung_score = (samsung_storage * 2) + (samsung_camera * 3) + (samsung_battery * 1.5) + (samsung_screen_size * 0.5) + (2000 / samsung_weight)
   
    # determine the best purchase
    if iphone_price <= samsung_price and iphone_score >= samsung_score:
        result = "The iPhone 14 Pro Max is the best purchase."
    elif samsung_price <= iphone_price and samsung_score >= iphone_score:
        result = "The Samsung Galaxy S23 Ultra is the best purchase."
    else:
        result = "Both phones are similarly priced and scored."
   
    # display the result
    result_label.config(text=result)

# create the button to calculate the purchase
calculate_button = tk.Button(root, text="Calculate", command=calculate_purchase)
calculate_button.grid(row=12, column=0, columnspan=2, padx=5, pady=10)

# create the label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=13, column=0, columnspan=2, padx=5, pady=10)

# start the main event loop
root.mainloop()