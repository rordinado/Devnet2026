#!/usr/bin/env python3
"""
Script template with best practices.

This module serves as a template for creating well-structured Python scripts.
It includes proper documentation, error handling, logging, and argparse setup.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ScriptConfig:
    """Configuration class for script settings."""
    
    def __init__(self, verbose: bool = False):
        """Initialize configuration.
        
        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        if verbose:
            logger.setLevel(logging.DEBUG)


def process_data(data: str) -> str:
    """Process input data.
    
    Args:
        data: Input string to process
        
    Returns:
        Processed string
        
    Raises:
        ValueError: If data is empty
    """
    if not data:
        raise ValueError("Data cannot be empty")
    
    return data.upper()


def main(args: Optional[list] = None) -> int:
    """Main entry point for the script.
    
    Args:
        args: Command-line arguments (for testing)
        
    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    parser = argparse.ArgumentParser(
        description='Script template with best practices'
    )
    parser.add_argument(
        'input',
        help='Input string to process'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output file path'
    )
    
    parsed_args = parser.parse_args(args)
    config = ScriptConfig(verbose=parsed_args.verbose)
    
    try:
        logger.info(f"Processing input: {parsed_args.input}")
        result = process_data(parsed_args.input)
        
        if parsed_args.output:
            parsed_args.output.write_text(result)
            logger.info(f"Output written to {parsed_args.output}")
        else:
            print(result)
        
        logger.info("Process completed successfully")
        return 0
        
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
