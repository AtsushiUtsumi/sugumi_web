from injector import Injector, Module, inject

from sugumi_domain import ProjectInfoRepository
from sugumi_infrastructure import PostgresqlProjectInfoRepository, SqliteProjectInfoRepository

class SqliteDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=SqliteProjectInfoRepository)

class PostgresqlDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=PostgresqlProjectInfoRepository)

class ProjectInfoService:
    @inject
    def __init__(self, repository: ProjectInfoRepository) -> None:
        self.repository = repository
        self.repository.create_table()# ここで何がインジェクションされているか

injector = Injector([SqliteDiModule()])# 「Sqlite」使いたければこっち
# injector = Injector([PostgresqlDiModule()])# 「Postgresql」使いたければこっち
