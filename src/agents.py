from langchain_ollama import ChatOllama
from src.tools import check_inventory, trigger_warehouse_reroute
from src.schemas import LogisticsDispatchReport

primary_model = ChatOllama(model='llama3.1', temperature=0)
backup_model = ChatOllama(model='mistral', temperature=0)

tools = [check_inventory, trigger_warehouse_reroute]

llm_with_tools = primary_model.bind_tools(tools).with_fallbacks([backup_model.bind_tools(tools)])
structured_llm = primary_model.with_structured_output(LogisticsDispatchReport, method='json_schema')