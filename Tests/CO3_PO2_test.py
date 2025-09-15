def unique_day(day, possible_birthdays):

    count=0

    for i in possible_birthdays:

        if day == i[1]:

            count+=1

        else:

            continue

    if count==1:

        return True

    else:

        return False

def unique_month(month, possible_birthdays):

    count=0

    for i in possible_birthdays:

        if month == i[0]:

            count+=1

        else:

            continue

    if count<=1:

        return True

    else:

        return False

def contains_unique_day(month, possible_birthdays):

    for i in possible_birthdays:

        if i[0]==month:

            if unique_day(i[1],possible_birthdays):

                return True

    return False


def test_birthday_functions():
    # Test data from global.py
    possible_birthdays = [
        ('May', '15'),
        ('May', '16'),
        ('May', '19'),
        ('June', '17'),
        ('June', '18'),
        ('July', '14'),
        ('July', '16'),
        ('August', '14'),
        ('August', '15'),
        ('August', '17')
    ]
    
    # Test unique_day function
    print("Testing unique_day function...")
    
    # Test case 1: Day that appears exactly once
    result = unique_day('19', possible_birthdays)
    assert result == True, f"Expected True for day '19', got {result}"
    
    # Test case 2: Day that appears exactly once
    result = unique_day('18', possible_birthdays)
    assert result == True, f"Expected True for day '18', got {result}"
    
    # Test case 3: Day that appears multiple times
    result = unique_day('15', possible_birthdays)
    assert result == False, f"Expected False for day '15', got {result}"
    
    # Test case 4: Day that appears multiple times
    result = unique_day('16', possible_birthdays)
    assert result == False, f"Expected False for day '16', got {result}"
    
    # Test case 5: Day that appears multiple times
    result = unique_day('14', possible_birthdays)
    assert result == False, f"Expected False for day '14', got {result}"
    
    # Test case 6: Day that doesn't exist
    result = unique_day('99', possible_birthdays)
    assert result == False, f"Expected False for day '99', got {result}"
    
    # Test unique_month function
    print("Testing unique_month function...")
    
    # Test case 7: Month that appears multiple times
    result = unique_month('May', possible_birthdays)
    assert result == False, f"Expected False for month 'May', got {result}"
    
    # Test case 8: Month that appears multiple times
    result = unique_month('June', possible_birthdays)
    assert result == False, f"Expected False for month 'June', got {result}"
    
    # Test case 9: Month that appears multiple times
    result = unique_month('July', possible_birthdays)
    assert result == False, f"Expected False for month 'July', got {result}"
    
    # Test case 10: Month that appears multiple times
    result = unique_month('August', possible_birthdays)
    assert result == False, f"Expected False for month 'August', got {result}"
    
    # Test case 11: Month that doesn't exist
    result = unique_month('September', possible_birthdays)
    assert result == False, f"Expected False for month 'September', got {result}"
    
    # Test contains_unique_day function
    print("Testing contains_unique_day function...")
    
    # Test case 12: May contains day '19' which is unique
    result = contains_unique_day('May', possible_birthdays)
    assert result == True, f"Expected True for month 'May', got {result}"
    
    # Test case 13: June contains day '18' which is unique
    result = contains_unique_day('June', possible_birthdays)
    assert result == True, f"Expected True for month 'June', got {result}"
    
    # Test case 14: July doesn't contain any unique days
    result = contains_unique_day('July', possible_birthdays)
    assert result == False, f"Expected False for month 'July', got {result}"
    
    # Test case 15: August doesn't contain any unique days
    result = contains_unique_day('August', possible_birthdays)
    assert result == False, f"Expected False for month 'August', got {result}"
    
    # Test case 16: Non-existent month
    result = contains_unique_day('September', possible_birthdays)
    assert result == False, f"Expected False for month 'September', got {result}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_birthday_functions()
