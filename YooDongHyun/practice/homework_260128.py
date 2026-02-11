def get_even_numbers(inlist):
    """
    리스트에서 짝수만 반환하는 함수
    """
    # 여기에 코드를 작성하세요.
    return [k for k in inlist if k % 2 == 0]

# 테스트
print(get_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

def is_palindrome(instr):
    """
    주어진 문자열이 회문인지 확인하는 함수
    """
    # 여기에 코드를 작성하세요.
    for i in range(0, len(instr) // 2):
        if instr[i] != instr[len(instr) - 1 - i]:
            return False
    return True

# 테스트
print(is_palindrome("tenet"))  # True
print(is_palindrome("소주만병만주소"))    # True
print(is_palindrome("hello"))    # False

def reverse_list(inlist):
    """
    리스트를 거꾸로 반환하는 함수
    """
    # 여기에 코드를 작성하세요.
    return inlist[::-1]

# 테스트
print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]

def count_vowels(instr):
    """
    문자열에서 모음의 개수를 세는 함수
    """
    # 여기에 코드를 작성하세요.
    cnt = 0
    for i in range(len(instr)):
        if instr[i] in 'aeiou':
            cnt += 1
    return cnt

# 테스트
print(count_vowels("hello world"))  # 3

def find_max(inlist):
    """
    리스트에서 최댓값을 반환하는 함수
    """
    # 여기에 코드를 작성하세요.
    return max(inlist)

# 테스트
print(find_max([1, 5, 2, 9, 3]))  # 9

def are_anagrams(str1, str2):
    """
    두 문자열이 애너그램인지 확인하는 함수
    """
    # 여기에 코드를 작성하세요.
    if len(str1) != len(str2):
        return False

    ln = len(str1)
    mask = [False] * ln
    for i in range(ln):
        for j in range(ln):
            if mask[j]:
                continue
            if str1[i] == str2[j]:
                mask[j] = True
                break

    res = True
    for i in range(ln):
        res = res and mask[i]
    return res


# 테스트
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False