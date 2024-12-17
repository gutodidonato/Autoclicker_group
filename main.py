import os
import random
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pyautogui
import webbrowser  

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        lista_imagens.delete(0, tk.END)  
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                lista_imagens.insert(tk.END, os.path.join(pasta, arquivo))

def verificar_e_clicar():
    tempo_min = int(entry_tempo_min.get())
    tempo_max = int(entry_tempo_max.get())
    tempo_entre_testes = int(entry_tempo_entre_testes.get())
    confianca = float(entry_confianca.get())
    usar_grayscale = var_grayscale.get()

    while True:
        for imagem in lista_imagens.get(0, tk.END):
            try:
                if usar_grayscale:
                    img = Image.open(imagem).convert('L')
                    img.save('temp_grayscale.png')
                    posicao = pyautogui.locateCenterOnScreen('temp_grayscale.png', confidence=confianca)
                else:
                    posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confianca)

                if posicao:
                    tempo_espera = random.uniform(tempo_min, tempo_max)
                    time.sleep(tempo_espera)
                    pyautogui.click(posicao)
                    print(f"Clicou na imagem: {imagem} após {tempo_espera:.2f} segundos.")
                
                # Espera entre cada teste
                time.sleep(tempo_entre_testes)
            except Exception as e:
                print(f"Erro ao verificar a imagem: {e}")
                time.sleep(tempo_entre_testes)
                pass

def abrir_bmc():
    webbrowser.open("https://www.buymeacoffee.com/gutodidonato")


root = tk.Tk()
root.title("Verificador de Imagens")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_escolher = tk.Button(frame, text="Escolher Pasta", command=escolher_pasta)
btn_escolher.pack()

lista_imagens = tk.Listbox(frame, width=50, height=10)
lista_imagens.pack(pady=10)

tk.Label(frame, text="Tempo Mínimo (segundos):").pack()
entry_tempo_min = tk.Entry(frame)
entry_tempo_min.insert(0, "3")  
entry_tempo_min.pack()

tk.Label(frame, text="Tempo Máximo (segundos):").pack()
entry_tempo_max = tk.Entry(frame)
entry_tempo_max.insert(0, "5")  
entry_tempo_max.pack()

tk.Label(frame, text="Tempo Entre Testes (segundos):").pack()
entry_tempo_entre_testes = tk.Entry(frame)
entry_tempo_entre_testes.insert(0, "2")  
entry_tempo_entre_testes.pack()

tk.Label(frame, text="Confiança (0 a 1):").pack()
entry_confianca = tk.Entry(frame)
entry_confianca.insert(0, "0.9")  
entry_confianca.pack()

var_grayscale = tk.BooleanVar()
checkbox_grayscale = tk.Checkbutton(frame, text="Usar Grayscale", variable=var_grayscale)
checkbox_grayscale.pack()

btn_verificar = tk.Button(frame, text="Ativar", command=verificar_e_clicar)
btn_verificar.pack(pady=10)


btn_bmc = tk.Button(frame, text="Buy Me a Coffee", command=abrir_bmc, bg="#FF9500", fg="white", font=("Arial", 12), padx=10, pady=5)
btn_bmc.pack(pady=10)

def on_enter(event):
    event.widget['bg'] = '#FFB300'  

def on_leave(event):
    event.widget['bg'] = '#FF9500' 

btn_bmc.bind("<Enter>", on_enter)
btn_bmc.bind("<Leave>", on_leave)

root.mainloop()