from clients.base_llm_client import BaseLLMClient
from errors import AuthenticationError, RefusalError
from models.eval_models import EvalInput, EvalResult, EvalRun


class Evaluator:
    def __init__(
        self, evals: list[EvalInput], llm_clients: list[BaseLLMClient]
    ) -> None:
        self._evals = evals
        self._llm_clients = llm_clients
        self._runs: list[EvalRun] = []

    async def run(self, *args, **kwargs):
        for eval in self._evals:
            for client in self._llm_clients:
                try:
                    response = await client.generate_structured_output(
                        messages=eval.messages,
                        response_model=eval.response_model,
                    )
                    result = EvalResult(
                        input_messages=eval.messages,
                        response=response,
                    )

                except AuthenticationError as e:
                    raise e

                except RefusalError as e:
                    print(f"RefusalError for Client {client.provider}: {e}")
                    result = EvalResult(
                        input_messages=eval.messages,
                        response=None,
                        refusal=True,
                    )

                self._runs.append(
                    EvalRun(
                        model=client.model,
                        provider=client.provider,
                        result=result,
                    )
                )
