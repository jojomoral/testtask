import DB


def show_users():
    users_data = DB.get_users(region_city_names=True)
    html = """
<html>
<head>
  <meta charset="utf-8">

  <link rel="stylesheet" href="../static/style.css">
  <title>Нигматулин Руслан, тестовое задание</title>
</head>
<body>
<a href="/users/add/"><h4 class="text-center mb-4">Добавить пользователя</h4></a>
<a href="/users/downoload/xlsx/"><h4 class="text-center mb-4">Импорт xlsx</h4></a>
<a href="/users/export/xlsx/"><h4 class="text-center mb-4">Экспорт xlsx</h4></a>
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
<link rel="stylesheet" href="../../static/style.css">
</head>
<body>

<script>
    (() => {
  const dynamicSelect = (id1, id2) => {

    const sel1 = document.getElementById(id1);
    const sel2 = document.getElementById(id2);

    const clone = sel2.cloneNode(true);

    const clonedOptions = clone.getElementsByTagName("option");

    refreshDynamicSelectOptions(sel1, sel2, clonedOptions);

    sel1.addEventListener('change', () => {
      refreshDynamicSelectOptions(sel1, sel2, clonedOptions);
    });
  };

  const refreshDynamicSelectOptions = (sel1, sel2, clonedOptions) => {
    while (sel2.options.length) {
      sel2.remove(0);
    }
    const selectedOption = sel1.options[sel1.selectedIndex].value;
    for (let i = 0; i < clonedOptions.length; i++) {
      const option = clonedOptions[i];
      if (option.classList.contains('select') ||
        option.classList.contains(selectedOption)) {

        sel2.appendChild(option.cloneNode(true));
      }
    }

    const event = document.createEvent('HTMLEvents');
    event.initEvent('change', true, false);
    sel2.dispatchEvent(event);
  };

  document.addEventListener("DOMContentLoaded", () => {
    dynamicSelect("select-1", "select-2");
    dynamicSelect("select-2", "select-3");
  });
})();
</script>
<a href="../"><h4 class="text-center mb-4">Назад</h4></a>
    <form method = "POST" action="/users/">
        <input type="text" name="second_name" required placeholder="Фамилия">
        <input type="text" name="first_name" required placeholder="Имя">
        <input type="text" name="patronymic" placeholder="Отчество">
        <select name="region" id="select-1">
  <option value="">Регион...</option>"""
    for row in regions:
        html += f"<option value='{row[0]}'>{row[1]}</option>"

    html += """</select>
<select name="city" id="select-2">
  <option class="select" value="">Город...</option>
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

def export_xlsx():
   html = """
    <html>
<head>
<meta charset="utf-8">
<title>Добавить нового пользователя</title>
<link rel="stylesheet" href="../../../static/style.css">
</head>
<body>
     <form enctype="multipart/form-data" method = "POST" action="">
    <input type="file" name="file" required placeholder="файл">
    <input type="submit">
    </form>
     </body>
    </html>   
    """
   return html


