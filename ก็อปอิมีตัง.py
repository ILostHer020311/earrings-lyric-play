import tkinter as tk
import time
import random

SPEED = 1.0
FONTS = ["Arial", "Courier New", "Times New Roman", "Comic Sans MS","Impact", "Georgia", "Verdana", "Consolas"]
FONT_INTERVAL = 200
font_job = None
root = tk.Tk()
label = tk.Label(root, text="", font=("Arial", 48, "bold"))
label.pack(expand=True)
root.attributes('-fullscreen', True)
root.attributes("-alpha", 0.7)

color_bg = [
    # 1-10 ม่วงเข้ม
    "#1e1e2e", "#241f31", "#2a2139", "#312442", "#38284a",
    "#3f2c52", "#46305a", "#4d3563", "#553a6b", "#5c3f73",
    # 11-20 ชมพูไวน์
    "#63364f", "#6b3556", "#73345c", "#7b3462", "#833a66",
    "#8b4069", "#93466c", "#9b4d6f", "#a35472", "#ab5b75",
    # 21-30 ส้มอำพันอบอุ่น
    "#8f4a52", "#96504d", "#9d5748", "#a45e44", "#aa6540",
    "#a76a3e", "#9f6f42", "#967446", "#8c794b", "#827d50",
    # 31-40 เขียวน้ำทะเล
    "#6f7d58", "#5e7d60", "#4f7c68", "#437a70", "#3a7776",
    "#34727c", "#306c82", "#2f6588", "#315d8d", "#345592",
    # 41-50 น้ำเงิน
    "#384d95", "#3d4598", "#443d98", "#4b3695", "#532f90",
    "#5b2b8a", "#632883", "#6b267b", "#722573", "#79246a",
    # 51-62
    "#6a2460", "#5c2356", "#4f224c", "#422042", "#361e39",
    "#2c1c31", "#241a2a", "#1d1824", "#18161f", "#14131a",
    "#100f15", "#0b0b10",
]

kam = [
    (0.0, "", color_bg[0]),
    (1.69, "Her", color_bg[1]),
    (1.98, "Love", color_bg[2]),
    (2.38, "is", color_bg[3]),
    (2.71, "in", color_bg[4]),
    (3.08, "your", color_bg[5]),
    (3.45, "head", color_bg[6]),
    (3.82, "You", color_bg[7]),
    (4.17, "lost", color_bg[8]),
    (4.57, "your", color_bg[9]),
    (4.97, "earrings", color_bg[10]),
    (5.72, "in", color_bg[11]),
    (6.06, "her", color_bg[12]),
    (6.51, "bed", color_bg[13]),
    (6.91, "You", color_bg[14]),
    (7.22, "couldn't", color_bg[15]),
    (7.89, "tell", color_bg[16]),
    (8.34, "her", color_bg[17]),
    (8.70, "that", color_bg[18]),
    (9.08, "you", color_bg[19]),
    (9.50, "lost", color_bg[20]),
    (9.88, "them", color_bg[21]),
    (10.28, "'Cause", color_bg[22]),
    (10.60, "you're", color_bg[23]),
    (10.93, "scared", color_bg[24]),
    (11.37, "and", color_bg[25]),
    (11.70, "you're", color_bg[26]),
    (12.06, "not", color_bg[27]),
    (12.47, "talking", color_bg[28]),
    (13.21, "So", color_bg[29]),
    (13.59, "you", color_bg[30]),
    (13.94, "think", color_bg[31]),
    (14.30, "of", color_bg[32]),
    (14.71, "what", color_bg[33]),
    (15.07, "to", color_bg[34]),
    (15.41, "say", color_bg[35]),
    (15.82, "Then", color_bg[36]),
    (16.19, "save", color_bg[37]),
    (16.54, "it", color_bg[38]),
    (16.94, "for", color_bg[39]),
    (17.20, "another day", color_bg[40]),
    (18.85, "'Cause", color_bg[41]),
    (19.20, "You", color_bg[42]),
    (19.58, "just", color_bg[43]),
    (19.93, "never", color_bg[44]),
    (20.68, "had", color_bg[45]),
    (21.02, "the", color_bg[46]),
    (21.41, "heart", color_bg[47]),
    (21.82, "Now", color_bg[48]),
    (22.18, "they", color_bg[49]),
    (22.53, "just", color_bg[50]),
    (22.96, "drift", color_bg[51]),
    (23.31, "further", color_bg[52]),
    (24.08, "apart", color_bg[53]),
    (25.20, "From", color_bg[54]),
    (25.56, "You", color_bg[55],True),
    (31.30, "From", color_bg[56]),
    (31.52, "You", color_bg[57],True),
    (37.40, "From", color_bg[58]),
    (37.71, "You", color_bg[59],True),
    (43.37, "From", color_bg[60]),
    (43.61, "You", color_bg[61],True),
]
index = 0

index = 0
if index + 1 < len(kam):
    delay = int((kam[index + 1][0]) * 1000)
else:
    delay = 1000
        
def update_kam():
    global index, font_job
    if index >= len(kam):
        root.destroy()
        return
    
    if font_job is not None:
        root.after_cancel(font_job)
        font_job = None
    label.config(font=("Arial", 48, "bold"))

    item = kam[index]
    start, word, color = item[0], item[1], item[2]
    effect = item[3] if len(item) > 3 else False

    label.config(text=word, bg=color, fg="#cdd6f4")
    root.config(bg=color)

    if effect:
        cycle_font()

    if index + 1 < len(kam):
        delay = int((kam[index + 1][0] - start) * 1000)
    else:
        delay = 1000

    index += 1
    root.after(delay, update_kam)

def cycle_font():
    global font_job
    label.config(font=(random.choice(FONTS), 48, "bold"))
    font_job = root.after(FONT_INTERVAL, cycle_font)

root.title("lyric_earrings")
root.bind("<Escape>", lambda e: root.destroy())

update_kam()
root.mainloop()