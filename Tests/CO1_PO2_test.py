def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(a % b, b)

def test_gcd():
    # Test case 1: GCD with one number being 0
    result = gcd(17, 0)
    assert result == 17, f"Expected 17, got {result}"
    
    # Test case 2: GCD of two identical numbers
    result = gcd(13, 13)
    assert result == 13, f"Expected 13, got {result}"
    
    # Test case 3: GCD of two coprime numbers (relatively prime)
    result = gcd(37, 600)
    assert result == 1, f"Expected 1, got {result}"
    
    # Test case 4: GCD where one number divides the other
    result = gcd(20, 100)
    assert result == 20, f"Expected 20, got {result}"
    
    # Test case 5: GCD of two large numbers
    result = gcd(624129, 2061517)
    assert result == 18913, f"Expected 18913, got {result}"
    
    # Test case 6: GCD where smaller number divides larger number
    result = gcd(3, 12)
    assert result == 3, f"Expected 3, got {result}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_gcd()
