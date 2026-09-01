"""This is the main entry point for the automaticGrindr application."""

import sys

from agents import AgentManager
from interactions import InteractionManager


def main():
    # Initialize managers
    agent_manager = AgentManager()
    interaction_manager = InteractionManager()

    # Perform initial setup
    agent_manager.load_agents()
    interaction_manager.start_interactions()

    # Start the main loop
    while True:
        interaction_manager.process_new_interactions()
        interaction_manager.check_for_responses()

if __name__ == '__main__':
    main()
    sys.exit(0)