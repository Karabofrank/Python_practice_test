def compute_standard_deviation(numbers):
    """Compute the standard deviation of a list of numbers"""
    sum = 0
    added = 0
    deviations = []
    squared = []
    
    if numbers == []:
        return None
    
    #Find the mean
    for num in numbers:
        sum = sum + num
    mean = sum / len(numbers)
    
    #Subtract the mean from each number (Deviations)
    for i in numbers:
        devs = i - mean
        deviations.append(devs)

    #Square each deviation
    for dvs in deviations:
        squared_deviations = dvs**2
        squared.append(squared_deviations)
    
    #Add the squared deviations, divide the sum by the length of numbers and then take the square root
    for _ in squared:
        added = added + _
        added_devs = added / len(numbers)
        sums = (added_devs)**0.5
    return sums


def find_second_largest(numbers):
    """Find the second largest number in a list"""
    list1 = []
    for i in numbers:
        if i not in list1:
            list1.append(i)

    list1 = sorted(list1)
    if len(list1) <= 1:
        return None
    
    return list1[-2]

    
def character_frequency_per_word(sentence):
    """Return a dictionary of character frequencies for each word in a sentence"""
    a = {}
    b = {}
    sentence = sentence.split(" ")
    for word in sentence:
        b[word] = {}
        for i in word:
            if i in b[word]:
                b[word][i] += 1
            else:
                b[word][i] = 1
    return b

def check_palindrome(numbers):
    """Check if a list of numbers is a palindrome"""
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers) - 1 - i]:
            return False
    return True

def longest_word_in_sentence(sentence):
    """Return the longest word in a sentence"""
    sentence = sentence.split(" ")
    a = []
    for word in sentence:
        a.append(len(word))
    return sentence[a.index(max(a))]
    
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list"""
    return sorted(list1 + list2)    
    
def find_intersection(list1, list2):
    """Find the intersection (common elements) of two lists"""
    a = []
    for i in list1:
        if i in list2:
            a.append(i)
    return a

def nth_fibonacci(n):
    """Calculate the nth Fibonacci number using both recursion and iteration"""
    
def reverse_words_in_sentence(sentence):
    """Reverse the words in a sentence while maintaining word order"""
    sentence = sentence.split(" ")
    a = []
    for i in range(len(sentence) - 1, -1, -1):
        a.append(sentence[i])
    return " ".join(a)
def unique_characters_in_string(s):
    """Return all unique characters in a string"""
    a = []
    for i in s:
        a.append(i)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return "".join(sorted(b))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))