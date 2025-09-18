# Deep Agents Demo - Simplified Makefile
# Essential commands for EPAM DIAL API demos

.PHONY: help setup activate demo1 demo2 demo3

# Configuration
PYTHON := python3
VENV := .venv
VENV_BIN := $(VENV)/bin
PYTHON_VENV := $(VENV_BIN)/python

# Colors for output
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
BLUE := \033[34m
RESET := \033[0m

help: ## Show available commands
	@echo "$(BLUE)🚀 Deep Agents Demo with EPAM DIAL API$(RESET)"
	@echo ""
	@echo "$(GREEN)Available Commands:$(RESET)"
	@echo "  $(YELLOW)make setup$(RESET)     - Complete environment setup"
	@echo "  $(YELLOW)make activate$(RESET)  - Activate virtual environment"
	@echo "  $(YELLOW)make demo1$(RESET)     - Run Demo 1: Standard ReAct Agent"
	@echo "  $(YELLOW)make demo2$(RESET)     - Run Demo 2: Deep Agent (Enhanced)"
	@echo ""
	@echo "$(BLUE)Quick Start:$(RESET)"
	@echo "  1. make setup"
	@echo "  2. Edit .env with your DIAL API credentials"
	@echo "  3. make demo1  # Standard agent"
	@echo "  4. make demo2  # Deep agent (see the difference!)"
	@echo ""

setup: ## Complete setup: virtual environment and dependencies
	@echo "$(BLUE)🏗️  Setting up Deep Agents Demo...$(RESET)"
	@echo ""
	@echo "$(YELLOW)Creating virtual environment...$(RESET)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✅ Virtual environment created$(RESET)"
	@echo ""
	@echo "$(YELLOW)Installing dependencies...$(RESET)"
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install -r requirements.txt
	@echo "$(GREEN)✅ Dependencies installed$(RESET)"
	@echo ""
	@echo "$(YELLOW)Setting up configuration...$(RESET)"
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "$(GREEN)✅ .env file created from template$(RESET)"; \
		echo "$(RED)⚠️  Please edit .env and add your DIAL API credentials:$(RESET)"; \
		echo "   - DIAL_API_KEY"; \
		echo "   - DIAL_API_URL"; \
	else \
		echo "$(GREEN)✅ .env file already exists$(RESET)"; \
	fi
	@echo ""
	@echo "$(GREEN)🎉 Setup complete!$(RESET)"
	@echo "$(BLUE)Next: Edit .env file, then run demos$(RESET)"

activate: ## Show command to activate virtual environment
	@echo "$(BLUE)To activate the virtual environment, run:$(RESET)"
	@echo ""
	@echo "$(YELLOW)source $(VENV)/bin/activate$(RESET)"
	@echo ""
	@echo "$(BLUE)Or run demos directly with make commands$(RESET)"

demo1: ## Run Demo 1: Standard ReAct Agent with DIAL API
	@echo "$(BLUE)🚀 Running Demo 1: Standard ReAct Agent$(RESET)"
	@echo "$(YELLOW)Showcasing: Traditional ReAct pattern with DIAL API$(RESET)"
	@echo ""
	@if [ ! -f .env ]; then \
		echo "$(RED)❌ .env file not found. Run 'make setup' first$(RESET)"; \
		exit 1; \
	fi
	$(PYTHON_VENV) demo_1_standard_agent.py
	@echo ""
	@echo "$(GREEN)✅ Demo 1 completed$(RESET)"

demo2: ## Run Demo 2: Deep Agent with Enhanced Capabilities
	@echo "$(BLUE)🚀 Running Demo 2: Deep Agent$(RESET)"
	@echo "$(YELLOW)Showcasing: Deep Agent with 4 pillars + Sub-agents$(RESET)"
	@echo ""
	@if [ ! -f .env ]; then \
		echo "$(RED)❌ .env file not found. Run 'make setup' first$(RESET)"; \
		exit 1; \
	fi
	$(PYTHON_VENV) demo_2_deep_agent.py
	@echo ""
	@echo "$(GREEN)✅ Demo 2 completed$(RESET)"
	@echo ""
	@echo "$(BLUE)💡 Notice the difference in depth and capability!$(RESET)"