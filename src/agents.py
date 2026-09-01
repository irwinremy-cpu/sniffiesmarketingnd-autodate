"""
This module manages browser agents for sniffies.com automation.
"""

import asyncio
import random
from typing import List, Dict, Any
from playwright.async_api import async_playwright, BrowserContext, Page
from utils import log_message, random_string


class Agent:
    """Represents a browser agent for sniffies.com automation."""
    
    def __init__(self, agent_id: str, context: BrowserContext):
        self.agent_id = agent_id
        self.context = context
        self.page = None
        self.is_active = False
        
    async def initialize(self):
        """Initialize the agent's browser context."""
        self.page = await self.context.new_page()
        self.is_active = True
        log_message(f"Agent {self.agent_id} initialized")
        
    async def close(self):
        """Close the agent's browser context."""
        if self.page:
            await self.page.close()
        await self.context.close()
        self.is_active = False
        log_message(f"Agent {self.agent_id} closed")


class AgentManager:
    """Manages multiple browser agents for concurrent operations."""
    
    def __init__(self, num_agents: int = 3):
        self.num_agents = num_agents
        self.agents: List[Agent] = []
        self.playwright = None
        
    async def initialize(self):
        """Initialize all agents."""
        self.playwright = await async_playwright().start()
        for i in range(self.num_agents):
            agent_id = f"agent_{i}_{random_string(6)}"
            # Create a new browser context with anti-detection features
            context = await self.playwright.chromium.launch_persistent_context(
                user_data_dir=f"/tmp/{agent_id}",
                headless=False,
                viewport={"width": 1280, "height": 720},
                device_scale_factor=1,
                geolocation={"latitude": random.uniform(30, 50), "longitude": random.uniform(-120, -70)},
                permissions=["geolocation"],
                extra_http_headers={
                    "Accept-Language": random.choice(["en-US,en;q=0.9", "en-GB,en;q=0.9", "fr-FR,fr;q=0.9"]),
                    "DNT": "1",
                    "Upgrade-Insecure-Requests": "1",
                }
            )
            
            agent = Agent(agent_id, context)
            await agent.initialize()
            self.agents.append(agent)
            
        log_message(f"Initialized {len(self.agents)} agents")
        
    async def close_all(self):
        """Close all agents."""
        for agent in self.agents:
            await agent.close()
        if self.playwright:
            await self.playwright.stop()
        log_message("All agents closed")
        
    def get_active_agents(self) -> List[Agent]:
        """Get list of active agents."""
        return [agent for agent in self.agents if agent.is_active]
        
    def get_random_agent(self) -> Agent:
        """Get a random active agent."""
        active_agents = self.get_active_agents()
        return random.choice(active_agents) if active_agents else None