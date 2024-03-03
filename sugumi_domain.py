# このモジュールはsugumiの中ではドメイン層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# 基本値オブジェクトとエンティティ
# あと、リポジトリで実装するインターフェースもここ

# conding: utf-8
from abc import ABCMeta, abstractmethod
class ProjectInfo:
    def __init__(self, id) -> None:# リモートリポジトリ
        self.id = id
        self.project_name = 'プロジェクト名'
        self.output_path = ''
        self.group_id = ''# Java特有だがここでいいのか
        self.framework = 'フレームワーク'
        self.language = ''
        pass

class ProjectInfoRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_table(self):
        return
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
    def find_all(self) -> list[ProjectInfo]:
        return
class TableInfo:
    def __init__(self, project_id, table_name) -> None:# リモートリポジトリ
        self.project_id = project_id
        self.table_name = table_name
        self.columns_info = ''
        pass

class TableInfoRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_table(self):
        return
    @abstractmethod
    def insert(self, entity: TableInfo):
        return
    @abstractmethod
    def updete(self, entity: TableInfo):
        return
    @abstractmethod
    def delete(self, table_name):
        return
    @abstractmethod
    def find(self, table_name: str) -> TableInfo:
        return
    @abstractmethod
    def find_all(self) -> list[TableInfo]:
        return
    @abstractmethod
    def delete_by_project_id(self, project_id: str) -> list[TableInfo]:
        return
    @abstractmethod
    def find_by_project_id(self, project_id: str) -> list[TableInfo]:
        return


class ClassInfo:
    def __init__(self, id) -> None:
        self.id = id
        self.class_name = id
        self.output_path = id
        self.group_id = id# Java特有だがここでいいのか
        self.framework = id
        self.language = id
        pass

class ClassInfoRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_table(self):
        return
    @abstractmethod
    def insert(self, entity: ClassInfo):
        return
    @abstractmethod
    def updete(self, entity: ClassInfo):
        return
    @abstractmethod
    def delete(self, id: int):
        return
    @abstractmethod
    def find(self, id: int) -> ClassInfo:
        return
    @abstractmethod
    def find_all(self) -> list[ClassInfo]:
        return
    



class PresentationInfo:
    def __init__(self, screen_name: str, url: str, class_name: str, action: str) -> None:
        self.screen_name: str = screen_name
        self.url: str = url
        self.class_name: str = class_name
        self.action: str = action

class PresentationInfoRepository(metaclass=ABCMeta):# 抽象クラスにDBを連想させる命名をすべきではないのでは?create_tableメソッドは削除、insertメソッドは名前を変更したい
    @abstractmethod
    def insert(self, entity: PresentationInfo):
        return
    @abstractmethod
    def updete(self, entity: PresentationInfo):
        return
    @abstractmethod
    def delete(self, id: str):
        return
    @abstractmethod
    def find(self, id: str) -> PresentationInfo:
        return
    @abstractmethod
    def find_all(self) -> list[PresentationInfo]:
        return
