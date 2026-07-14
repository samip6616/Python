"""
Unit tests for the EmailValidator class.
Tests cover valid emails, invalid formats, disposable providers, and edge cases.
"""

import unittest
from email_validator import EmailValidator


class TestEmailValidator(unittest.TestCase):
    """Test cases for EmailValidator class."""
    
    # ==================== VALID EMAILS ====================
    def test_valid_gmail_address(self):
        """Test a valid Gmail address."""
        self.assertTrue(EmailValidator.is_valid('john.doe@gmail.com'))
        is_valid, error = EmailValidator.validate('john.doe@gmail.com')
        self.assertTrue(is_valid)
        self.assertEqual(error, '')
    
    def test_valid_yahoo_address(self):
        """Test a valid Yahoo address."""
        self.assertTrue(EmailValidator.is_valid('jane_smith@yahoo.com'))
        is_valid, error = EmailValidator.validate('jane_smith@yahoo.com')
        self.assertTrue(is_valid)
        self.assertEqual(error, '')
    
    def test_valid_outlook_address(self):
        """Test a valid Outlook address."""
        self.assertTrue(EmailValidator.is_valid('user123@outlook.com'))
        is_valid, error = EmailValidator.validate('user123@outlook.com')
        self.assertTrue(is_valid)
        self.assertEqual(error, '')
    
    def test_valid_hotmail_address(self):
        """Test a valid Hotmail address."""
        self.assertTrue(EmailValidator.is_valid('person@hotmail.com'))
        is_valid, error = EmailValidator.validate('person@hotmail.com')
        self.assertTrue(is_valid)
        self.assertEqual(error, '')
    
    def test_valid_email_with_numbers(self):
        """Test a valid email with numbers."""
        self.assertTrue(EmailValidator.is_valid('user2024@gmail.com'))
    
    def test_valid_email_with_plus_sign(self):
        """Test a valid email with plus sign."""
        self.assertTrue(EmailValidator.is_valid('user+tag@gmail.com'))
    
    def test_valid_email_with_dots(self):
        """Test a valid email with dots in local part."""
        self.assertTrue(EmailValidator.is_valid('first.last@yahoo.com'))
    
    def test_valid_email_uppercase(self):
        """Test that uppercase emails are normalized and valid."""
        self.assertTrue(EmailValidator.is_valid('USER@GMAIL.COM'))
    
    def test_valid_email_mixed_case(self):
        """Test mixed case email addresses."""
        self.assertTrue(EmailValidator.is_valid('John.Doe@Gmail.com'))
    
    # ==================== INVALID FORMAT ====================
    def test_email_missing_at_symbol(self):
        """Test email without @ symbol."""
        is_valid, error = EmailValidator.validate('johngmail.com')
        self.assertFalse(is_valid)
        self.assertIn('@', error)
    
    def test_email_with_spaces(self):
        """Test email containing spaces."""
        is_valid, error = EmailValidator.validate('john doe@gmail.com')
        self.assertFalse(is_valid)
        self.assertIn('spaces', error.lower())
    
    def test_email_with_space_before_at(self):
        """Test email with space before @."""
        is_valid, error = EmailValidator.validate('john @gmail.com')
        self.assertFalse(is_valid)
        self.assertIn('spaces', error.lower())
    
    def test_email_missing_local_part(self):
        """Test email missing local part."""
        is_valid, error = EmailValidator.validate('@gmail.com')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    def test_email_missing_domain(self):
        """Test email missing domain part."""
        is_valid, error = EmailValidator.validate('john@')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    def test_email_missing_extension(self):
        """Test email missing domain extension."""
        is_valid, error = EmailValidator.validate('john@gmail')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    def test_email_multiple_at_symbols(self):
        """Test email with multiple @ symbols."""
        is_valid, error = EmailValidator.validate('john@@gmail.com')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    def test_email_invalid_characters(self):
        """Test email with invalid characters."""
        is_valid, error = EmailValidator.validate('john#doe@gmail.com')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    # ==================== DISPOSABLE PROVIDERS ====================
    def test_yopmail_disposable_provider(self):
        """Test that yopmail (disposable provider) is rejected."""
        is_valid, error = EmailValidator.validate('user@yopmail.com')
        self.assertFalse(is_valid)
        self.assertIn('disposable', error.lower())
    
    def test_10minutemail_disposable_provider(self):
        """Test that 10minutemail is rejected."""
        is_valid, error = EmailValidator.validate('user@10minutemail.com')
        self.assertFalse(is_valid)
        self.assertIn('disposable', error.lower())
    
    def test_tempmail_disposable_provider(self):
        """Test that tempmail is rejected."""
        is_valid, error = EmailValidator.validate('user@tempmail.com')
        self.assertFalse(is_valid)
        self.assertIn('disposable', error.lower())
    
    def test_mailinator_disposable_provider(self):
        """Test that mailinator is rejected."""
        is_valid, error = EmailValidator.validate('user@mailinator.com')
        self.assertFalse(is_valid)
        self.assertIn('disposable', error.lower())
    
    # ==================== INVALID PROVIDERS ====================
    def test_invalid_provider_corporate(self):
        """Test email from non-whitelisted provider."""
        is_valid, error = EmailValidator.validate('user@company.com')
        self.assertFalse(is_valid)
        self.assertIn('not in the list of valid providers', error)
    
    def test_invalid_provider_random(self):
        """Test email from random domain."""
        is_valid, error = EmailValidator.validate('user@example.com')
        self.assertFalse(is_valid)
        self.assertIn('not in the list of valid providers', error)
    
    def test_invalid_provider_university(self):
        """Test email from university domain."""
        is_valid, error = EmailValidator.validate('student@university.edu')
        self.assertFalse(is_valid)
        self.assertIn('not in the list of valid providers', error)
    
    # ==================== EDGE CASES ====================
    def test_empty_string(self):
        """Test empty string."""
        is_valid, error = EmailValidator.validate('')
        self.assertFalse(is_valid)
        self.assertIn('non-empty', error.lower())
    
    def test_none_value(self):
        """Test None value."""
        is_valid, error = EmailValidator.validate(None)
        self.assertFalse(is_valid)
        self.assertIn('non-empty', error.lower())
    
    def test_only_at_symbol(self):
        """Test string with only @ symbol."""
        is_valid, error = EmailValidator.validate('@')
        self.assertFalse(is_valid)
        self.assertIn('invalid', error.lower())
    
    def test_very_long_local_part(self):
        """Test email with very long local part."""
        long_local = 'a' * 100
        is_valid, error = EmailValidator.validate(f'{long_local}@gmail.com')
        self.assertTrue(is_valid)
    
    def test_email_with_hyphens_in_domain(self):
        """Test email with hyphens in domain (invalid provider)."""
        is_valid, error = EmailValidator.validate('user@my-domain.com')
        self.assertFalse(is_valid)
        self.assertIn('not in the list of valid providers', error)
    
    # ==================== PROVIDER CASE INSENSITIVITY ====================
    def test_provider_uppercase(self):
        """Test that provider names are case-insensitive."""
        self.assertTrue(EmailValidator.is_valid('user@GMAIL.COM'))
    
    def test_provider_mixed_case(self):
        """Test mixed case provider names."""
        self.assertTrue(EmailValidator.is_valid('user@Gmail.Com'))
    
    def test_disposable_provider_case_insensitive(self):
        """Test that disposable providers are case-insensitive."""
        is_valid, error = EmailValidator.validate('user@YOPMAIL.COM')
        self.assertFalse(is_valid)
        self.assertIn('disposable', error.lower())
    
    # ==================== SPECIAL CHARACTER HANDLING ====================
    def test_email_with_underscore(self):
        """Test email with underscore in local part."""
        self.assertTrue(EmailValidator.is_valid('john_doe@gmail.com'))
    
    def test_email_with_hyphen(self):
        """Test email with hyphen in local part."""
        self.assertTrue(EmailValidator.is_valid('john-doe@gmail.com'))
    
    def test_email_with_percent(self):
        """Test email with percent sign in local part."""
        self.assertTrue(EmailValidator.is_valid('john%doe@gmail.com'))
    
    # ==================== HELPER METHODS ====================
    def test_get_validation_error_valid_email(self):
        """Test get_validation_error returns empty string for valid email."""
        error = EmailValidator.get_validation_error('user@gmail.com')
        self.assertEqual(error, '')
    
    def test_get_validation_error_invalid_email(self):
        """Test get_validation_error returns error message for invalid email."""
        error = EmailValidator.get_validation_error('user@yopmail.com')
        self.assertNotEqual(error, '')
        self.assertIn('disposable', error.lower())
    
    def test_is_valid_method(self):
        """Test is_valid method."""
        self.assertTrue(EmailValidator.is_valid('valid@gmail.com'))
        self.assertFalse(EmailValidator.is_valid('invalid@yopmail.com'))
    
    # ==================== BATCH TESTING ====================
    def test_batch_valid_emails(self):
        """Test multiple valid emails at once."""
        valid_emails = [
            'user1@gmail.com',
            'user2@yahoo.com',
            'user3@outlook.com',
            'john.doe@hotmail.com',
            'jane+tag@gmail.com',
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(EmailValidator.is_valid(email), f'{email} should be valid')
    
    def test_batch_invalid_emails(self):
        """Test multiple invalid emails at once."""
        invalid_emails = [
            'user@yopmail.com',
            'user@tempmail.com',
            'user@company.com',
            'user gmail.com',
            '@gmail.com',
            'user@',
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(EmailValidator.is_valid(email), f'{email} should be invalid')


if __name__ == '__main__':
    unittest.main()
