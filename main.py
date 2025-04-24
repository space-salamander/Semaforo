import tkinter as tk
import time
import threading

# Cores do Semáforo
vermelho = "#FD3223"
amarelo = "#F57B14"
verde = "#2AE341"

janela = tk.Tk()
janela.geometry("300x300")  # Aumentei a largura para acomodar os timers
janela.title("Simulador de Semáforo com Timer")


# Criação do Canvas
canvas_largura = 100
canvas_altura = 250
canvas = tk.Canvas(janela, width=canvas_largura, height=canvas_altura, bg="#1E1F22")
canvas.grid(row=0, column=0, rowspan=3, padx=10)

raio = 30
x_centro = canvas_largura // 2
espacamento_vertical = 60

# Criação dos três círculos em posições verticais diferentes
y_centro_vermelho = espacamento_vertical // 2 + raio
circulo_vermelho_id = canvas.create_oval(x_centro - raio, y_centro_vermelho - raio,
                                          x_centro + raio, y_centro_vermelho + raio,
                                          fill="white", outline="black", width=2)

y_centro_amarelo = y_centro_vermelho + espacamento_vertical
circulo_amarelo_id = canvas.create_oval(x_centro - raio, y_centro_amarelo - raio,
                                         x_centro + raio, y_centro_amarelo + raio,
                                         fill="white", outline="black", width=2)

y_centro_verde = y_centro_amarelo + espacamento_vertical
circulo_verde_id = canvas.create_oval(x_centro - raio, y_centro_verde - raio,
                                       x_centro + raio, y_centro_verde + raio,
                                       fill="white", outline="black", width=2)

# Criação dos Labels para os timers
timer_vermelho_label = tk.Label(janela, text="", width=5, font="Arial 20")
timer_vermelho_label.grid(row=0, column=1, padx=5)

timer_verde_label = tk.Label(janela, text="", width=5, font="Arial 20")
timer_verde_label.grid(row=2, column=1, padx=5)

def mudar_cor(cor):
    canvas.itemconfig(circulo_vermelho_id, fill="white")
    canvas.itemconfig(circulo_amarelo_id, fill="white")
    canvas.itemconfig(circulo_verde_id, fill="white")
    timer_vermelho_label.config(text="")
    timer_verde_label.config(text="")

    if cor == "vermelho":
        canvas.itemconfig(circulo_vermelho_id, fill=vermelho)
    elif cor == "amarelo":
        canvas.itemconfig(circulo_amarelo_id, fill=amarelo)
    elif cor == "verde":
        canvas.itemconfig(circulo_verde_id, fill=verde)

    janela.update()

def atualizar_timer(label, tempo):
    if tempo > 0:
        label.config(text=str(tempo))
        janela.after(1000, atualizar_timer, label, tempo - 1) # Atualiza a cada 1 segundo

def ciclo_semaforo():
    mudar_cor("vermelho")
    tempo_vermelho = 60  # Tempo em segundos para o vermelho
    atualizar_timer(timer_vermelho_label, tempo_vermelho)
    time.sleep(tempo_vermelho)

    mudar_cor("amarelo")
    time.sleep(5)

    mudar_cor("verde")
    tempo_verde = 30  # Tempo em segundos para o verde
    atualizar_timer(timer_verde_label, tempo_verde)
    time.sleep(tempo_verde)

    mudar_cor("amarelo")
    time.sleep(1)

    ciclo_semaforo()

# Inicia o ciclo do semáforo em uma thread separada
thread_semaforo = threading.Thread(target=ciclo_semaforo)
thread_semaforo.daemon = True
thread_semaforo.start()

janela.mainloop()