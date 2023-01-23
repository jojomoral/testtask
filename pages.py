import DB


def show_users():
    users_data = DB.get_users(region_city_names=True)
    html = """
<html>
<head>
  <meta charset="utf-8">

  
  <title>Нигматулин Руслан, тестовое задание</title>
</head>
<body>
<table>
<h1>users</h1>
<thead>
    <tr>
      <th>id</th>
      <th>Фамилия</th>
      <th>Имя</th>
      <th>Отчество</th>
      <th>Регион</th>
      <th>Город</th>
      <th>Телефон</th>
      <th>email</th>
    </tr>
</thead>
<tbody>
"""

    for row in users_data:
        html += '<tr>'
        for value in row:
            html += f'<td >{value}</td>'
        html += '</tr>'
    html += """
    </tbody>
    </table>
    </body>
    </html>
    """

    return html


def add_user():
    regions = DB.get_regions()
    cities = DB.get_cities()
    html = """
<html>
<head>
<meta charset="utf-8">
<title>Добавить нового пользователя</title>
</head>
<body>

<script>
    (() => {
  const dynamicSelect = (id1, id2) => {
    // Определение переменных, ссылающихся на списки
    const sel1 = document.getElementById(id1);
    const sel2 = document.getElementById(id2);
    // Клонирование динамического списка
    const clone = sel2.cloneNode(true);
    // Определение переменных для клонированных элементов списка
    const clonedOptions = clone.getElementsByTagName("option");
    // Вызов функции собирающей вызываемый список
    refreshDynamicSelectOptions(sel1, sel2, clonedOptions);
    // При изменении выбранного элемента в первом списке: // вызов функции пересобирающей вызываемый список
    sel1.addEventListener('change', () => {
      refreshDynamicSelectOptions(sel1, sel2, clonedOptions);
    });
  };

  // Функция для сборки динамического списка
  const refreshDynamicSelectOptions = (sel1, sel2, clonedOptions) => {
    // Удаление всех элементов динамического списка
    while (sel2.options.length) {
      sel2.remove(0);
    }
    const selectedOption = sel1.options[sel1.selectedIndex].value;
    // Перебор клонированных элементов списка
    for (let i = 0; i < clonedOptions.length; i++) {
      const option = clonedOptions[i];
      // Если название класса клонированного option эквивалентно "select"
      // либо эквивалентно значению option первого списка
      if (option.classList.contains('select') ||
        option.classList.contains(selectedOption)) {
        // его нужно клонировать в динамически создаваемый список
        sel2.appendChild(option.cloneNode(true));
      }
    }
    // Отправляем событие change выбранного select
    const event = document.createEvent('HTMLEvents');
    event.initEvent('change', true, false);
    sel2.dispatchEvent(event);
  };

  // Вызов скрипта при загрузке страницы
  document.addEventListener("DOMContentLoaded", () => {
    dynamicSelect("select-1", "select-2");
    dynamicSelect("select-2", "select-3");
  });
})();
</script>

    <form method = "POST" action="/users/">
        <input type="text" name="second_name" required placeholder="Фамилия">
        <input type="text" name="first_name" required placeholder="Имя">
        <input type="text" name="patronymic" placeholder="Отчество">
        <select name="region" id="select-1">
  <option value="select">Регион...</option>"""
    for row in regions:
        html += f"<option value='{row[0]}'>{row[1]}</option>"

    html += """</select>
<select name="city" id="select-2">
  <option class="select" value="select">Город...</option>
"""
    for row in cities:
        html += f"<option class='{row[1]}' value='{row[0]}'>{row[2]}</option>"

    html += """
    </select>
    <input type="tel" name="phone" placeholder="+7 999 999 99 99"  pattern="\+7\s?9[0-9]{2}\s?\d{3} \d{2} \d{2}">
    <input type="email" name="email" placeholder="email">
        <input type="submit">
    </form>
</body>
</html>    
"""
    return html

