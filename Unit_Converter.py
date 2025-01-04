import tkinter as tk

root=tk.Tk()
root.title("Unit Converter")

#base unit is cm
unitsdata = {
    'mm': 0.1,
    'cm': 1,
    'm': 100,
    'km':100000,
    'in':2.54,
    'ft':30.48,
    'yd':91.44,
    'mi':160934
}

def convertUnit(fromUnit, toUnit, length):
    if(fromUnit== "Select an unit" or toUnit=="Select an unit"):
        resultLevel.config(text="Please select an unit")
        return
    try:
        result = int(length) * (unitsdata[fromUnit] / unitsdata[toUnit])
        print(result)
        resultLevel.config(text=f"{length} {fromUnit}= {result} {toUnit}")
    except ValueError:
        resultLevel.config(text="Please enter the value")


inputArea = tk.Entry(root,border=3, bg='gray', fg='#fff', font=10)
inputArea.grid(row=0, column=0)

selectedFromUnit = tk.StringVar(root)
selectedFromUnit.set("Select an unit")
fromUnitSelectBox = tk.OptionMenu(root, selectedFromUnit, *unitsdata.keys())
fromUnitSelectBox.grid(row=0, column=1)

toTextLabel = tk.Label(root, text="Select target option", padx=20, pady=5, background="gray",font=10)
toTextLabel.grid(row=1, column=0)

selectedToUnit = tk.StringVar(root)
selectedToUnit.set("Select an unit")
toUnitSelectBox = tk.OptionMenu(root, selectedToUnit, *unitsdata.keys())
toUnitSelectBox.grid(row=1, column=1)

convertButton = tk.Button(root, text= "Contvert", font=10,padx=4, pady=3, background="gray", border=2, borderwidth=3, command=lambda:convertUnit(selectedFromUnit.get(), selectedToUnit.get(), inputArea.get()))
convertButton.grid(row=2, column=0, sticky="ew", columnspan=2)

resultLevel = tk.Label(root, text="press convert to calculate", padx=4, pady=5,font=10)
resultLevel.grid(row=3, column=0, columnspan=2)

root.mainloop()