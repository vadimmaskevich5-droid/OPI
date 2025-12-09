import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import defaultdict

def load_users_data():
    try:
        users_tree = ET.parse('lab6/users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': int(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text,
            'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
    return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse('lab6/workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
    return []

def get_stats(users, workouts):
    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(workout['calories'] for workout in workouts)
    total_time = sum(workout['duration'] for workout in workouts) / 60
    total_distance = sum(workout['distance'] for workout in workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("="*40)
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {round(total_time, 1)} часов")
    print(f"Пройдено дистанции: {total_distance} км")

def analyze_user_activity(users, workouts):
    user_stats = []
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        total_sessions = len(user_workouts)
        total_calories = sum(w['calories'] for w in user_workouts)
        total_time = sum(w['duration'] for w in user_workouts) / 60 

        user_stats.append({
            'name': user['name'],
            'fitness_level': user['fitness_level'],
            'sessions': total_sessions,
            'calories': total_calories,
            'time': round(total_time, 1)
        })

    top_users = sorted(user_stats, key=lambda u: (-u['sessions'], -u['calories']))[:3]

    print("\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, user in enumerate(top_users, 1):
        print(f"{i}. {user['name']} ({user['fitness_level']}):")
        print(f"   Тренировок: {user['sessions']}")
        print(f"   Калорий: {user['calories']}")
        print(f"   Время: {user['time']} часов")

def analyze_workout_types(workouts):
    type_stats = defaultdict(list)

    for workout in workouts:
        type_stats[workout['type']].append(workout)

    total_workouts = len(workouts)

    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, group in sorted(type_stats.items(), key=lambda x: len(x[1]), reverse=True):
        count = len(group)
        percent = round(count / total_workouts * 100, 1)
        avg_duration = round(sum(w['duration'] for w in group) / count)
        avg_calories = round(sum(w['calories'] for w in group) / count)

        print(f"{workout_type}: {count} тренировок ({percent}%)")
        print(f"Средняя длительность: {avg_duration} мин")
        print(f"Средние калории: {avg_calories} ккал\n")

def find_user_workouts(users, workouts, user_name):
    user_ids = [user['user_id'] for user in users if user['name'].lower() == user_name.lower()]
    if not user_ids:
        print(f"Пользователь с именем '{user_name}' не найден.")
        return []

    user_id = user_ids[0]
    user_workouts = [w for w in workouts if w['user_id'] == user_id]

    return user_workouts

def analyze_user(user, workouts):
    user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
    total_sessions = len(user_workouts)
    total_calories = sum(w['calories'] for w in user_workouts)
    total_time = round(sum(w['duration'] for w in user_workouts) / 60, 1) 
    total_distance = round(sum(w['distance'] for w in user_workouts), 1)
    avg_calories = round(total_calories / total_sessions) if total_sessions else 0

    type_count = {}
    for w in user_workouts:
        type_count[w['type']] = type_count.get(w['type'], 0) + 1
    favorite_type = max(type_count, key=type_count.get) if type_count else "—"

    print(f"\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 40)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {total_sessions}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time} часов")
    print(f"Пройдено дистанции: {total_distance} км")
    print(f"Средние калории за тренировку: {avg_calories}")
    print(f"Любимый тип тренировки: {favorite_type}")

def plot_workout_type_distribution(workouts):
    type_counts = {}
    for workout in workouts:
        wtype = workout['type']
        type_counts[wtype] = type_counts.get(wtype, 0) + 1

    labels = list(type_counts.keys())
    sizes = list(type_counts.values())

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Распределение типов тренировок")
    plt.axis('equal')  
    plt.show()

def plot_user_activity_bar_chart(users, workouts):
    user_counts = {}
    for user in users:
        count = sum(1 for w in workouts if w['user_id'] == user['user_id'])
        user_counts[user['name']] = count

    names = list(user_counts.keys())
    counts = list(user_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(names, counts)
    plt.title("Активность пользователей (количество тренировок)", fontsize=14)
    plt.xlabel("Пользователи", fontsize=12)
    plt.ylabel("Количество тренировок", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_efficiency_by_type(workouts):
    type_stats = {}

    for w in workouts:
        wtype = w['type']
        if wtype not in type_stats:
            type_stats[wtype] = {'total_calories': 0, 'total_duration': 0}
        type_stats[wtype]['total_calories'] += w['calories']
        type_stats[wtype]['total_duration'] += w['duration']

    types = []
    efficiency = []

    for wtype, stats in type_stats.items():
        if stats['total_duration'] > 0:
            cal_per_min = stats['total_calories'] / stats['total_duration']
            types.append(wtype)
            efficiency.append(round(cal_per_min, 2))

    plt.figure(figsize=(10, 6))
    plt.bar(types, efficiency, color='purple')
    plt.title("Эффективность тренировок (калории/минуту)", fontsize=14)
    plt.xlabel("Тип тренировки", fontsize=12)
    plt.ylabel("Калории/минуту", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_calories_by_user(users, workouts):
    user_stats = []
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        total_calories = sum(w['calories'] for w in user_workouts)
        user_stats.append({
            'name': user['name'],
            'calories': total_calories,
            'level': user['fitness_level']
        })

    user_stats.sort(key=lambda x: x['calories'], reverse=True)

    level_colors = {
        'продвинутый': 'red',
        'средний': 'orange',
        'начинающий': 'green'
    }

    names = [u['name'] for u in user_stats]
    calories = [u['calories'] for u in user_stats]
    colors = [level_colors.get(u['level'], 'green') for u in user_stats]

    plt.figure(figsize=(10, 6))
    plt.bar(names, calories, color=colors)
    plt.title("Сравнение пользователей по общим затраченным калориям", fontsize=14)
    plt.xlabel("Пользователи", fontsize=12)
    plt.ylabel("Калории", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

user_name = "Григорий"
user = next((u for u in load_users_data() if u['name'].lower() == user_name.lower()), None)

get_stats(load_users_data(), load_workouts_data())
analyze_user_activity(load_users_data(), load_workouts_data())
analyze_workout_types(load_workouts_data())
find_user_workouts(load_users_data(), load_workouts_data(), user_name)
analyze_user(user, load_workouts_data())
plot_workout_type_distribution(load_workouts_data())
plot_user_activity_bar_chart(load_users_data(), load_workouts_data())
plot_efficiency_by_type(load_workouts_data())
plot_calories_by_user(load_users_data(), load_workouts_data())

