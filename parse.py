from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


model = OllamaLLM(model="llama3.2:1b")

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

### The AI will use the description from the user to extract info
### Be advised, the template specifies that the AI should only extract the information that directly matches prompt

def parse_withAI(dom_chunks, prompt):
    
    prompt_temp = ChatPromptTemplate.from_template(template, role="user")
    chain = prompt_temp | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": prompt})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)