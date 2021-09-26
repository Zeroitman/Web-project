import json
import random
from russian_names import RussianNames
from project.models import *


def save_examples_of_full_name():
    # 0 - female, 1 - male
    try:
        for gender in range(2):
            full_name = RussianNames(count=1000, output_type='dict', gender=gender).get_batch()
            name_list, surname_list, patronymic_list = [], [], []
            for a in full_name:
                name_list.append(a.get('name'))
                patronymic_list.append(a.get('patronymic'))
                surname_list.append(a.get('surname'))
            full_name = {
                'names': name_list,
                'patronymic': patronymic_list,
                'surname': surname_list
            }
            gen = {0: 'female', 1: 'male'}
            with open('../example_of_full_name/examples_of_%s_names.json' % gen.get(gender), 'w') as outfile:
                json.dump(full_name, outfile)
    except Exception as err:
        print(err)


def generate_department():
    return random.randint(2, 25)


def generate_salary():
    salary = random.randint(25000, 120000) // 1000
    return salary * 1000


def generate_date():
    year = random.randint(2010, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return "%s-%s-%s" % (year, month, day)


def generate_position(department_id):
    department_name = Department.objects.get(id=department_id).name
    element = department_name.split()
    element.remove('Отдел')
    positions = ['Cпециалист', 'Ведущий специалист', 'Главный спецалист']
    return '%s отдела %s' % (random.choice(positions), " ".join(element))


def get_full_name(gender='male'):
    try:
        with open('../example_of_full_name/examples_of_%s_names.json' % gender, 'r', encoding='utf-8') as f:
            text = json.load(f)
        return text
    except Exception as err:
        print(err)


def generate_employes():
    try:
        for gender in ['male', 'female']:
            text = get_full_name(gender)
            for emp in range(25000):
                print(emp)
                department_id = generate_department()
                employee = Employee(name=random.choice(text.get('names')),
                                    surname=random.choice(text.get('surname')),
                                    patronymic=random.choice(text.get('patronymic')),
                                    position=generate_position(department_id),
                                    employment_date=generate_date(),
                                    salary=generate_salary(),
                                    department_id=department_id
                                    )
                employee.save()
    except Exception as err:
        print(err)
