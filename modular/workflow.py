from langgraph.graph import StateGraph, END
from .models import AnalyticsState
from .agents import (
    data_exploration_agent,
    cleaning_strategy_agent,
    visualization_design_agent,
    insight_generation_agent,
    action_recommendation_agent,
    executive_summary_agent
)

def build_workflow() -> StateGraph:
    graph = StateGraph(AnalyticsState)
    
    # Add nodes
    graph.add_node("data_exploration_agent", data_exploration_agent)
    graph.add_node("cleaning_strategy_agent", cleaning_strategy_agent)
    graph.add_node("visualization_design_agent", visualization_design_agent)
    graph.add_node("insight_generation_agent", insight_generation_agent)
    graph.add_node("action_recommendation_agent", action_recommendation_agent)
    graph.add_node("executive_summary_agent", executive_summary_agent)

    # Set workflow sequence
    graph.set_entry_point("data_exploration_agent")
    graph.add_edge("data_exploration_agent", "cleaning_strategy_agent")
    graph.add_edge("cleaning_strategy_agent", "visualization_design_agent")
    graph.add_edge("visualization_design_agent", "insight_generation_agent")
    graph.add_edge("insight_generation_agent", "action_recommendation_agent")
    graph.add_edge("action_recommendation_agent", "executive_summary_agent")
    graph.add_edge("executive_summary_agent", END)

    return graph.compile()