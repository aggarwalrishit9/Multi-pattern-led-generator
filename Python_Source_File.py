import tkinter as tk

root = tk.Tk()
root.title("5 LED Pattern Generator")
root.geometry("700x300")
root.configure(bg="black")
sw1_state = tk.IntVar()
sw2_state = tk.IntVar()
canvas = tk.Canvas(root, width=700, height=150, bg="black", highlightthickness=0)
canvas.pack(pady=20)
led_positions = [80, 200, 320, 440, 560]
leds = []

for x in led_positions:
    led = canvas.create_oval(x, 40, x + 60, 100, fill="gray20", outline="white", width=2)
    leds.append(led)
pattern_index = 0
current_pattern = []

def turn_off_all():
    for led in leds:
        canvas.itemconfig(led, fill="gray20")

def update_pattern():
    global pattern_index, current_pattern
    turn_off_all()
    sw1 = sw1_state.get()
    sw2 = sw2_state.get()
    if sw1 == 0 and sw2 == 0:
        patterns = [
            [0],
            [1],
            [2],
            [3],
            [4]
        ]
    elif sw1 == 1 and sw2 == 1:
        patterns = [
            [2],
            [1, 3],
            [0, 4],
            [1, 3]
        ]
    else:
        patterns = [[]]
    current_pattern = patterns[pattern_index % len(patterns)]
    for index in current_pattern:
        canvas.itemconfig(leds[index], fill="yellow")
    pattern_index += 1
    root.after(500, update_pattern)

switch_frame = tk.Frame(root, bg="black")
switch_frame.pack(pady=10)
sw1_check = tk.Checkbutton(
    switch_frame,
    text="SPST Switch 1",
    variable=sw1_state,
    font=("Arial", 12),
    bg="black",
    fg="white",
    selectcolor="gray20",
    activebackground="black",
    activeforeground="white"
)

sw1_check.grid(row=0, column=0, padx=20)
sw2_check = tk.Checkbutton(
    switch_frame,
    text="SPST Switch 2",
    variable=sw2_state,
    font=("Arial", 12),
    bg="black",
    fg="white",
    selectcolor="gray20",
    activebackground="black",
    activeforeground="white"
)
sw2_check.grid(row=0, column=1, padx=20)
update_pattern()
root.mainloop()
