# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач

from datetime import datetime
import pandas as pd


class Task:
    _nextId = 1
    all_tasks = []

    def __init__(self, code, description, duedate, status):
        self.id = Task._nextId
        self.code = code
        self.description = description
        self.duedate = duedate
        self.status = status
        Task._nextId += 1
        Task.all_tasks.append(self)

    # Метод класса для получения всех экземпляров
    @classmethod
    def get_all_tasks(cls):
        return cls.all_tasks

    # Метод класса для фильтрации объектов по заданным критериям
    @classmethod
    def filter_tasks(cls, **criteria):
        filtered_tasks = []
        for every_task in cls.all_tasks:
            if all(getattr(every_task, attr) == value for attr, value in criteria.items()):
                filtered_tasks.append(every_task)
        return filtered_tasks

    def info(self):
        print(f"идентификатор  = {self.id}")
        print(f"код = {self.code}")
        print(f"описание = {self.description}")
        print(f"дата выполнения - {self.duedate}")
        print(f"статус - {self.status}")

    def markcompleate(self):
        self.status = "Выполнено"
        self.duedate = datetime.now()


# пример использования

# создаем задачи
task1 = Task("TASK001", "1-я задача", datetime.strptime("2025-04-08", "%Y-%m-%d"), "Новая")
task2 = Task("TASK002", "2-я задача", datetime.strptime("2025-04-15", "%Y-%m-%d"), "Новая")
task3 = Task("TASK003", "3-я задача", datetime.strptime("2025-04-22", "%Y-%m-%d"), "Новая")
task4 = Task("TASK004", "4-я задача", datetime.strptime("2025-04-29", "%Y-%m-%d"), "Новая")
task5 = Task("TASK005", "5-я задача", datetime.strptime("2025-05-06", "%Y-%m-%d"), "Новая")
task6 = Task("TASK006", "6-я задача", datetime.strptime("2025-05-13", "%Y-%m-%d"), "Новая")

# отмечаем несколько как выполенные
task1.markcompleate()
task3.markcompleate()
task5.markcompleate()

# Вывод всех созданных задач
print("Все задачи:")
all_tasks = Task.get_all_tasks()
for task in all_tasks:
    print(
        f'id: {task.id}, code: {task.code}, description: {task.description}, '
        f'duedate: {datetime.strftime(task.duedate, "%d-%m-%Y")}, status: {task.status}')

# Вывод невыполненных задач
print("Невыполненные задачи:")
uncompleted_tasks = Task.filter_tasks(status="Новая")
for task in uncompleted_tasks:
    print(
        f'id: {task.id}, code: {task.code}, description: {task.description}, '
        f'duedate: {datetime.strftime(task.duedate, "%d-%m-%Y")}, status: {task.status}')

# Вывод невыполненных задач
print("Выполненные задачи:")
completed_tasks = Task.filter_tasks(status="Выполнено")
for task in completed_tasks:
    print(
        f'id: {task.id}, code: {task.code}, description: {task.description}, '
        f'duedate: {datetime.strftime(task.duedate, "%d-%m-%Y")}, status: {task.status}')

# С использованием date frame
# Преобразование списка объектов в DataFrame
df = pd.DataFrame([task.__dict__ for task in Task.all_tasks])

# Фильтрация DataFrame для вывода только не выполненных задач
uncompleated_df = df[df['status'] != "Выполнено"]
# Вывод не выполненных задач
print("Не выполненные задачи:")
print(uncompleated_df)

# Фильтрация DataFrame для вывода только выполненных задач
compleated_df = df[df['status'] == "Выполнено"]
# Вывод выполненных задач

print("Выполненные задачи:")
print(compleated_df)
