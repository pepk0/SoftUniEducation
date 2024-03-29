from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self) -> None:
        self.categories: list = []
        self.topics: list = []
        self.documents: list = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        if category_id in self.categories:
            category = self.categories[self.categories.index(category_id)]
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str,
                   new_storage_folder: str) -> None:
        if topic_id in self.topics:
            topic: Topic = self.topics[self.topics.index(topic_id)]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        if document_id in self.documents:
            document = self.documents[self.documents.index(document_id)]
            document.file_name = new_file_name

    def delete_category(self, category_id) -> None:
        if category_id in self.categories:
            self.categories.remove(category_id)

    def delete_topic(self, topic_id) -> None:
        if topic_id in self.topics:
            self.topics.remove(topic_id)

    def delete_document(self, document_id) -> None:
        if document_id in self.documents:
            self.documents.remove(document_id)

    def get_document(self, document_id: int) -> Document or None:
        if document_id in self.documents:
            return self.documents[self.documents.index(document_id)]

    def __repr__(self) -> str:
        return "\n".join(str(doc) for doc in self.documents)
