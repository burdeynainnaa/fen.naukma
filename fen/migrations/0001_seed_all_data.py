from django.db import migrations, models

def seed_data(apps, schema_editor):
    Department = apps.get_model('fen', 'Department')
    Program = apps.get_model('fen', 'Program')
    Teacher = apps.get_model('fen', 'Teacher')
    HomePageContent = apps.get_model('fen', 'HomePageContent')
    ExchangeProgram = apps.get_model('fen', 'ExchangeProgram')

    HomePageContent.objects.get_or_create(
        id=1,
        defaults={
            "title": "Факультет економічних наук (ФЕН) НаУКМА",
            "description": "Факультет економічних наук Національного університету «Києво-Могилянська академія» є одним із провідних центрів економічної та фінансової освіти в Україні, що готує конкурентоспроможних фахівців за міжнародними стандартами.",
            "contacts": "Адреса: вул. Волоська 8/5, 4 корпус НаУКМА, Київ\nEmail: fen@ukma.edu.ua\nТелефон: +380 (44) 425-60-20"
        }
    )

    dept_econ = Department.objects.create(name="Кафедра економіки", head="Баранник В. А.")
    dept_fin = Department.objects.create(name="Кафедра фінансів", head="Лук'яненко І. Г.")
    dept_market = Department.objects.create(name="Кафедра маркетингу та управління бізнесом", head="Резнікова Н. В.")

    Teacher.objects.create(name="Баранник В. А.", position="Доцент", degree="к.е.н.", department=dept_econ)
    Teacher.objects.create(name="Біла Ірина Сергіївна", position="Завідувач кафедри", degree="к.е.н., доцент", department=dept_econ)
    Teacher.objects.create(name="Бажал Юрій Миколайович", position="Професор", degree="д.е.н., професор", department=dept_econ)

    Teacher.objects.create(name="Лук'яненко І. Г.", position="Професор", degree="д.е.н.", department=dept_fin)
    Teacher.objects.create(name="Кужелєв Михайло Олександрович", position="Професор", degree="д.е.н., професор", department=dept_fin)

    Teacher.objects.create(name="Резнікова Н. В.", position="Професор", degree="д.е.н.", department=dept_market)
    Teacher.objects.create(name="Пічик Катерина Валеріївна", position="Завідувач кафедри", degree="к.е.н., доцент", department=dept_market)

    Program.objects.create(
        name="Економіка та міжнародні економічні відносини (економіка)",
        code="С1.01.",
        description="Докторська програма 'Економіка' побудована відповідно до сучасних європейських стандартів докторської освіти та орієнтується на так звані Зальцбурзькі принципи. Її основна ідея — розвиток знань через оригінальні дослідження та їхню практичну релевантність для економіки.",
        coordinator_name="Новікова Наталія Леонідівна",
        coordinator_contact="n.novikova@ukma.edu.ua",
        department=dept_econ,
        disciplines="Мікроекономіка, Макроекономіка, Економетрика, Теорія ігор, Фінансовий аналіз"
    )
    Program.objects.create(
        name="Фінанси, банківська справа, страхування та фондовий ринок",
        code="D2.",
        description="Бакалаврська програма з фінансів, банківської справи та страхування спрямована на підготовку фінансових аналітиків нового покоління з глибокою теоретичною та методологічною базою.",
        coordinator_name="Дяковський Дмитро Анатолійович",
        coordinator_contact="dmytro.dyakovsky@ukma.edu.ua",
        department=dept_fin,
        disciplines="Фінанси підприємств, Банківська система, Ризик-менеджмент, Інвестиційний аналіз"
    )
    Program.objects.create(
        name="Менеджмент",
        code="D3.",
        description="Бакалаврська програма з менеджменту формує фахівців, здатних ефективно вирішувати прикладні управлінські задачі, мислити інноваційно та працювати в динамічному середовищі.",
        coordinator_name="Боднар Ольга Василівна",
        coordinator_contact="o.bodnar@ukma.edu.ua",
        department=dept_market,
        disciplines="Основи менеджменту, Стратегічне управління, Управління персоналом, Організаційна поведінка"
    )
    Program.objects.create(
        name="Маркетинг",
        code="D5.",
        description="Програма формує фахівців із маркетингу, які поєднують аналітичне мислення, креативність і розуміння бізнесу.",
        coordinator_name="Гриджук Ірина Анатоліївна",
        coordinator_contact="iryna.grydzhuk@ukma.edu.ua",
        department=dept_market,
        disciplines="Маркетингові дослідження, Цифровий маркетинг, Поведінка споживачів, Бренд-менеджмент"
    )

    exchange_programs = [
        {"university": "Uniwersytet Warszawski", "country": "Польща", "languages": "польська, англійська", "slots": 5, "deadline": "2026-11-15", "description": "Один із провідних університетів Польщі з багатими академічними традиціями."},
        {"university": "KU Leuven", "country": "Бельгія", "languages": "English", "slots": 2, "deadline": "2026-12-01", "description": "Найстаріший католицький університет Європи та потужний науковий центр."},
        {"university": "Vilnius University", "country": "Литва", "languages": "англійська", "slots": 4, "deadline": "2026-10-20", "description": "Найвищий за рейтингом університет Литви з широким вибором програм англійською мовою."},
        {"university": "Uniwersytet Jagielloński", "country": "Польща", "languages": "Польська, Англійська", "slots": 3, "deadline": "2026-11-15", "description": "Найстаріший виш Польщі у Кракові з високими стандартами викладання."},
        {"university": "University of Tartu", "country": "Естонія", "languages": "англійська, естонська", "slots": 2, "deadline": "2027-01-10", "description": "Провідний класичний університет Естонії, відомий інноваціями та дослідницькою базою."},
        {"university": "Masaryk University", "country": "Чехія", "languages": "англійська", "slots": 1, "deadline": "2026-09-30", "description": "Другий за величиною університет Чехії з сучасним кампусом та європейським середовищем."},
    ]

    for p in exchange_programs:
        ExchangeProgram.objects.create(**p)

def unseed_data(apps, schema_editor):
    Department = apps.get_model('fen', 'Department')
    Program = apps.get_model('fen', 'Program')
    Teacher = apps.get_model('fen', 'Teacher')
    HomePageContent = apps.get_model('fen', 'HomePageContent')
    ExchangeProgram = apps.get_model('fen', 'ExchangeProgram')

    Department.objects.all().delete()
    Program.objects.all().delete()
    Teacher.objects.all().delete()
    HomePageContent.objects.all().delete()
    ExchangeProgram.objects.all().delete()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Назва кафедри')),
                ('head', models.CharField(max_length=100, verbose_name='Завідувач кафедри')),
            ],
            options={'verbose_name': 'Кафедра', 'verbose_name_plural': 'Кафедри'},
        ),
        migrations.CreateModel(
            name='ExchangeProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('university', models.CharField(max_length=200, verbose_name='Університет')),
                ('country', models.CharField(max_length=100, verbose_name='Країна')),
                ('languages', models.CharField(max_length=200, verbose_name='Мови навчання')),
                ('slots', models.IntegerField(verbose_name='Кількість місць')),
                ('deadline', models.DateField(verbose_name='Дедлайн подачі')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(default='Факультет економічних наук (ФЕН) НаУКМА', max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис факультету')),
                ('contacts', models.TextField(verbose_name='Контактна інформація')),
            ],
            options={'verbose_name': 'Контент головної сторінки', 'verbose_name_plural': 'Контент головної сторінки'},
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Назва спеціальності')),
                ('code', models.CharField(max_length=20, verbose_name='Код спеціальності')),
                ('description', models.TextField(verbose_name='Повний опис')),
                ('coordinator_name', models.CharField(max_length=100, verbose_name="Ім'я координатора набору")),
                ('coordinator_contact', models.CharField(max_length=100, verbose_name='Контакт координатора')),
                ('disciplines', models.TextField(verbose_name='Список дисциплін')),
                ('department', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='programs', to='fen.department', verbose_name='Випускова кафедра')),
            ],
            options={'verbose_name': 'Спеціальність', 'verbose_name_plural': 'Спеціальності'},
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я викладача")),
                ('position', models.CharField(max_length=100, verbose_name='Посада')),
                ('degree', models.CharField(blank=True, max_length=100, null=True, verbose_name='Науковий ступінь')),
                ('department', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='teachers', to='fen.department', verbose_name='Кафедра')),
            ],
            options={'verbose_name': 'Викладач', 'verbose_name_plural': 'Викладачі'},
        ),
        migrations.RunPython(seed_data, unseed_data),
    ]