from application.db.people import People
from application.salary import Salary
from datetime import datetime
import emoji


if __name__ == '__main__':
    print(datetime.today().strftime('%d-%m-%Y'))
    employe1 = People("Ivanov")
    salary1 = Salary(50000, 200)

    employe1.get_employees()
    salary1.calculate_salary()

result = emoji.emojize('Директор получил зарплату: :smiling_face_with_heart-eyes:')
print(result)
