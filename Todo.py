# Список узлов с атрибутами
nodes = [
    {
        "name": "Node 1",
        "ip_address": "192.168.1.1",
        "device_type": "Router",
        "status": "Active"
    },
    {
        "name": "Node 2",
        "ip_address": "192.168.1.2",
        "device_type": "Switch",
        "status": "Inactive"
    },
    {
        "name": "Node 3",
        "ip_address": "192.168.1.3",
        "device_type": "Firewall",
        "status": "Active"
    }
]

# HTML шаблон страницы
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To Do List для {node_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        input, select {{
            padding: 10px;
            margin: 10px 0;
            width: calc(100% - 22px);
        }}
        button {{
            padding: 10px 15px;
            cursor: pointer;
        }}
        .delete {{
            background-color: red;
            color: white;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <h1>To Do List для {node_name}</h1>
    <table>
        <thead>
            <tr>
                <th>Имя Узла</th>
                <th>IP-Адрес</th>
                <th>Тип Устройства</th>
                <th>Статус</th>
                <th>Задача</th>
                <th>Действия</th>
            </tr>
        </thead>
        <tbody id="todo-list">
            <!-- Список задач для узлов появляется здесь -->
        </tbody>
    </table>
    <input type="text" id="node-name" placeholder="Имя Узла" value="{node_name}" readonly>
    <input type="text" id="ip-address" placeholder="IP-Адрес" value="{ip_address}" readonly>
    <select id="device-type" disabled>
        <option value="Router" {router_selected}>Router</option>
        <option value="Switch" {switch_selected}>Switch</option>
        <option value="Firewall" {firewall_selected}>Firewall</option>
        <option value="Server" {server_selected}>Server</option>
    </select>
    <input type="text" id="status" placeholder="Статус" value="{status}" readonly>
    <input type="text" id="task" placeholder="Задача">
    <button onclick="addTask()">Добавить</button>

    <script>
        function addTask() {{
            var taskInput = document.getElementById('task');
            var taskText = taskInput.value;
            if (taskText === '') return;

            var tr = document.createElement('tr');
            tr.innerHTML = `<td>{node_name}</td><td>{ip_address}</td><td>{device_type}</td><td>{status}</td><td>${{taskText}}</td>`;

            var deleteButton = document.createElement('button');
            deleteButton.textContent = 'Удалить';
            deleteButton.className = 'delete';
            deleteButton.onclick = function() {{
                var tr = this.parentElement.parentElement;
                tr.parentElement.removeChild(tr);
            }};

            var td = document.createElement('td');
            td.appendChild(deleteButton);
            tr.appendChild(td);

            document.getElementById('todo-list').appendChild(tr);

            taskInput.value = '';
        }}
    </script>
</body>
</html>
"""

# Функция для генерации и сохранения HTML страницы
def generate_html_page(node):
    router_selected = "selected" if node["device_type"] == "Router" else ""
    switch_selected = "selected" if node["device_type"] == "Switch" else ""
    firewall_selected = "selected" if node["device_type"] == "Firewall" else ""
    server_selected = "selected" if node["device_type"] == "Server" else ""
    
    html_content = html_template.format(
        node_name=node["name"],
        ip_address=node["ip_address"],
        device_type=node["device_type"],
        status=node["status"],
        router_selected=router_selected,
        switch_selected=switch_selected,
        firewall_selected=firewall_selected,
        server_selected=server_selected
    )
    
    filename = f'todo_{node["name"].replace(" ", "_")}.html'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f'HTML страница для {node["name"]} успешно создана: {filename}')

# Генерация HTML страниц для всех узлов
for node in nodes:
    generate_html_page(node)
