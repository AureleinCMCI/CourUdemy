from openaiapi import *

system_message = "Tu es un assistant plus humain tu t'appelle Alex, tu as 30 ans et tu réponds comme un humain et non comme un assistant virtuel."

messages = []

while True:
    prompt = input("Vous : ")
    print()
    response = getCompletion(prompt, system_message, messages)
    print("Alex: " + response)
    print()