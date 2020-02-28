django-unique-together-bug
==========================

```
$ python3.6 -m venv venv
$ source venv/bin/activate
$ pip install django  # or even master at time of writing
$ python manage.py migrate
$ python manage.py sqlmigrate testapp 0001_squashed_0002
Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/.../django/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/.../django/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/.../django/django/core/management/base.py", line 328, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/.../django/django/core/management/commands/sqlmigrate.py", line 30, in execute
    return super().execute(*args, **options)
  File "/.../django/django/core/management/base.py", line 369, in execute
    output = self.handle(*args, **options)
  File "/.../django/django/core/management/commands/sqlmigrate.py", line 65, in handle
    sql_statements = executor.collect_sql(plan)
  File "/.../django/django/db/migrations/executor.py", line 225, in collect_sql
    state = migration.apply(state, schema_editor, collect_sql=True)
  File "/.../django/django/db/migrations/migration.py", line 124, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/.../django/django/db/migrations/operations/models.py", line 525, in database_forwards
    getattr(new_model._meta, self.option_name, set()),
  File "/.../django/django/db/backends/base/schema.py", line 380, in alter_unique_together
    self._delete_composed_index(model, fields, {'unique': True}, self.sql_delete_unique)
  File "/.../django/django/db/backends/base/schema.py", line 414, in _delete_composed_index
    ", ".join(columns),
ValueError: Found wrong number (0) of constraints for testapp_book(title)
```

Also triggers on `migrate` with PostgreSQL.

Edit `settings.py` to switch from postgresql to sqlite3.

Then:

```
$ pip install django psycopg2-binary
$ psql postgres <<< 'create database testproj'
$ python manage.py migrate
Operations to perform:
  Apply all migrations: testapp
Running migrations:
  Applying testapp.0001_squashed_0002_add_author...Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File ".../django/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File ".../django/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File ".../django/django/core/management/base.py", line 328, in run_from_argv
    self.execute(*args, **cmd_options)
  File ".../django/django/core/management/base.py", line 369, in execute
    output = self.handle(*args, **options)
  File ".../django/django/core/management/base.py", line 83, in wrapped
    res = handle_func(*args, **kwargs)
  File ".../django/django/core/management/commands/migrate.py", line 234, in handle
    fake_initial=fake_initial,
  File ".../django/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File ".../django/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File ".../django/django/db/migrations/executor.py", line 245, in apply_migration
    state = migration.apply(state, schema_editor)
  File ".../django/django/db/migrations/migration.py", line 124, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File ".../django/django/db/migrations/operations/models.py", line 525, in database_forwards
    getattr(new_model._meta, self.option_name, set()),
  File ".../django/django/db/backends/base/schema.py", line 380, in alter_unique_together
    self._delete_composed_index(model, fields, {'unique': True}, self.sql_delete_unique)
  File ".../django/django/db/backends/base/schema.py", line 414, in _delete_composed_index
    ", ".join(columns),
ValueError: Found wrong number (0) of constraints for testapp_book(title)
```
