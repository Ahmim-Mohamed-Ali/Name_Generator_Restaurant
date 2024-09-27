import secret_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_community.llms import OpenAI  # Après avoir installé langchain-community

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Template pour le nom du restaurant
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest me a fancy name."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Template pour les plats
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated list. Maximum 7 items"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Chaîne séquentielle qui d'abord génère le nom, puis les plats
    chaine = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],  # L'entrée est uniquement la cuisine
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chaine({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
