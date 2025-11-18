def shorten_text(text):
    result = text
    
    while '(' in result and ')' in result:
        start = result.find('(')
        end = result.find(')')
        if end > start:
            result = result[:start] + result[end+1:]
    
    return result

# Тестирование
test_text = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())."
print(f"Исходный: {test_text}")
print(f"Укороченный: {shorten_text(test_text)}")
