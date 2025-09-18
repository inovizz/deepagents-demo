"""
EPAM DIAL API Client for Deep Agents Demo

This module provides the LLM client specifically for EPAM DIAL API integration.
"""

import os
import logging
from typing import List, Dict, Union, Optional
from dataclasses import dataclass

# Azure OpenAI imports for DIAL API
try:
    from openai import AzureOpenAI
    from langchain_openai import AzureChatOpenAI
    AZURE_AVAILABLE = True
except ImportError:
    AZURE_AVAILABLE = False
    print("Azure OpenAI packages not found. Please install: pip install openai langchain-openai")

logger = logging.getLogger(__name__)

@dataclass
class LLMMessage:
    """Message structure for LLM communication"""
    role: str
    content: str

@dataclass 
class LLMResponse:
    """Response structure from LLM"""
    content: str
    model: str
    usage: Dict[str, int]

@dataclass
class DIALSettings:
    """Settings for EPAM DIAL API"""
    dial_api_key: str
    dial_api_url: str
    dial_api_version: str = "2024-02-15-preview"
    model_name: str = "gpt-4"
    temperature: float = 0.0
    max_tokens: int = 1000
    timeout_seconds: int = 30

class LLMClient:
    """Client for driving text/chat completions against EPAM DIAL API."""

    def __init__(self, settings: Optional[DIALSettings] = None):
        if settings is None:
            # Load from environment variables
            self.dial_api_key: str = os.getenv("DIAL_API_KEY", "")
            self.dial_api_url: str = os.getenv("DIAL_API_URL", "")
            self.dial_api_version: str = os.getenv("DIAL_API_VERSION", "2024-02-15-preview")
            self.model_name: str = os.getenv("MODEL_NAME", "gpt-4")
            self.temperature: float = float(os.getenv("TEMPERATURE", "0.0"))
            self.max_tokens: int = int(os.getenv("MAX_TOKENS", "1000"))
            self.timeout: int = int(os.getenv("TIMEOUT_SECONDS", "30"))
        else:
            self.dial_api_key = settings.dial_api_key
            self.dial_api_url = settings.dial_api_url
            self.dial_api_version = settings.dial_api_version
            self.model_name = settings.model_name
            self.temperature = settings.temperature
            self.max_tokens = settings.max_tokens
            self.timeout = settings.timeout_seconds
            
        logger.info(f"LLMClient initialized: using model={self.model_name} via DIAL API")

    async def get_langchain_api(self):
        """Get LangChain compatible API client for DIAL"""
        try:
            if not AZURE_AVAILABLE:
                raise ImportError("AzureChatOpenAI not available")
                
            llm = AzureChatOpenAI(
                azure_deployment=self.model_name,
                api_key=self.dial_api_key,
                api_version=self.dial_api_version,
                azure_endpoint=self.dial_api_url,
                temperature=self.temperature
            )
            logger.info(f"Creating langchain API with model: {self.model_name}")
            return llm
        except Exception as e:
            logger.error(f"Error creating langchain API: {str(e)}")
            raise RuntimeError(f"langchain API creation failed: {str(e)}")

    def get_langchain_api_sync(self):
        """Get LangChain compatible API client for DIAL (synchronous)"""
        try:
            if not AZURE_AVAILABLE:
                raise ImportError("AzureChatOpenAI not available")
                
            llm = AzureChatOpenAI(
                azure_deployment=self.model_name,
                api_key=self.dial_api_key,
                api_version=self.dial_api_version,
                azure_endpoint=self.dial_api_url,
                temperature=self.temperature
            )
            logger.info(f"Creating langchain API with model: {self.model_name}")
            return llm
        except Exception as e:
            logger.error(f"Error creating langchain API: {str(e)}")
            raise RuntimeError(f"langchain API creation failed: {str(e)}")

    async def _call_dial_api(self, messages: List[LLMMessage], temperature: float) -> LLMResponse:
        """Call EPAM DIAL API using AzureOpenAI client."""
        try:
            if not AZURE_AVAILABLE:
                raise ImportError("AzureOpenAI not available")
                
            client = AzureOpenAI(
                api_key=self.dial_api_key,
                azure_endpoint=self.dial_api_url,
                api_version=self.dial_api_version,
            )
            formatted = [{"role": m.role, "content": m.content} for m in messages]

            logger.info(f"Calling DIAL API with model: {self.model_name}")

            resp = client.chat.completions.create(
                model=self.model_name,
                messages=formatted,
                temperature=temperature,
                max_tokens=self.max_tokens,
            )

            usage = {
                "prompt_tokens": resp.usage.prompt_tokens,
                "completion_tokens": resp.usage.completion_tokens,
                "total_tokens": resp.usage.total_tokens,
            }

            logger.info(f"DIAL API response received, {usage['total_tokens']} tokens used")

            return LLMResponse(
                content=resp.choices[0].message.content,
                model=self.model_name,
                usage=usage,
            )
        except Exception as e:
            logger.error(f"DIAL API error: {str(e)}")
            raise RuntimeError(f"DIAL API call failed: {str(e)}")

    async def generate(
        self,
        messages: List[Union[LLMMessage, Dict[str, str]]],
        temperature: Optional[float] = None,
    ) -> LLMResponse:
        """
        Generate a chat completion via DIAL API.

        :param messages: List of dicts or LLMMessage objects
        :param temperature: Override the default temperature
        :returns: LLMResponse
        """
        temp = temperature if temperature is not None else self.temperature

        parsed: List[LLMMessage] = []
        for msg in messages:
            if isinstance(msg, dict):
                parsed.append(LLMMessage(**msg))
            else:
                parsed.append(msg)

        logger.info(f"Generating completion with model {self.model_name} via DIAL API")

        return await self._call_dial_api(parsed, temp)

# Export key classes and functions
__all__ = [
    "LLMClient",
    "LLMMessage", 
    "LLMResponse",
    "DIALSettings",
    "AZURE_AVAILABLE"
]