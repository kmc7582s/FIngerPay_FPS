import tkinter as tk
from tkinter import CENTER, Label
from tkinter import font
from PIL import Image, ImageTk, ImageSequence
import sys
from tkinter import messagebox

price = {'ttuk' : 2500, 'hamburger': 3200, 'pizza': 13000, 'chiken': 30000}
order = []
sum = 0
basket_array=[]
food_number=[]


def add(item) :
    global sum
    this_price = price.get(item)
    sum += this_price
    basket2['text'] = "금액: " + str(sum) + "원"
    if item not in order:
        order.append(item)
        basket = tk.Label(frame_bas_menu, width = 30, height = 2, text=item+' : 1', font=custom_font)
        basket.pack()
        basket_array.append(basket)
        food_number.append(1)
        btn = tk.Button(frame_bas_menu, image = delete)
        btn.pack()
    else:
        food_number[order.index(item)]+=1
        basket_array[order.index(item)]['text'] = item+' : '+str(food_number[order.index(item)])
        
def reset():
    global sum 
    sum = 0
    basket_array.clear()
    food_number.clear()
    order.clear()
    for widget in frame_bas_menu.winfo_children():
        widget.destroy()
    basket2['text'] = "금액 : 0원"





def btn_exit():     ##주문 마치기
    msgbox = messagebox.askquestion('확인', '주문을 마치겠습니까?')
    if msgbox == 'yes' :
        exit()


def payment():      ##주문하기 누른 뒤 나오는 새로운 창 
    root3 = tk.Toplevel()
    root3.title("Payment")
    root3.geometry("400x400")
    tx_font = font.Font(family="nanumsquare", size=12, weight="bold")
    custom_font = font.Font(family="nanumsquare", size=20, weight="bold")
    
    def play_gif():
        # GIF 애니메이션 파일 열기
        gif_file_path = "img/loading_design2.gif"
        gif = Image.open(gif_file_path)

        # Tkinter 라벨 생성 및 초기 프레임 설정
        gif_label = tk.Label(root3)
        gif_label.pack(anchor='center',pady=4)

        # GIF를 Tkinter용 이미지로 변환
        frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

        # 애니메이션 재생 함수
        def update_animation(frame_number):
            gif_label.config(image=frames[frame_number])
            frame_number += 1
            if frame_number == len(frames):
                frame_number = 0
            root.after(animation_speed, update_animation, frame_number)

        # 애니메이션 속도 (밀리초)
        animation_speed = gif.info.get("duration", 100)

        # 애니메이션 시작
        update_animation(0)
    
    # 이미지를 보여주기 위한 라벨 생성
    logo = tk.PhotoImage(file="./img/logo.png")
    Label(root3, image=logo, bg='black').pack(anchor='center',pady=8) 

    play_gif()

    message = Label(root3, text="지문을 스캔해주세요.",font=tx_font,fg="green",bg='black')
    message.pack(anchor='center')

    total = Label(root3, text="총 금액 : "+str(sum)+"원",font=custom_font,fg="white",bg='black', pady=18)
    total.pack(anchor='center')

    root3.configure(bg='black')
    root3.mainloop()

def complete() :
    root4 = tk.Toplevel()





root=tk.Tk()
root.title("Finger Pay 전용 Kiosk")
root.attributes('-fullscreen', True)

custom_font = font.Font(family="nanumsquare", size=20, weight="bold")

ttuk = tk.PhotoImage(file="img/ttuk.png")
hamburger = tk.PhotoImage(file="img/hamburger.png")
pizza = tk.PhotoImage(file="img/pizza.png")
chiken = tk.PhotoImage(file="img/chiken.png")
delete = tk.PhotoImage(file="img/delete.png")

Label(root, text="메뉴를 선택해 주세요", font=custom_font).pack(side="top")


# 메뉴판
frame_menu = tk.LabelFrame(root, text="메뉴", relief="solid", bd=1,font=custom_font) # 테두리
frame_menu.pack(side="left", fill="both", expand=True)

#Canvas와 스크롤 바 생성
canvas = tk.Canvas(frame_menu, width=300, height=300)
scrollbar = tk.Scrollbar(frame_menu, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

#Canvas에 내용을 넣을 프레임 생성
frame_menu = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_menu, anchor="nw")

tk.Button(frame_menu, image = ttuk, command=lambda: add('ttuk')).pack()
tk.Label(frame_menu, text = "떡볶이 2500", font=custom_font).pack()
tk.Button(frame_menu, image = hamburger, command=lambda: add('hamburger')).pack()
tk.Label(frame_menu, text = "햄버거 3200", font=custom_font).pack()
tk.Button(frame_menu, image = pizza, command=lambda: add('pizza')).pack()
tk.Label(frame_menu, text = "피자 13000", font=custom_font).pack()
tk.Button(frame_menu, image = chiken, command=lambda: add('chiken')).pack()
tk.Label(frame_menu, text = "치킨 30000", font=custom_font).pack()
tk.Button(frame_menu, text="exit", command=btn_exit).pack()

#Canvas와 스크롤 바를 프레임에 배치
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#스크롤 바 동작을 위한 바인딩
frame_menu.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# 장바구니
frame_bas = tk.LabelFrame(root, text="장바구니", font=custom_font)
frame_bas.pack(side="right", fill="both", expand=True)

frame_bas_menu = tk.Frame(frame_bas, width=400, height=600, relief="solid", bd=1)
frame_bas_menu.pack()

# frame_bas_menu_r = tk.Frame(frame_bas_menu,width=200, height=600, relief="solid",bd=1).pack(side='right',fill='y',expand=True)
# frame_bas_menu_l = tk.Frame(frame_bas_menu,width=200, height=600,relief="solid",bd=1).pack(side='left',fill='y',expand=True)

tk.Button(frame_bas, text="초기화", command=reset, font=custom_font).pack()

basket2 = Label(frame_bas, text="금액 : 0원", width = 100, height = 2, fg = "blue", font=custom_font)
basket2.pack()

tk.Button(frame_bas, text="주문하기", command=payment, font=custom_font).pack()



root.mainloop()