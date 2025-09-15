def create_framed_string(user_input):
    
    diff = 28 - len(user_input)
    whitespace = diff // 2
    lines = []
    
    lines.append("*" * 30)
    
    if len(user_input) % 2 != 0: 
        whitespace_adjusted = (diff // 2) + 1 
        middle_line = "*" + " " * whitespace + user_input + " " * whitespace_adjusted + "*"
    else: 
        middle_line = "*" + " " * whitespace + user_input + " " * whitespace + "*"
    
    lines.append(middle_line)
    lines.append("*" * 30)
    
    return lines

def test_create_framed_string():
    # Test case 1: Even length string (10 characters)
    result = create_framed_string("HelloWorld")
    expected = [
        "******************************",
        "*         HelloWorld         *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 2: Odd length string (11 characters)
    result = create_framed_string("HelloWorld!")
    expected = [
        "******************************",
        "*        HelloWorld!         *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 3: Short even length string (4 characters)
    result = create_framed_string("test")
    expected = [
        "******************************",
        "*            test            *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 4: Short odd length string (3 characters)
    result = create_framed_string("cat")
    expected = [
        "******************************",
        "*            cat             *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 5: Single character (odd)
    result = create_framed_string("A")
    expected = [
        "******************************",
        "*             A              *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 6: Two characters (even)
    result = create_framed_string("Hi")
    expected = [
        "******************************",
        "*             Hi             *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 7: Empty string (even length - 0)
    result = create_framed_string("")
    expected = [
        "******************************",
        "*                            *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 8: Long even string (26 characters)
    result = create_framed_string("abcdefghijklmnopqrstuvwxyz")
    expected = [
        "******************************",
        "* abcdefghijklmnopqrstuvwxyz *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 9: Long odd string (27 characters)
    result = create_framed_string("abcdefghijklmnopqrstuvwxyz!")
    expected = [
        "******************************",
        "*abcdefghijklmnopqrstuvwxyz! *",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 10: Maximum length (28 characters)
    result = create_framed_string("a" * 28)
    expected = [
        "******************************",
        "*aaaaaaaaaaaaaaaaaaaaaaaaaaaa*",
        "******************************"
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_create_framed_string()
