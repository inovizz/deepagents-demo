#!/usr/bin/env python3
"""
Setup script for Deep Agents Demo
Run this first to ensure everything is configured correctly
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Setup the demo environment"""
    print("🚀 Setting up Deep Agents Demo Environment...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    # Install requirements
    print("📦 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Check for .env file
    if not Path(".env").exists():
        print("⚠️  No .env file found. Creating from template...")
        if Path(".env.example").exists():
            Path(".env.example").read_text()
            print("📝 Please edit .env and add your OPENAI_API_KEY")
        else:
            print("❌ .env.example not found")
            sys.exit(1)
    
    # Test imports
    try:
        import deepagents
        import langchain
        print("✅ All packages installed successfully!")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)
    
    # Test OpenAI connection
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY not set in .env file")
        print("   Add your key to .env file and run again")
    else:
        print("✅ OpenAI API key found")
    
    print("\n✨ Setup complete! You're ready to run the demos:")
    print("   python demo_1_basic.py      - Basic deep agent")
    print("   python demo_2_comparison.py - Shallow vs deep comparison")
    print("   python demo_3_full_demo.py  - Full featured demo")
    print("   jupyter notebook           - Interactive notebook demo")

if __name__ == "__main__":
    setup_environment()