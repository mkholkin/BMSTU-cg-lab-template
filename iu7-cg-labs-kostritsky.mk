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

ready/stud-unit-test-report-prev.json: tests/results/stud-unit-test-report.json
	mkdir -p ./ready
	cp tests/results/stud-unit-test-report.json ready/stud-unit-test-report-prev.json

# Положить на проверку программу из питоновских скриптов
ready/main-cli.py: main-cli.py src
	mkdir -p ./ready
	cp -r ./src ./ready
	cp main-cli.py ready/main-cli.py

# ИЛИ

# Очистка
.PHONY: clean func_testing gui_testing
clean:
	$(RM) ready/main-gui.py
	$(RM) ready/main-cli.py
	$(RM) -r ready/src

# --

gui-testing:
	exit 66

func-testing:
	mkdir -p ./ready/pics
	QT_QPA_PLATFORM=offscreen PYTHONPATH="$PYTHONPATH:." python func_tests/run_tests.py

# Положить на проверку программу из питоновских скриптов
ready/main-gui.py: main-gui.py src
	mkdir -p ./ready
	./scripts/generate_forms.sh
	cp -r ./src ./ready
	cp main-gui.py ready/main-gui.py


# Реализация по желанию - удалить цели, если нет реализации

# Сборка и запуск модульных тестов прямо на сервере
ready/stud-unit-test-report.json:
	python -m pytest tests/
	cp tests/results/stud-unit-test-report.json ready/stud-unit-test-report.json
