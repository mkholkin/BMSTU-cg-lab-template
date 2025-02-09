# Обязательно в реализации
# - Цели НЕ менять
# - Зависимости и сценарии поменять на необходимые

# Рекомендуется проект выстраивать вокруг собственных сценариев сборки
# Рекомендуется в этом файле оставить только свои вызовы "make build",
# "cmake .", "msBuild proj1.sln ./out" и операции копирования

# Сценарий интерфейса специально не носит название "makefile" -
# Вы можете отсюда обращаться к своим сценариям


# Положить на проверку уже загруженный в репозиторий отчёт тестирования
#
# Пример содержимого:
#
# { 
#     "timestamp": "2024-07-14T19:46:32+03:00",
#     "coverage": 0.1,
#     "passed": 1,
#     "failed": 0
# }
#
# "timestamp" - дататаймштамп в формате UTC с указанием зоны dtst=$(date +"%Y-%m-%dT%H:%M:%S%:z")
# "coverage" - покрытие в процентах
# "passed" - число пройденных модульных тестов при последнем тестировании
# "failed" - число проваленных модульных тестов при последнем тестировании
#
# При невозможности/нежелании генерировать такой файл автоматически допускается ручное заполнение "на глаз" с одним тестом и минимальным покрытием

ready/stud-unit-test-report-prev.json: tests/stud-unit-test-report-prev.json
	mkdir -p ./ready
	cp tests/stud-unit-test-report.json ready/stud-unit-test-report-prev.json

# Положить на проверку программу из питоновских скриптов
ready/main-cli-debug.py: main-cli-debug.py src
	mkdir -p ./ready
	cp -r ./src ./ready
	cp main-cli-debug.py ready/main-cli-debug.py

# ИЛИ

# Очистка
.PHONY: clean
clean:
	$(RM) -r ./ready/*

# --

# Положить на проверку программу из питоновских скриптов
ready/main-gui.py: main-gui.py src
	mkdir -p ./ready
	cp -r ./src ./ready
	cp main-gui.py ready/main-gui.py
	
ready/app-gui-debug:

# Реализация по желанию - удалить цели, если нет реализации

# Сборка и запуск модульных тестов прямо на сервере
ready/stud-unit-test-report.json:
	python run_tests.py
	cp tests/stud-unit-test-report-prev.json stud-unit-test-report.json
