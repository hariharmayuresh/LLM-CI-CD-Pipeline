"""
LLM CI/CD Pipeline — App Package
---------------------------------
Exposes the core `generate_response` function at the package level
and serves as the CLI entry point when run via `python -m app`.
"""

from app.llm_service import generate_response

__all__ = ["generate_response"]


def main():
    """Interactive REPL for the LLM service (used as Docker entry point)."""
    print("=== LLM Service (qwen3 via Ollama) ===")
    print("Type your prompt and press Enter. Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            response = generate_response(prompt)
            print(f"\nAssistant: {response}\n")
        except Exception as e:  # noqa: BLE001
            print(f"[Error] Could not get a response: {e}\n")


if __name__ == "__main__":
    main()
