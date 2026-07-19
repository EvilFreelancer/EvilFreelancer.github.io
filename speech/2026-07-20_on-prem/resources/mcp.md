# MCP-серверы для кодинга

Подключать точечно: 5-7 серверов максимум, каждый должен отбивать свои токены, иначе tool bloat роняет качество. Работу с GitHub и GitLab удобнее вести через CLI (gh, glab), а не через MCP, поэтому их тут нет.

## Полезные серверы

- context7 - актуальная документация библиотек под нужную версию - https://github.com/upstash/context7
- serena - семантический граф кода и навигация по символам, тот самый codegraph - https://github.com/oraios/serena
- filesystem - файловые операции, часто уже встроено в агента - https://github.com/modelcontextprotocol/servers
- playwright - браузер для проверки UI и e2e - https://github.com/microsoft/playwright-mcp
- postgres - прямые запросы к схеме и данным - https://github.com/modelcontextprotocol/servers
- sequential-thinking - структурированное пошаговое рассуждение - https://github.com/modelcontextprotocol/servers
- fetch - загрузка веб-страниц и конвертация в markdown - https://github.com/modelcontextprotocol/servers

## Где искать ещё

- Эталонные серверы и реестр Model Context Protocol - https://github.com/modelcontextprotocol/servers
- Большая подборка Awesome MCP Servers - https://github.com/punkpeye/awesome-mcp-servers
