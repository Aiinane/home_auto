#ptint ("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# неправильно: 

# assert self.catalog_link.text  == "Каталог", \
#     f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'" 
# Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст на странице может измениться, и вы получите неактуальный текст об ошибке. Результат выполнения такого теста сложно анализировать: 

# "Wrong language, got 'Каталог' instead of 'Каталог'"
# правильно: 

# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"
# 
# assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
# 
# assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
# 
# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')  