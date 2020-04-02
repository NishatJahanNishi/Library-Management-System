from flask_sqlalchemy import get_debug_queries


class SQLAlchemyQueryLog:
    def __init__(self, app=None):
        self.app = app

        # init app if given
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        @app.after_request
        def sql_debug(response):
            queries = list(get_debug_queries())
            if not queries:
                return response
            query_str = ''
            total_duration = 0.0
            for q in queries:
                total_duration += q.duration
                try:
                    stmt = str(q.statement % q.parameters)
                except:
                    stmt = str(q.statement) + '\n' + str(q.parameters)
                stmt = stmt.replace('\n', '\n       ').replace(',', ',\n             ')
                query_str += f'Query: {stmt}\nDuration: {round(q.duration * 1000)}ms\n\n'

            print('=' * 80)
            print(f'SQL Queries - {len(queries)} Queries Executed in {round(total_duration * 1000, 2)}ms')
            print('')
            print(query_str.rstrip('\n'))
            print('=' * 36 + ' !!END!! ' + '=' * 36 + '\n\n')

            return response
