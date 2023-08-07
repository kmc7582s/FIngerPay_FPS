import tkinter as tk
from tkinter import CENTER, Label
from tkinter import font
from PIL import Image, ImageTk, ImageSequence
import sys
import pymysql
from tkinter import messagebox

price = {'떡볶이' : 250, '햄버거': 320, '피자': 1300, '치킨': 3000}
order = []
sum = 0

def make_fullscreen(window):
    # 사용자의 화면 크기를 얻어옴
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 윈도우를 화면 크기로 설정
    window.geometry(f"{screen_width}x{screen_height}")

def add(item):
    global sum
    
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    basket2['text'] = "금액: " + str(sum) + "원"
    
    tk.Label(frame_bas_menu, width = 10, height = 2, text=item).pack()

def btn_exit():     ##주문 마치기
    msgbox = messagebox.askquestion('확인', '주문을 마치겠습니까?')
    if msgbox == 'yes' :
        exit()

def payment():      ##주문하기 누른 뒤 나오는 새로운 창
    root3 = tk.Toplevel()
    root3.title("Payment")
    root3.geometry("400x400")
    root3.configure(bg='black')
    tx_font = font.Font(family="nanumsquare", size=12, weight="bold")
    custom_font = font.Font(family="nanumsquare", size=20, weight="bold")

    conn = pymysql.connect(host="uws7-088.cafe24.com", user="kmc7582s", password="FPS597582@", db="kmc7582s", charset='utf8')
    cursor=conn.cursor()

    select_sql = "SELECT * FROM users where account = %s"
    update_sql = "UPDATE users SET coin = %s WHERE account = %s"

    cursor.execute(select_sql,('account'))
    res = cursor.fetchall()

    def play_gif():
        # GIF 애니메이션 파일 열기
        gif_file_path = "img/loading.gif"
        gif = Image.open(gif_file_path)

        # Tkinter 라벨 생성 및 초기 프레임 설정
        gif_label = tk.Label(root3, bg='black')
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

    #결제 성공 창
    def complete() :   
        def close_window():
            root4.destroy()

        root4 = tk.Tk()
        root4.title("결제 성공")
        root4.geometry("400x500")
        root4.configure(bg='black')
        custom_font = font.Font(family="nanumsquare", size=20, weight="bold")
        
        #이미지를 보여주기 위한 라벨 생성
        logo = tk.PhotoImage(file="./img/logo.png")
        Label(root4, image=logo, bg='black').pack(anchor='center',pady=8) 
        agr = tk.PhotoImage(file="./img/icons1.png")
        Label(root4, image=agr, bg='black').pack(anchor='center',pady=8) 
        label = tk.Label(root4, text="결제가 완료되었습니다!",font=custom_font,fg="white",bg='black', pady=18)
        label.pack(padx=20, pady=20)
    
        root4.after(5000, close_window)
        root4.mainloop()
    
    #잔액부족으로 인한 결제 실패 창
    def nobalance() :   
        def close_window():
            root5.destroy()

        root5 = tk.Tk()
        root5.title("결제 실패")
        root5.geometry("400x500")
        root5.configure(bg='black')
        custom_font = font.Font(family="nanumsquare", size=20, weight="bold")
        
        #이미지를 보여주기 위한 라벨 생성
        logo = tk.PhotoImage(file="./img/logo.png")
        Label(root5, image=logo, bg='black').pack(anchor='center',pady=8) 
        disa = tk.PhotoImage(file="./img/iconsd1.png")
        Label(root5, image=disa, bg='black').pack(anchor='center',pady=8) 
        label = tk.Label(root5, text="잔액이 부족합니다.",font=custom_font,fg="white",bg='black', pady=18)
        label.pack(padx=20, pady=20)
        
        root5.after(5000, close_window)
        root5.mainloop()
        
    #회원정보 확인 불가로 인한 결제 실패창     
    def noaccount() :
        def close_window():
            root6.destroy()

        root6 =tk.Tk()
        root6.title("결제 실패")
        root6.geometry("400x500")
        root6.configure(bg='black')
        custom_font = font.Font(family="nanumsquare", size=20, weight="bold")
        
        #이미지를 보여주기 위한 라벨 생성
        logo = tk.PhotoImage(file="./img/logo.png")
        Label(root6, image=logo, bg='black').pack(anchor='center',pady=8) 
        no = tk.PhotoImage(file="./img/iconsd1.png")
        Label(root6, image=no, bg='black').pack(anchor='center',pady=8) 
        label = tk.Label(root6, text="회원정보가 없습니다.",font=custom_font,fg="white",bg='black', pady=18)
        label.pack(padx=20, pady=20)

        root6.after(5000, close_window)
        root6.mainloop()



    message = Label(root3, text="지문을 스캔해주세요.",font=tx_font,fg="green",bg='black')
    message.pack(anchor='center')

    total = Label(root3, text="총 금액 : "+str(sum)+"원",font=custom_font,fg="white",bg='black', pady=18)
    total.pack(anchor='center')

    root3.mainloop()

    for user in res:
        account = user[7]
        coin = user[8]
        if account == None:
            noaccount()
        else :
            if sum < coin:
                coin = user[8]-sum
                #coin값 업데이트
                cursor.execute(update_sql, (coin, account))
                complete()
            else :
                nobalance()

    #업데이트 종료
    conn.commit() 
    conn.close()            


#메인 키오스
root=tk.Tk()
root.title("Finger Pay 전용 Kiosk")
root.attributes('-fullscreen', True)

ttuk = tk.PhotoImage(file="img/ttuk.png")
hamburger = tk.PhotoImage(file="img/hamburger.png")
pizza = tk.PhotoImage(file="img/pizza.png")
chiken = tk.PhotoImage(file="img/chiken.png")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")


# 메뉴판
frame_menu = tk.LabelFrame(root, text="MENU", relief="solid", bd=1) # 테두리
frame_menu.pack(side="left", fill="both", expand=True)

#Canvas와 스크롤 바 생성
canvas = tk.Canvas(frame_menu, width=300, height=300)
scrollbar = tk.Scrollbar(frame_menu, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

#Canvas에 내용을 넣을 프레임 생성
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

tk.Button(inner_frame, image = ttuk, command=lambda: add('떡볶이'), text="떡볶이 2500", compound=tk.TOP).pack(side="left")
tk.Button(inner_frame, image = hamburger, command=lambda: add('햄버거'), text="햄버거 3200", compound=tk.TOP).pack(side="left")
tk.Button(inner_frame, image = pizza, command=lambda: add('피자'), text="피자 13000", compound=tk.TOP).pack(side="left")
tk.Button(inner_frame, image = chiken, command=lambda: add('치킨'), text="치킨 30000", compound=tk.TOP).pack(side="left")
tk.Button(inner_frame, text="exit", command=btn_exit).pack(side="bottom")

#Canvas와 스크롤 바를 프레임에 배치
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#스크롤 바 동작을 위한 바인딩
inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# 장바구니
frame_bas = tk.LabelFrame(root, text="ORDER LIST")
frame_bas.pack(side="right", fill="both", expand=True)

frame_bas_menu = tk.Frame(frame_bas, width=200, height=300, relief="solid", bd=1)
frame_bas_menu.pack()

# tk.Button(frame_bas, text="초기화", command=reset).pack()

basket2 = Label(frame_bas, text="총 금액 : 0원", width = 100, height = 2, fg = "blue")
basket2.pack()

tk.Button(frame_bas, text="주문하기", command=payment).pack()

root.mainloop()