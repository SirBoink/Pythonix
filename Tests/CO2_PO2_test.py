
def is_valid_parenthesization(parens):
    depth = 0
    for paren in parens:
        if paren == '(':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return False

    return True

def test_is_valid_parenthesization():
    # Test case 1: Valid nested parentheses
    result = is_valid_parenthesization("((()()))()")
    assert result == True, f"Expected True, got {result}"
    
    # Test case 2: Invalid - starts with closing parenthesis
    result = is_valid_parenthesization(")()(")
    assert result == False, f"Expected False, got {result}"
    
    # Test case 3: Invalid - unmatched opening parentheses
    result = is_valid_parenthesization("((")
    assert result == False, f"Expected False, got {result}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_is_valid_parenthesization()
