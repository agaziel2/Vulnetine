```python
from scenarios import scenarios
from openai_chatgpt import openai_chatgpt

def execute_scenario(scenario):
    response = openai_chatgpt(scenario)
    return response

def scanner():
    results = []
    for scenario in scenarios:
        result = execute_scenario(scenario)
        results.append(result)
    return results
```