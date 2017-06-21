import os
import unittest

from july3.contrib.postgres import PostgresUser, PostgresDatabase, PostgresConnection
from july3.util import run


class TestPostgresRule(unittest.TestCase):

    def tearDown(self):
        run('dropdb j3db')
        run('psql postgres -c "DROP USER j3test"')

    def test_postgres_user_and_db(self):

        postgres_user = PostgresUser('j3test', 'j3pass')
        postgres_db = PostgresDatabase('j3db', 'j3test', 'j3pass', dependencies=[postgres_user])

        postgres_db.make()

        self.assertEqual('1', run(r'psql -U j3test j3db -t -c "select 1"', capture=True).stdout.strip())


    def test_postgres_connection(self):

        postgres = PostgresConnection('j3db', 'j3test', 'j3pass')

        postgres.make()

        run(r'psql -U j3test j3db -t -c "select 1"')
        self.assertEqual('1', run(r'psql -U j3test j3db -t -c "select 1"', capture=True).stdout.strip())

