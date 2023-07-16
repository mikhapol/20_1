from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Андрей', 'last_name': 'Самойлюк'},
            {'first_name': 'Александр', 'last_name': 'Зазноба'},
            {'first_name': 'Владимир', 'last_name': 'Высоцкий'},
            {'first_name': 'Дьякон', 'last_name': 'Феофан'},
            {'first_name': 'Петр', 'last_name': 'Василькин'},
            {'first_name': 'Дмитрий', 'last_name': 'Медведьев'},
            {'first_name': 'Савелий', 'last_name': 'Картонкин'},
            {'first_name': 'Тимур', 'last_name': 'Измайлов'},
            {'first_name': 'Бирис', 'last_name': 'Комаров'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        # print(students_for_create)

        Student.objects.bulk_create(students_for_create)
