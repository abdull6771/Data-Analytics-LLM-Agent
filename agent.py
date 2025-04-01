import os
from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Load API key from environment
os.environ["GROQ_API_KEY"] = "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"
# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define the AnalyticsState
class AnalyticsState(TypedDict):
    data_description: str
    data_exploration: str
    cleaning_strategy: str
    visualization_design: str
    insight_generation: str
    action_recommendations: str
    executive_summary: str

# Define agent functions (nodes)
def data_exploration_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Data Exploration Agent. Your task is to analyze data sources and provide a comprehensive understanding of the dataset.
        
        Data Description: {data_description}
        
        Provide a detailed exploration including:
        1. Initial observations about the data structure
        2. Potential patterns and correlations
        3. Key features that might be significant
        4. Potential anomalies or outliers
        5. Statistical summaries that would be valuable to calculate
        
        Focus on providing a thorough exploration to guide subsequent steps."""
    )
    chain = prompt | llm
    response = chain.invoke({"data_description": state["data_description"]}).content
    return {"data_exploration": response}

def cleaning_strategy_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Data Cleaning Strategy Agent. Recommend data transformation and cleaning procedures based on the exploration results.
        
        Data Exploration: {data_exploration}
        
        Provide detailed recommendations for:
        1. Handling missing values
        2. Outlier detection and treatment
        3. Feature scaling or normalization needs
        4. Feature engineering opportunities
        5. Data type conversions
        6. Specific transformations for analysis readiness
        
        Focus on creating a structured cleaning strategy."""
    )
    chain = prompt | llm
    response = chain.invoke({"data_exploration": state["data_exploration"]}).content
    return {"cleaning_strategy": response}

def visualization_design_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Visualization Design Agent. Recommend optimal chart types and layouts based on the cleaned data structure and exploration findings.
        
        Data Exploration: {data_exploration}
        Cleaning Strategy: {cleaning_strategy}
        
        Provide detailed visualization recommendations including:
        1. Specific chart types for different aspects of the data
        2. Dashboard layout suggestions
        3. Color schemes and design principles
        4. Interactive elements to enhance understanding
        5. Specific techniques to highlight key insights
        
        Focus on creating visualizations that communicate the data's story."""
    )
    chain = prompt | llm
    response = chain.invoke({
        "data_exploration": state["data_exploration"],
        "cleaning_strategy": state["cleaning_strategy"]
    }).content
    return {"visualization_design": response}

def insight_generation_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Insight Generation Agent. Extract key insights from the processed data and visualization recommendations.
        
        Data Exploration: {data_exploration}
        Cleaning Strategy: {cleaning_strategy}
        Visualization Design: {visualization_design}
        
        Generate meaningful insights including:
        1. Key patterns and trends identified
        2. Surprising or counterintuitive findings
        3. Correlations and potential causal relationships
        4. Segment-specific observations
        5. Historical context and future projections
        
        Focus on insights valuable for decision-making."""
    )
    chain = prompt | llm
    response = chain.invoke({
        "data_exploration": state["data_exploration"],
        "cleaning_strategy": state["cleaning_strategy"],
        "visualization_design": state["visualization_design"]
    }).content
    return {"insight_generation": response}

def action_recommendation_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Action Recommendation Agent. Suggest business actions based on the insights generated.
        
        Insights: {insight_generation}
        
        Provide actionable recommendations including:
        1. Immediate actions that can be taken
        2. Medium-term strategic adjustments
        3. Long-term planning considerations
        4. Potential experiments or A/B tests
        5. Areas requiring further investigation
        
        Prioritize recommendations based on impact and feasibility."""
    )
    chain = prompt | llm
    response = chain.invoke({"insight_generation": state["insight_generation"]}).content
    return {"action_recommendations": response}

def executive_summary_agent(state: AnalyticsState) -> Dict[str, str]:
    prompt = ChatPromptTemplate.from_template(
        """You are an expert Executive Summary Agent. Compile all findings into a concise, business-friendly report.
        
        Data Exploration: {data_exploration}
        Cleaning Strategy: {cleaning_strategy}
        Visualization Design: {visualization_design}
        Insights: {insight_generation}
        Action Recommendations: {action_recommendations}
        
        Create a comprehensive yet concise summary including:
        1. Overview of the analysis purpose and approach
        2. Key findings and their significance
        3. Most important visualizations (described)
        4. Critical insights for decision makers
        5. Prioritized recommendations with expected outcomes
        6. Next steps and future considerations
        
        Ensure accessibility to non-technical stakeholders."""
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

# Create and compile the LangGraph workflow
graph = StateGraph(AnalyticsState)
graph.add_node("data_exploration_agent", data_exploration_agent)
graph.add_node("cleaning_strategy_agent", cleaning_strategy_agent)
graph.add_node("visualization_design_agent", visualization_design_agent)
graph.add_node("insight_generation_agent", insight_generation_agent)
graph.add_node("action_recommendation_agent", action_recommendation_agent)
graph.add_node("executive_summary_agent", executive_summary_agent)

# Set the workflow sequence
graph.set_entry_point("data_exploration_agent")
graph.add_edge("data_exploration_agent", "cleaning_strategy_agent")
graph.add_edge("cleaning_strategy_agent", "visualization_design_agent")
graph.add_edge("visualization_design_agent", "insight_generation_agent")
graph.add_edge("insight_generation_agent", "action_recommendation_agent")
graph.add_edge("action_recommendation_agent", "executive_summary_agent")
graph.add_edge("executive_summary_agent", END)

# Compile the graph (this makes it available for use in app.py)
graph = graph.compile()

# Optional: Uncomment to test locally
# if __name__ == "__main__":
#     initial_state = {
#         "data_description": "Retail sales data with customer ID, purchase date, product category, amount, location, age, and payment method over 12 months."
#     }
#     result = graph.invoke(initial_state)
#     for key, value in result.items():
#         print(f"{key}:\n{value}\n{'-'*50}")