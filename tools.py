from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from lanchain_core.output_parsers import pydantinOutputParser

load_dotenv()

# llm = ChatOpenAI(model = 'gpt-4o-mini')

class ResearchResponse(BaseModel):
    topic:str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatAnthropic(model = 'claude-3-5-sonnet-20241022')
respone = llm.invoke('What is the meaning of God? ')

print(respone)