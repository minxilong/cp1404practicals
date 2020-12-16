code_to_color = {'antiquewhite': '#faebd7', 'coral': '#ff7f50', 'cornflowerblue': '#6495ed', 'darkkhaki': '#bdb76b',
              'gainsboro': '#dcdcdc', 'lavender': '#e6e6fa', 'light': '#eedd82', 'lightblue': '#add8e6',
              'mintcream': '#f5fffa', 'pale': '#db7093'}
code = input('Enter color name: ').lower()
while code != '':
    if code in code_to_color:
        print(code_to_color[code])
    else:
        print('Invalid color name')
    code = input('Enter color name: ').lower()