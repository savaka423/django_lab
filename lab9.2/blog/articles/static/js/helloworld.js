const groupmates = [
    {
        "name": "Климай Полина",
        "group": "БСТ-2253",
        "age": 23,
        "marks": [2,3,4,4]
    },
    {
        "name": "Кондаков Артем",
        "group": "БСТ-2254",
        "age": 23,
        "marks": [2,5,4,5]
    },
    {
        "name": "Коновалов Сергей",
        "group": "БСТ-2255",
        "age": 28,
        "marks": [5,5,4,5]
    },
    {
        "name": "Кузнецов Вадим",
        "group": "БСТ-2253",
        "age": 28,
        "marks": [2,3,2,3]
    }
];

const rpad = function (str, length) {
// js не поддерживает добавление нужного количества символов
// справа от строки, то есть аналога ljust из языка Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};
const printStudents = function (students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
// был выведен заголовок таблицы
    for (let i = 0; i <= students.length - 1; i++) {
// в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates);

function filterStudent(students, groupStudent) {
    const result = []; // сюда будем добавлять студентов нужной группы

    for (let i = 0; i < students.length; i++) {
        if (students[i].group === groupStudent) {
            result.push(students[i]);
        }
    }

    return result;
}

const students2253 = filterStudent(groupmates, "БСТ-2253");
console.log("Студенты группы БСТ-2253:");
console.log(students2253);
