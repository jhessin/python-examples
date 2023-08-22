courses = {
    'js': 'JavaScript 101',
    'python': ('Python 101', 'Python 201'),
    'html': 'HTML 101',
}

if courses.get('css'):
    print('You are enrolled in CSS 101')
else:
    print('You are NOT enrolled in CSS 101')
