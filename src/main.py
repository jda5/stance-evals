import asyncio

from clients.openai_client import OpenAIClient
from evals.election_evals import USA_ELECTION_2024_EVAL


async def main():
    client = OpenAIClient(model="gpt-5.1")

    response = await client.generate_structured_output(
        messages=USA_ELECTION_2024_EVAL.messages,
        response_model=USA_ELECTION_2024_EVAL.response_model,
    )
    print(response)


asyncio.run(main())
