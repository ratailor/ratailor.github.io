# AI assistent
import ollama

msgs = []

def ask(chat):
  msgs.append(
    {
      'role': 'user',
      'content': chat,
    }
  )
  stream = ollama.chat(
    model = 'mistral:7b',
    messages = msgs,
    stream = True,
  )

  response = ""
  for s in stream:
    part = s['message']['content']
    print(part, end='', flush=True)
    response = response + part

  msgs.append(
    {
      'role': 'assistant',
      'content': response,
    }
  )
  print("type '/exit' to quite, '/history/' to dump message history.")

print("type '/exit' to quit, '/history' to dump message history.")

while True:
    chat = input(">>> ")

    if chat == "/exit":
        break
    elif chat == "/history":
        print(messages)
    elif len(chat) > 0:
        ask(chat)
