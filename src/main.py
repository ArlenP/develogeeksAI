from src.llm.ollama_client import OllamaClient

def main():

    llm = OllamaClient(
        model="llama3"
    )

    response = llm.generate(
        "Hola"
    )

    print(response)

if __name__ == "__main__":
    main()
