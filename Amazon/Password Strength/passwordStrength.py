# Solution - 1
def passwordStrength1(password):
    containsVowel = False
    containsConstant = False
    vowels = 'aeiou'
    count = 0
    for char in password:
        if char in vowels:
            containsVowel = True
        else:
            containsConstant = True
        if containsVowel and containsConstant:
            count += 1
            containsVowel, containsConstant = False, False
    return count 

# Solution - 2 | Detailed
# Time - O(n) | Space - O(n)
# [char, hasVowel, hasConst]
def passwordStrength2(password):
    strength = []
    vowels = 'aeiou'
    for char in password:
        if len(strength) == 0:
            if char in vowels:
                strength.append([char, True, False])
            else:
                strength.append([char, False, True])
        elif strength[-1][1] is True and strength[-1][2] is True:
            if char in vowels:
                strength.append([char, True, False])
            else:
                strength.append([char, False, True])
        elif strength[-1][1] is False and strength[-1][2] is True:
            if char in vowels:
                strength[-1][0] += char
                strength[-1][1] = True
            else:
                strength[-1][0] += char
        elif strength[-1][1] is True and strength[-1][2] is False:
            if char in vowels:
                strength[-1][0] += char
            else:
                strength[-1][0] += char
                strength[-1][2] = True

    if strength[-1][1] is False or strength[-1][2] is False:
        return len(strength) - 1
    else:
        return len(strength)

testCaseOne = 'hackerrank'        # Expected o/p - 3
testCaseTwo = 'thisisbeautiful'   # Expected o/p - 6
testCaseThree = 'aeiou'           # Expected o/p - 0
testCaseFour = 'rhythm'           # Expected o/p - 0
testCaseFive = 'abcdfg'           # Expected o/p - 1
testCaseSix = 'zyxwvuu'           # Expected o/p - 1


print(passwordStrength1(testCaseOne)) 
print(passwordStrength1(testCaseTwo))
print(passwordStrength1(testCaseThree))
print(passwordStrength1(testCaseFour))
print(passwordStrength1(testCaseFive))
print(passwordStrength1(testCaseSix))
print()
print(passwordStrength2(testCaseOne)) 
print(passwordStrength2(testCaseTwo))
print(passwordStrength2(testCaseThree))
print(passwordStrength2(testCaseFour))
print(passwordStrength2(testCaseFive))
print(passwordStrength2(testCaseSix))
