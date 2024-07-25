# AIResearchAssistant


A web-based AI research assistant that provides detailed and contextually relevant answers to user queries. This project uses a Flask backend and a language model to process and respond to research questions, making it an invaluable tool for quick and accurate information retrieval.

## Table of Contents

* Introduction
* Features
* Installation
* Usage
* Configuration

## Introduction

The AI Research Assistant is designed to assist users in obtaining detailed answers to complex research questions. By leveraging advanced natural language processing techniques and integrating external data sources, this application aims to provide accurate and contextually relevant responses.

## Features

* Interactive Query Handling: Allows users to submit queries and receive detailed responses.
* AI-Powered Answers: Utilizes a language model to understand and respond to queries.
* Web-Based Interface: Accessible via a simple web interface, built using Flask.
* Dynamic Content Retrieval: Fetches and processes content from external sources to provide comprehensive answers.

## Installation

### Prerequisites

* Python 3.x
* Flask
* Additional libraries as listed in `requirements.txt`

### Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/bhanuteja625/AIResearchAssistant
   
2. Navigate to the project directory:
   ```bash
   cd ai-research-assistant
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

Usage
To start the Flask application, run the following command:

```bash
python app.py
```
Navigate to http://127.0.0.1:5000/ in your web browser to access the web interface.

Users can input their research queries, and the AI assistant will provide detailed responses based on the information it retrieves and processes.

## Configuration
The application's behavior can be configured in the `config.py` file. Key settings include:

  * Model Configuration:

    * MODEL: Specifies the model file to use.
    * MODEL_TYPE: Type of language model used.
    * MAX_NEW_TOKENS: Maximum number of tokens for responses.
    * TEMPERATURE: Controls the randomness of the model's output.
* Prompt Template:

    *PROMPT_TEMPLATE: Template used to format the prompt for the model.
Adjust these settings according to your needs.
