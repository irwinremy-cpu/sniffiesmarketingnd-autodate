"""
This is the main entry point for the automaticGrindr application.
"""

import sys
import asyncio
from agents import AgentManager
from interactions import InteractionManager
from database import DatabaseManager
from utils import log_message


async def main():
    # Initialize managers
    log_message("Initializing automaticGrindr application...")
    
    agent_manager = AgentManager(num_agents=2)
    interaction_manager = InteractionManager()
    db_manager = DatabaseManager()
    
    # Initialize agents
    await agent_manager.initialize()
    
    # Add agents to interaction manager
    for agent in agent_manager.get_active_agents():
        interaction_manager.add_agent(agent)
    
    # Perform initial setup
    await interaction_manager.start_interactions()
    
    # Save some sample data to database
    user_id = db_manager.save_user(
        username="sniffies_user_1",
        email="user@example.com",
        age=28,
        location="New York",
        interests=["travel", "photography", "cooking"]
    )
    
    if user_id:
        db_manager.save_interaction(
            user_id=user_id,
            action_type="login",
            target_user=None,
            message="User logged in successfully"
        )
    
    # Start the main loop
    log_message("Starting main loop...")
    try:
        # Run for 10 minutes as a demo
        await interaction_manager.run_campaign(campaign_duration=600)
    except KeyboardInterrupt:
        log_message("Received interrupt signal, shutting down...")
    finally:
        # Cleanup
        await agent_manager.close_all()
        log_message("Application shutdown complete")


if __name__ == '__main__':
    asyncio.run(main())
    sys.exit(0)