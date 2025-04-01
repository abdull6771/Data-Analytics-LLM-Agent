from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from .config import LLM_CONFIG
from .models import AnalyticsState

# Initialize LLM
llm = ChatGroq(**LLM_CONFIG)

def data_exploration_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Data Exploration Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({"data_description": state["data_description"]}).content
    return {"data_exploration": response}

def cleaning_strategy_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Data Cleaning Strategy Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({"data_exploration": state["data_exploration"]}).content
    return {"cleaning_strategy": response}

def visualization_design_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Visualization villeDesign Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({
        "data_exploration": state["data_exploration"],
        "cleaning_strategy": state["cleaning_strategy"]
    }).content
    return {"visualization_design": response}

def insight_generation_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Insight Generation Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({
        "data_exploration": state["data_exploration"],
        "cleaning_strategy": state["cleaning_strategy"],
        "visualization_design": state["visualization_design"]
    }).content
    return {"insight_generation": response}

def action_recommendation_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Action Recommendation Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({"insight_generation": state["insight_generation"]}).content
    return {"action_recommendations": response}

def executive_summary_agent(state: AnalyticsState) -> dict:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Executive Summary Agent...
        # [Full prompt template remains the same as in original code]
        """
    )
    chain = prompt | llm
    response = chain.invoke({
        "data_exploration": state["data_exploration"],
        "cleaning_strategy": state["cleaning_strategy"],
        "visualization_design": state["visualization_design"],
        "insight_generation": state["insight_generation"],
        "action_recommendations": state["action_recommendations"]
    }).content
    return {"executive_summary": response}