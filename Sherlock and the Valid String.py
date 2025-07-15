def isValid(message):
    letters = []
    Remove = True
    
    for char in message:
        letters.append(char)
        
    current_max = letters.count(letters[0])
    
    for letter in letters:
        if letters.count(letter) < current_max:
            current_max = letters.count(letter)
    
    for letter in letters:
        if not (letters.count(letter) == current_max or letters.count(letter) == current_max + 1):
            return "No"
        else:
            if letters.count(letter) == current_max + 1:
                if Remove or removedLetter == letter:
                    Remove = False
                    removedLetter = letter
                else:
                    return "No"
            
    return "Yes"

print(isValid("aabbccddeefffgg"))