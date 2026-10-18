import json

from app.llm_service import generate_response

with open ("evals/test_cases.json") as f:
    test_cases = json.load(f)


def run_evals():

    passed = 0
    for case in test_cases:
        response = generate_response(case['input'])
        keyword = case['expected_keyword'].lower()

        if keyword in response.lower():
            passed += 1
            
    score = passed / len(test_cases)

    print(f"eval_score : {score: 2f}")

    return score

if __name__ == "__main__":
    score = run_evals()

    if score < 0.8:
        raise SystemExit("LLM evaluation failed")
