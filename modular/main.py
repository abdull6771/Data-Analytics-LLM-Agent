from IPython.display import display, Image
from langchain_core.runnables.graph import MermaidDrawMethod
from .workflow import build_workflow

def main():
    # Build and compile the workflow
    graph = build_workflow()
    
    # Initial state
    initial_state = {
        "data_description": """
        The dataset contains sales data from a retail company, 
        including customer transactions with variables such as 
        Customer ID, Purchase Date, Product Category, Product ID, 
        Purchase Amount, Customer Location, Device Used, Customer Age, 
        and Payment Method. It includes approximately 100,000 records 
        collected over a period of 12 months.
        """
    }
    
    # Run the workflow
    result = graph.invoke(initial_state)
    
    # Display the workflow graph
    display(
        Image(
            graph.get_graph().draw_mermaid_png(
                draw_method=MermaidDrawMethod.API
            )
        )
    )
    
    return result

if __name__ == "__main__":
    result = main()
    # You can access results like result["executive_summary"]