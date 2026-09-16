from src.prompts import system_prompt
from src.agents import llm_with_tools

def run_fde_pipeline(user_query: str):
    print(f'\n[FDE AGENT INGEST] Query: {user_query}')
    messages = system_prompt.format_messages(client_name='OmniLogistics', query=user_query)
    response = llm_with_tools.invoke(messages)
    print(f'[LLM DECISION] Generated Tool Calls: {response.tool_calls}')

if __name__ == '__main__':
    run_fde_pipeline('Check stock for SKU-9921 at facility WH-EAST and summarize status.')