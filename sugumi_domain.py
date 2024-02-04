# このモジュールはsugumiの中ではドメイン層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# 基本値オブジェクトとエンティティ
# あと、リポジトリで実装するインターフェースもここ

# conding: utf-8
from abc import ABCMeta, abstractmethod

class TableInfo:
    def __init__(self) -> None:
        pass
# 本日の目標はこれをDBに保存すること
class ProjectInfo:
    def __init__(self, id) -> None:
        self.id = id
        self.project_name = id
        self.output_path = id
        self.group_id = id
        self.framework = id
        self.language = id
        pass

class ProjectInfoRepository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, entity: ProjectInfo):
        return
    @abstractmethod
    def updete(self, entity: ProjectInfo):
        return
    @abstractmethod
    def delete(self, id: int):
        return
    @abstractmethod
    def find(self, id: int) -> ProjectInfo:
        return
    @abstractmethod
    def find_all(self) -> [ProjectInfo]:
        return