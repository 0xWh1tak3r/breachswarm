from llama_index.core.agent import ReActAgentWorker

from breachswarm.llms.llm import LLM
from breachswarm.sdk_context import SDKContext


class ClaudeLLM(LLM):

    def __init__(self, llm=None, tools=None, instruction="", tool_retriever=None, sdk_context: SDKContext = None):
        super().__init__(llm, tools, instruction, tool_retriever)
        self.agent = ReActAgentWorker.from_tools(
            tools=self.tools,
            system_prompt=self.system_prompt,
            llm=self.llm,
            allow_parallel_tool_calls=False,
            tool_retriever=self.tool_retriever,
            callback_manager=sdk_context.get_utility("callback_manager"),
        ).as_agent()
