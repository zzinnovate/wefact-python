#!/usr/bin/env python3
"""
Example: Testing Invoice Endpoints with Test Debtor

This example shows how to use the InvoiceTester to test all invoice
endpoints safely without sending emails to real customers.

PREREQUISITES:
1. Run "Initialize Dummy Data" in the CLI first to create the test debtor
2. This ensures emails go to your test email address, not real customers

The tester automatically:
1. Uses the existing test debtor from dummy data initialization
2. Creates NEW invoices for each test run
3. Tests all invoice lifecycle transitions
4. Cleans up test invoices (debtor remains for future tests)
"""

from wefact import WeFact
from wefact_cli.endpoints.invoice_tester import InvoiceTester
from wefact_cli.utils import ensure_api_key, get_test_debtor_code

def main():
    # 1. Check if test debtor exists
    print("Checking for test debtor...")
    test_debtor = get_test_debtor_code()
    if not test_debtor:
        print("❌ Test debtor not found!")
        print("\nPlease run the CLI and select 'Initialize Dummy Data' first.")
        print("This creates a test debtor with your test email address.")
        return
    
    print(f"✓ Test debtor found: {test_debtor}")
    
    # 2. Get API credentials
    api_key = ensure_api_key()
    if not api_key:
        print("❌ API key not found. Please configure WEFACT_API_KEY in .env")
        return
    
    # 3. Initialize WeFact client
    client = WeFact(api_key=api_key)
    
    # 4. Create invoice tester
    tester = InvoiceTester(client)
    
    # 5. Run full lifecycle test
    # This will:
    # - Use the existing test debtor
    # - Create NEW test invoices
    # - Send emails to your test email (not real customers!)
    # - Test all invoice state transitions
    print("\n" + "="*60)
    print("Running Full Invoice Lifecycle Test")
    print("="*60)
    
    results = tester.test_full_lifecycle()
    
    # 6. Show summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    passed = sum(1 for r in results.values() if r.success)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total} tests")
    
    # Show failed tests
    failed = [(name, result) for name, result in results.items() if not result.success]
    if failed:
        print("\n❌ Failed tests:")
        for name, result in failed:
            print(f"  - {name}: {result.message}")
    else:
        print("\n✓ All tests passed!")
    
    # 7. Optional: Run attachment workflow test
    print("\n" + "="*60)
    print("Running Attachment Workflow Test")
    print("="*60)
    
    attachment_results = tester.test_attachment_workflow()
    
    att_passed = sum(1 for r in attachment_results.values() if r.success)
    att_total = len(attachment_results)
    print(f"\nAttachment tests: {att_passed}/{att_total} passed")


if __name__ == '__main__':
    main()
