
def check_vowels(user_input):
   
    vowels = ["a", "e", "o"]
    results = {}
    
    for i in range(0, len(vowels)):
        if vowels[i] in user_input:
            results[vowels[i]] = "found"
        else:
            results[vowels[i]] = "not found"
    
    return results

def test_check_vowels():
    # Test case 1: String containing all three vowels
    result = check_vowels("hello awesome")
    assert result["a"] == "found", f"Expected 'a' to be found in 'hello awesome', got {result['a']}"
    assert result["e"] == "found", f"Expected 'e' to be found in 'hello awesome', got {result['e']}"
    assert result["o"] == "found", f"Expected 'o' to be found in 'hello awesome', got {result['o']}"
    
    # Test case 2: String with only 'a'
    result = check_vowels("cat")
    assert result["a"] == "found", f"Expected 'a' to be found in 'cat', got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in 'cat', got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in 'cat', got {result['o']}"
    
    # Test case 3: String with only 'e'
    result = check_vowels("test")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'test', got {result['a']}"
    assert result["e"] == "found", f"Expected 'e' to be found in 'test', got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in 'test', got {result['o']}"
    
    # Test case 4: String with only 'o'
    result = check_vowels("dog")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'dog', got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in 'dog', got {result['e']}"
    assert result["o"] == "found", f"Expected 'o' to be found in 'dog', got {result['o']}"
    
    # Test case 5: String with no target vowels (but has other vowels)
    result = check_vowels("fun guy")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'fun guy', got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in 'fun guy', got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in 'fun guy', got {result['o']}"
    
    # Test case 6: String with no vowels at all
    result = check_vowels("xyz")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'xyz', got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in 'xyz', got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in 'xyz', got {result['o']}"
    
    # Test case 7: Empty string
    result = check_vowels("")
    assert result["a"] == "not found", f"Expected 'a' to be not found in empty string, got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in empty string, got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in empty string, got {result['o']}"
    
    # Test case 8: String with repeated vowels
    result = check_vowels("aeoaeoaeo")
    assert result["a"] == "found", f"Expected 'a' to be found in 'aeoaeoaeo', got {result['a']}"
    assert result["e"] == "found", f"Expected 'e' to be found in 'aeoaeoaeo', got {result['e']}"
    assert result["o"] == "found", f"Expected 'o' to be found in 'aeoaeoaeo', got {result['o']}"
    
    # Test case 9: Mixed case (should only find lowercase)
    result = check_vowels("HELLO")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'HELLO', got {result['a']}"
    assert result["e"] == "not found", f"Expected 'e' to be not found in 'HELLO', got {result['e']}"
    assert result["o"] == "not found", f"Expected 'o' to be not found in 'HELLO', got {result['o']}"
    
    # Test case 10: Mixed case with lowercase vowels
    result = check_vowels("Hello World")
    assert result["a"] == "not found", f"Expected 'a' to be not found in 'Hello World', got {result['a']}"
    assert result["e"] == "found", f"Expected 'e' to be found in 'Hello World', got {result['e']}"
    assert result["o"] == "found", f"Expected 'o' to be found in 'Hello World', got {result['o']}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_check_vowels()
