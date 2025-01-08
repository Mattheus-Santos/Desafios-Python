#Esse programa é um contador regressivo para o ano novo, e ao final ele desenha fogos de artifício na tela.

import time
import turtle
import random

print("Contagem regressiva para o ano novo!!!")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

# Configurações iniciais da janela
window = turtle.Screen()
window.bgcolor("black")


# Função para desenhar um fogo de artifício
def draw_firework():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

    for _ in range(36):  # 36 linhas para criar o efeito de círculo
        t.color(random.choice(colors))
        t.forward(100)
        t.backward(100)
        t.right(10)


# Desenha múltiplos fogos de artifício
for _ in range(10):
    draw_firework()

# Mantém a janela aberta
window.mainloop()