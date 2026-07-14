"""
Email validation module that validates email addresses based on specific rules:
- Proper email format (presence of "@", no spaces)
- Valid email providers (yahoo, gmail, outlook)
- Exclusion of disposable email providers (yopmail, etc.)
"""

import re
from typing import Tuple


class EmailValidator:
    """Validates email addresses based on specific rules."""
    
    # Valid email providers
    VALID_PROVIDERS = {
        'gmail.com',
        'yahoo.com',
        'outlook.com',
        'hotmail.com'
    }
    
    # Disposable/temporary email providers to block
    DISPOSABLE_PROVIDERS = {
        'yopmail.com',
        '10minutemail.com',
        'tempmail.com',
        'throwaway.email',
        'mailinator.com',
        'temp-mail.org',
        'maildrop.cc',
        'spam4.me'
    }
    
    # Email regex pattern for basic format validation
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    @staticmethod
    def validate(email: str) -> Tuple[bool, str]:
        """
        Validates an email address against all defined rules.
        
        Args:
            email: The email address to validate
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
                - is_valid: True if email passes all validations, False otherwise
                - error_message: Empty string if valid, otherwise describes the validation error
        """
        
        # Check if email is None or empty
        if not email or not isinstance(email, str):
            return False, "Email must be a non-empty string"
        
        # Check for spaces
        if ' ' in email:
            return False, "Email address cannot contain spaces"
        
        # Check for presence of "@"
        if '@' not in email:
            return False, "Email address must contain '@' symbol"
        
        # Check basic email format
        if not re.match(EmailValidator.EMAIL_PATTERN, email):
            return False, "Email address format is invalid"
        
        # Extract domain from email
        try:
            domain = email.split('@')[1].lower()
        except IndexError:
            return False, "Email address format is invalid"
        
        # Check if domain is a disposable provider
        if domain in EmailValidator.DISPOSABLE_PROVIDERS:
            return False, f"Disposable email provider '{domain}' is not allowed"
        
        # Check if domain is a valid provider
        if domain not in EmailValidator.VALID_PROVIDERS:
            return False, f"Email provider '{domain}' is not in the list of valid providers"
        
        return True, ""
    
    @staticmethod
    def is_valid(email: str) -> bool:
        """
        Simple boolean check for email validity.
        
        Args:
            email: The email address to validate
            
        Returns:
            bool: True if email is valid, False otherwise
        """
        is_valid, _ = EmailValidator.validate(email)
        return is_valid
    
    @staticmethod
    def get_validation_error(email: str) -> str:
        """
        Gets the validation error message for an invalid email.
        
        Args:
            email: The email address to validate
            
        Returns:
            str: Error message, or empty string if valid
        """
        _, error = EmailValidator.validate(email)
        return error
