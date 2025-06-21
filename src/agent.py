from utils import extract_text_from_pdf
from langchain.llms import OpenAI
from data import get_template_str
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SequentialChain

import logging

logging.basicConfig(level=logging.INFO)

# Make sure to run this script from the root of the repository.
# Otherwise, it may fail to locate the file due to an incorrect relative path.
pdf_path = 'src/documents/coffee_info.pdf'
coffee_store_info = extract_text_from_pdf(file_path=pdf_path)

class CoffeeSellerTemplate:
    def __init__(self):
        self.system_template = get_template_str(context=coffee_store_info)

        self.human_template = """
        #### {request}
        """
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt,
                                                             self.human_message_prompt])


class Agent:
    def __init__(self, open_ai_key, model="gpt-4o-mini", temperature=0.1):
        self.open_ai_key = open_ai_key
        self.model = model
        self.temperature = temperature
        self.logger = logging.getLogger(__name__)
        self.chat_model = ChatOpenAI(model=self.model,
                                     temperature=self.temperature,
                                     openai_api_key=self.open_ai_key)

    def get_coffee_answer(self, request):
        seller_prompt = CoffeeSellerTemplate()
        parser = LLMChain(
            llm=self.chat_model,
            prompt=seller_prompt.chat_prompt,
            output_key="coffee"
        )

        chain = SequentialChain(
            chains=[parser],
            input_variables=["request"],
            output_variables=["coffee"],
            verbose=True
        )
        return chain(
            {"request": request},
            return_only_outputs=True
        )
