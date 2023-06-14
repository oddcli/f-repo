import random

def generate_message():
    messages = ["Olá!", "Bem-vindo(a) à minha aplicação Flask!", "Divirta-se explorando!", "Esta é uma mensagem aleatória."]
    return random.choice(messages)
