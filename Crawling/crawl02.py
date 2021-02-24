from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>Test HTML</title>
    </head>
    <body>
        <ul>
            <li>Java</li>
            <li>Oracle</li>
        </ul>
        <ol>
            <li>Python</li>
            <li>Hello world</li>
        </ol>
    </body>
</html>

'''

soup = BeautifulSoup(html, 'html.parser')
result = soup.select('li')
result = soup.select_one('li') # 가장 첫 번째꺼 하나만 찾음.
result = soup.select('ul>li') # ul 밑의 li들만 찾음
print(result)

