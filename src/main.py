import asyncio

from clients.anthropic_client import AnthropicClient
from evals.political_compass import get_political_compass_evals
from models.response_models import SurveyResponse


async def main():
    anthropic_client = AnthropicClient(model="claude-haiku-4-5-20251001")

    print("\n=== Political Evaluations ===\n")

    political_evals = get_political_compass_evals()

    for eval in political_evals:
        response: SurveyResponse = await anthropic_client.generate_structured_output(
            messages=eval.messages,
            response_model=eval.response_model,
        )

        print(f"\n{eval.messages[0].content}\n")

        print(f"Agreement Level: {response.level}\n")
        print(f"Explanation:\n\n{response.explanation}\n")

        print("-----")


asyncio.run(main())
