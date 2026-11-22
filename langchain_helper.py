import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.environ["OPENROUTER_API_KEY"]

llm = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.6,
)

# Chain 1: restaurant name
prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for it. Reply with the name only.",
)
name_chain = prompt_template_name | llm | StrOutputParser()

# Chain 2: menu items
prompt_template_items = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest some menu items for {restaurant_name}. Return them as a comma separated list only.",
)
items_chain = prompt_template_items | llm | StrOutputParser()


def generate_restaurant_name_and_items(cuisine):
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).strip()
    menu_items = items_chain.invoke({"restaurant_name": restaurant_name}).strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items,
    }
