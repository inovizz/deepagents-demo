"""
Utility functions for Deep Agents demo

This module contains simple utility functions for the demo,
without any custom deep agent implementations.
"""

import os
import time
from typing import Dict

# Rich imports for UI
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.tree import Tree
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Rich package not available. Install with: pip install rich")

# DuckDuckGo search import
try:
    from ddgs import DDGS
    DUCKDUCKGO_AVAILABLE = True
except ImportError:
    DUCKDUCKGO_AVAILABLE = False
    print("Warning: ddgs not installed. Install with: pip install ddgs")

if RICH_AVAILABLE:
    console = Console()
else:
    console = None

def web_search(query: str) -> str:
    """Search the web for information using DuckDuckGo"""
    if not DUCKDUCKGO_AVAILABLE:
        return f"DuckDuckGo search unavailable. Please install: pip install ddgs"
    
    try:
        # Use DuckDuckGo to search
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            
        if not results:
            return f"No search results found for: {query}"
        
        # Format results
        formatted_results = f"Search results for '{query}':\n\n"
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            body = result.get('body', 'No description')
            url = result.get('href', 'No URL')
            formatted_results += f"{i}. {title}\n   {body}\n   Source: {url}\n\n"
        
        return formatted_results
        
    except Exception as e:
        return f"Error performing web search: {str(e)}"

def setup_environment() -> bool:
    """Setup and validation for the demo environment"""
    if RICH_AVAILABLE and console:
        console.print("[blue]🔧 Setting up DIAL API environment...[/blue]")
    else:
        print("🔧 Setting up DIAL API environment...")
    
    # Check for DIAL API credentials
    dial_api_key = os.getenv("DIAL_API_KEY")
    dial_api_url = os.getenv("DIAL_API_URL")
    
    if not dial_api_key or dial_api_key == "your-dial-api-key-here":
        if RICH_AVAILABLE and console:
            console.print("[red]❌ Please set your DIAL_API_KEY in .env file[/red]")
        else:
            print("❌ Please set your DIAL_API_KEY in .env file")
        return False
    
    if not dial_api_url or dial_api_url == "your-dial-api-url-here":
        if RICH_AVAILABLE and console:
            console.print("[red]❌ Please set your DIAL_API_URL in .env file[/red]")
        else:
            print("❌ Please set your DIAL_API_URL in .env file")
        return False
    
    if RICH_AVAILABLE and console:
        console.print("[green]✅ DIAL API environment configured successfully[/green]")
    else:
        print("✅ DIAL API environment configured successfully")
    return True

def print_header(title: str):
    """Print a formatted header"""
    if RICH_AVAILABLE and console:
        console.print(f"\n[bold cyan]{'='*60}[/bold cyan]")
        console.print(f"[bold yellow]{title.center(60)}[/bold yellow]")
        console.print(f"[bold cyan]{'='*60}[/bold cyan]\n")
    else:
        print(f"\n{'='*60}")
        print(title.center(60))
        print(f"{'='*60}\n")

def simulate_thinking(message: str, duration: float = 1.0):
    """Simulate agent thinking with spinner"""
    if RICH_AVAILABLE and console:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(message, total=None)
            time.sleep(duration)
        console.print(f"✓ {message}", style="green")
    else:
        print(f"Processing: {message}")
        time.sleep(duration)
        print(f"✓ {message}")

def display_file_tree(files: Dict[str, str]):
    """Display virtual file system as tree"""
    if RICH_AVAILABLE and console:
        tree = Tree("📁 Virtual File System")
        for filename, content in files.items():
            preview = content[:50] + "..." if len(content) > 50 else content
            tree.add(f"📄 {filename}").add(f"[dim]{preview}[/dim]")
        console.print(tree)
    else:
        print("📁 Virtual File System:")
        for filename, content in files.items():
            preview = content[:50] + "..." if len(content) > 50 else content
            print(f"  📄 {filename}: {preview}")

def validate_dependencies():
    """Validate that required dependencies are available"""
    missing_deps = []
    
    if not RICH_AVAILABLE:
        missing_deps.append("rich")
    
    try:
        import dotenv
    except ImportError:
        missing_deps.append("python-dotenv")
    
    try:
        from openai import AzureOpenAI
    except ImportError:
        missing_deps.append("openai")
    
    try:
        from langchain_openai import AzureChatOpenAI
    except ImportError:
        missing_deps.append("langchain-openai")
    
    try:
        from deepagents import create_deep_agent
    except ImportError:
        missing_deps.append("deepagents")
    
    if missing_deps:
        error_msg = f"❌ Missing dependencies: {', '.join(missing_deps)}"
        install_msg = "Install with: pip install -r requirements.txt"
        
        if RICH_AVAILABLE and console:
            console.print(f"[red]{error_msg}[/red]")
            console.print(f"[yellow]{install_msg}[/yellow]")
        else:
            print(error_msg)
            print(install_msg)
        return False
    
    return True

# Export key functions
__all__ = [
    "web_search",
    "setup_environment",
    "print_header", 
    "simulate_thinking",
    "display_file_tree",
    "validate_dependencies",
    "console"
]