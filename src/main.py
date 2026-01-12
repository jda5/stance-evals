import asyncio

from clients.openai_client import OpenAIClient
from evals.political_compass import political_evals
from models.response_models import SurveyResponse


async def main():
    openai_client = OpenAIClient(model="gpt-4o-2024-08-06")

    print("\n=== Political Evaluations ===\n")

    for eval in political_evals:
        response: SurveyResponse = await openai_client.generate_structured_output(
            messages=eval.messages,
            response_model=eval.response_model,
        )

        print(f"\n{eval.messages[0].content}\n")

        print(f"Agreement Level: {response.level}\n")
        print(f"Explanation:\n\n{response.explanation}\n")

        print("-----")


asyncio.run(main())
