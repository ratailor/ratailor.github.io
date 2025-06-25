# AI Assistent using CLI

This script runs an [Ollama AI model](https://ollama.com) locally to
generate conversation with history enabled so that model to remembers
the context about previous questions asked.

I used ollama LLM framework and mistral:7b model to locally run the LLM
and generate the responses for the conversation.

To start conversation with AI assistent you need to install the pre-requisites.

### Requirements
- python3.8+
- [Ollama](https://ollama.com/download) framework to run LLM locally.
- ~8 GB RAM minimum
---

## Installation instructions:

### Install Ollama (here we are doing on linux system)
- Follow instruction to [install Ollama](https://ollama.com/download/linux)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
### Start serving Ollama LLM
```bash
ollama serve &
```

### check for available models (you won't have any by-default)
```bash
ollama list
```

### Pull [mistral:7b](https://ollama.com/library/mistral:7b) model to run on local vm
```bash
ollama pull mistral:7b
```

### Create python virtual environment
```bash
python3 -m venv ai-venv
source ai-venv/bin/activate
pip install ollama
```

### Run the script to start conversation
```bash
python main.py
```
### Example Prompts
```bash python main.py
type '/exit' to quit, '/history' to dump message history.
>>> closest country to antarctica
 The closest countries to Antarctica are Chile and Argentina, as they border the Drake Passage, which separates the southern tip of South America from the Antarctic Peninsula.

1. Chile: The city of Puerto Williams is located on Navarino Island, which is part of the Chilean territories in Antarctica, making it the southernmost city in the world.
2. Argentina: Argentina's Antarctic claim includes the Antarctic Peninsula and several islands surrounding it. The Argentine Base "Esperanza" on the Antarctic Peninsula is one of the largest research stations in Antarctica.

type '/exit' to quite, '/history/' to dump message history.
>>> how far those are
 The Drake Passage separates South America from the Antarctic Peninsula, with an average width of about 600 kilometers (372 miles). From the southernmost tip of Chile (Puerto Williams) to the Antarctic Peninsula, it's approximately 1,050 kilometers (652 miles). The distance from Argentina's mainland to the Antarctic Peninsula is a bit longer.

type '/exit' to quite, '/history/' to dump message history.
>>> longest river in africa
 The longest river in Africa is the Nile River, which originates in south-central Rwanda and flows northwards through Uganda, Sudan, Egypt, and empties into the Mediterranean Sea. The Nile River's total length is approximately 6,650 kilometers (4,130 miles).

The second longest river in Africa is the Congo River, which starts in the Democratic Republic of the Congo and flows westwards through the countries of the Democratic Republic of the Congo, Angola, Republic of the Congo, Gabon, Central African Republic, and the Republic of the Congo before emptying into the Atlantic Ocean. The length of the Congo River is about 4,700 kilometers (2,920 miles).

type '/exit' to quite, '/history/' to dump message history.
>>> how many countries it passes through
 The Nile River flows through eleven countries:

1. Rwanda
2. Burundi
3. Tanzania
4. Uganda
5. Democratic Republic of the Congo (DRC)
6. South Sudan
7. Sudan
8. Egypt
9. Ethiopia
10. Eritrea
11. Kenya

The Congo River flows through six countries:

1. Democratic Republic of the Congo (DRC)
2. Angola
3. Republic of the Congo
4. Gabon
5. Central African Republic
6. Republic of the Congo
type '/exit' to quite, '/history/' to dump message history.
/exit
```
