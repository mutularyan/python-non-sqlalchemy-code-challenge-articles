class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be modified")

    def add_article(self, article):
        if not isinstance(article, article):
            raise TypeError("Article must be of type Article")
        self._articles.append(article)

    def create_article(self, magazine, title):
        article = article(self, magazine, title)
        self.add_article(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))
