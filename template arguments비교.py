# Positional Arguments
def mysum(x, y):
    return x + y

mysum(1, 2)


#keyword arguments
def musum(x, y, z=0)
    return x + y + z

mysum(1, 2, z=10)


장고 템플릿 =>  소괄호랑 콤마 안씀.

class Person(object):
    def say_hello(self):
        print('hello')

person = Person()
people = {'Tom':10 , 'Steve':20}
names = ['Tom', 'Steve']



#python code
person.say_hello()
people['Tom']
names[0]
athelete_list = []

if athelete_list:
    for athelete in athelete_list:
        print(athelete.name)
else:
    print("empty")


#django.template ENGINE
{{ person.say_hello }}
{{ people.Tom }}
{{ names.0 }}
{% if athelete_list %}
    {% for athelete in athelete_list %}
        {{ athelete.name }}
    {% endfor %}
{% else %}
    empty
{% endif %}



#for tag / 가독성높음(empty를 지원하기때문에)
{% for athelete in athelete_list %}
    {{ athelete.name }}
{% empty %}
    empty
{% endfor %}
