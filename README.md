# LLM Analytics Agent

A powerful LLM-powered data analytics agent with a web interface, built using LangChain, LangGraph, and Flask. This project processes a data description through a modular workflow—data exploration, cleaning strategy, visualization design, insight generation, action recommendations, and executive summary generation—delivering actionable insights in a user-friendly browser-based format.

## Features
- **Modular Workflow**: Uses LangGraph to orchestrate a sequence of analytical steps powered by an LLM (Grok’s Llama model via xAI).
- **Web Interface**: Built with Flask, allowing users to input a data description and view detailed outputs.
- **Scalable Design**: Ready for integration with AWS services (e.g., S3 for storage, Lambda for serverless execution).
- **Customizable**: Easily adaptable to different LLMs or data analysis tasks.

## Project Structure
```
llm-analytics-agent/
├── agent.py            # Core LLM agent workflow
├── app.py              # Flask web application
├── templates/
│   ├── index.html      # Input form page
│   └── result.html     # Results display page
├── static/
│   └── style.css       # CSS for styling the web interface
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Prerequisites
- Python 3.8+
- Git installed
- An API key for Grok (xAI) or another LLM provider
- Optional: AWS account for cloud deployment

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdull6771/Data-Analytics-LLM-Agent.git
   cd llm-analytics-agent
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Generate a `requirements.txt` file with:
   ```
   flask
   langchain
   langgraph
   langchain-groq
   ```
   Then install:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   Configure your Grok API key:
   ```bash
   export GROQ_API_KEY="your_grok_api_key"
   ```
   On Windows, use `set` instead of `export`.

## Running the Application

1. **Start the Flask App**:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**:
   Open your browser to `http://127.0.0.1:5000/`. Enter a data description (e.g., "Retail sales data with customer ID, purchase date, product category, amount, location, age, and payment method over 12 months") and click "Analyze" to see the results.

## Usage
- **Input**: Provide a concise description of your dataset in the text area.
- **Output**: The app processes the input through six stages and displays the results, including exploration insights, cleaning recommendations, visualization suggestions, actionable insights, business recommendations, and an executive summary.

## Deployment Options

### Local Deployment
- Use `ngrok` for a temporary public URL:
  ```bash
  ngrok http 5000
  ```
  Share the generated URL with others.

### Cloud Deployment
- **AWS Elastic Beanstalk**:
  1. Package the app with `requirements.txt`.
  2. Use the EB CLI to deploy:
     ```bash
     eb init -p python-3.9 llm-analytics-agent
     eb create llm-agent-env
     ```
  3. Set the `GROQ_API_KEY` environment variable in the EB console.

- **Heroku**:
  1. Add a `Procfile` with:
     ```
     web: python app.py
     ```
  2. Deploy with:
     ```bash
     heroku create
     git push heroku main
     heroku config:set GROQ_API_KEY=your_grok_api_key
     ```

## Extending the Project
- **AWS Integration**: Add S3 for storing inputs/outputs or Lambda for serverless execution (see comments in `agent.py` for pointers).
- **UI Enhancements**: Incorporate file uploads or real-time progress updates in the Flask app.
- **LLM Customization**: Swap Grok for another LLM (e.g., OpenAI) by modifying the `llm` initialization in `agent.py`.

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (add one if desired).

## Contact
For questions or collaboration, reach out via GitHub Issues or connect with me on LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourusername).

---

Happy analyzing!