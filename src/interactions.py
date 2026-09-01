"""
This module handles interactions with sniffies.com for automated advertising and dating.
"""

import asyncio
import random
import time
from typing import List, Dict, Any
from playwright.async_api import Page
from agents import Agent
from utils import log_message


class InteractionManager:
    """Manages interactions with sniffies.com."""
    
    def __init__(self):
        self.agents: List[Agent] = []
        self.active_sessions = {}
        self.advertisements = []
        self.dating_profiles = []
        
    def add_agent(self, agent: Agent):
        """Add an agent to the manager."""
        self.agents.append(agent)
        
    def load_advertisements(self, ads_data: List[Dict[str, Any]]):
        """Load advertisement data."""
        self.advertisements = ads_data
        log_message(f"Loaded {len(ads_data)} advertisements")
        
    def load_dating_profiles(self, profiles_data: List[Dict[str, Any]]):
        """Load dating profile data."""
        self.dating_profiles = profiles_data
        log_message(f"Loaded {len(profiles_data)} dating profiles")
        
    async def start_interactions(self):
        """Start initial interactions."""
        log_message("Starting interactions...")
        
        # Load some sample data
        sample_ads = [
            {
                "title": "Premium Dating Service",
                "description": "Find your perfect match with our premium service",
                "target_audience": "Single professionals"
            },
            {
                "title": "Dating App Promotion",
                "description": "Join thousands of happy couples today",
                "target_audience": "Young adults"
            }
        ]
        
        sample_profiles = [
            {
                "username": "dating_user_1",
                "age": 28,
                "location": "New York",
                "interests": ["travel", "photography", "cooking"]
            },
            {
                "username": "dating_user_2",
                "age": 32,
                "location": "Los Angeles",
                "interests": ["sports", "music", "hiking"]
            }
        ]
        
        self.load_advertisements(sample_ads)
        self.load_dating_profiles(sample_profiles)
        
    async def process_new_interactions(self):
        """Process new interactions."""
        if not self.agents:
            log_message("No agents available for processing interactions")
            return
            
        # Randomly select an agent to perform actions
        agent = random.choice(self.agents)
        
        # Simulate some interaction logic
        action_type = random.choice(["advertising", "dating"])
        
        if action_type == "advertising":
            await self._perform_advertising_action(agent)
        else:
            await self._perform_dating_action(agent)
            
        log_message(f"Processed interaction with {agent.agent_id}")
        
    async def _perform_advertising_action(self, agent: Agent):
        """Perform advertising-related actions."""
        log_message(f"Performing advertising action with {agent.agent_id}")
        
        if not self.advertisements:
            log_message("No advertisements loaded")
            return
            
        # Select a random advertisement
        ad = random.choice(self.advertisements)
        log_message(f"Selected advertisement: {ad['title']}")
        
        # Simulate posting or sharing
        await asyncio.sleep(random.uniform(1, 3))
        log_message(f"Posted advertisement '{ad['title']}'")
        
    async def _perform_dating_action(self, agent: Agent):
        """Perform dating-related actions."""
        log_message(f"Performing dating action with {agent.agent_id}")
        
        if not self.dating_profiles:
            log_message("No dating profiles loaded")
            return
            
        # Select a random profile
        profile = random.choice(self.dating_profiles)
        log_message(f"Selected profile: {profile['username']}")
        
        # Simulate messaging or liking
        await asyncio.sleep(random.uniform(1, 3))
        action = random.choice(["liked", "messaged"])
        log_message(f"{action} profile '{profile['username']}'")
        
    async def check_for_responses(self):
        """Check for responses to interactions."""
        log_message("Checking for responses...")
        
        # Simulate checking for responses
        if random.random() > 0.7:  # 30% chance of getting a response
            response = random.choice([
                "New message received",
                "Someone liked your post",
                "Profile viewed"
            ])
            log_message(f"Received: {response}")
            
    async def run_campaign(self, campaign_duration: int = 3600):
        """Run a full campaign for the specified duration."""
        log_message(f"Starting campaign for {campaign_duration} seconds")
        
        start_time = time.time()
        while time.time() - start_time < campaign_duration:
            await self.process_new_interactions()
            await self.check_for_responses()
            
            # Wait between actions
            await asyncio.sleep(random.uniform(5, 15))
            
        log_message("Campaign completed")