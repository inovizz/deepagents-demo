# Deep Agents Demo

This project demonstrates the difference between standard ReAct agents and Deep Agents using the EPAM DIAL API integration.

## 🎯 Overview

This demo showcases two different agent approaches:

1. **Standard ReAct Agent** - Traditional reasoning and acting pattern using LangChain
2. **Deep Agent** - Advanced 4-pillar architecture using the deepagents library

Both agents use the EPAM DIAL API for enterprise-grade AI access with Azure OpenAI backend.

## 🏗️ Architecture

### Standard Agent (Demo 1)
- Uses LangChain's `create_react_agent`
- Simple tool execution with basic reasoning
- Traditional observation-action loop

### Deep Agent (Demo 2)
- Uses deepagents library's `create_deep_agent`
- 4-Pillar Architecture:
  - **Planning**: Advanced task planning and decomposition
  - **File System**: Virtual file management
  - **Instructions**: Dynamic instruction adaptation
  - **Subagents**: Specialized sub-agent coordination

## 📁 Project Structure

```
deep-agents-demo/
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
├── .env.example          # Environment template
├── Makefile              # Project automation
├── dial_client.py        # EPAM DIAL API client
├── utils.py              # Utility functions
├── demo_1_standard_agent.py  # Standard ReAct agent demo
├── demo_2_deep_agent.py      # Deep agent demo
└── old_demos/            # Previous demo versions
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- EPAM DIAL API access credentials

### Setup

1. **Clone and navigate to the project:**
   ```bash
   git clone <your-repo>
   cd deep-agents-demo
   ```

2. **Set up the environment:**
   ```bash
   make setup
   ```

3. **Configure DIAL API credentials:**
   ```bash
   cp .env.example .env
   # Edit .env with your DIAL API credentials
   ```

4. **Activate the environment:**
   ```bash
   make activate
   ```

### Running the Demos

**Standard ReAct Agent:**
```bash
make demo1
```

**Deep Agent:**
```bash
make demo2
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# DIAL API Configuration
DIAL_API_KEY=your-dial-api-key-here
DIAL_API_URL=your-dial-api-url-here
DIAL_API_VERSION=2024-04-01-preview

# Model Configuration
MODEL_NAME=gpt-4
TEMPERATURE=0.7

# Optional: Azure-specific settings
AZURE_OPENAI_ENDPOINT=your-azure-endpoint
AZURE_OPENAI_API_VERSION=2024-02-01
```

### DIAL API Setup

The EPAM DIAL API provides enterprise access to Azure OpenAI models. Ensure you have:

- Valid DIAL API key
- Access to the DIAL API endpoint
- Appropriate model permissions

## 📋 Available Commands

The Makefile provides these essential commands:

```bash
make setup     # Install dependencies and create virtual environment
make activate  # Show activation command for virtual environment
make demo1     # Run standard ReAct agent demo
make demo2     # Run deep agent demo
make help      # Show all available commands
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test both demos
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [deepagents Documentation](https://github.com/DigitalPhilosopher/deepagents)
- [LangChain Documentation](https://python.langchain.com/)
- [EPAM DIAL Platform](https://dial.epam.com/)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

---

**Note:** This demo is designed for educational purposes to showcase the differences between traditional and deep agent architectures in enterprise AI applications.
