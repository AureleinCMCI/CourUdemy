from openai import OpenAI
from openaikey import OPENAI_KEY
import requests

client = OpenAI(api_key=OPENAI_KEY)

def getCompletion(prompt, system_prompt = "", messages = []):
    if system_prompt != "" and len(messages) == 0:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": prompt})

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        text = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": text})
        return text
    except Exception as e:
        print("OpenAi Exception : " + str(e))

    return None

def generateImage(prompt, filename=None, cheap_mode=False):
    model = "dall-e-3"  # ou "dall-e-2" pour une option moins coûteuse
    
    # Ajustez la taille selon le mode
    size = "512x512" if cheap_mode else "1024x1024"
    
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        n=1,
    )
    
    image_url = response.data[0].url

    if filename != "":
        print("Téléchargement de l'image...")
        image_data = requests.get(image_url).content
        with open(filename, 'wb') as file:
            file.write(image_data)

    print("Image générée")

    return image_url



if __name__ == "__main__":
    # print(getCompletion("Bonjour"))
    print(generateImage("a very big cat in the snow", filename="cat.png", cheap_mode=True))
    