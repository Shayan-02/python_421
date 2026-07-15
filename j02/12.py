def strToInt(a: list):
    """
    Inputs a list and returns each index in int.
    
    Args:
        a (list): لیست ورودی متشکل از چند رشته
    
    Returns:
        b (list) : لیستی از عددی شده مقادیر ورودی
    """
    b = []
    for i in a:
        b.append(int(i))
    return b

# برنامه اصلی

a = input().split()
print(strToInt(a))