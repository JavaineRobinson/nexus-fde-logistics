from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

examples = [
    {
        'input': 'Check stock for SKU-104 at WH-NORTH.',
        'output': 'I will check inventory balance for SKU-104 at WH-NORTH using check_inventory.'
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ('human', '{input}'),
    ('ai', '{output}')
])

few_shot = FewShotChatMessagePromptTemplate(example_prompt=example_prompt, examples=examples)

system_prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an FDE Logistics Agent at {client_name}. Follow safety thresholds strictly.'),
    few_shot,
    ('human', '{query}')
])