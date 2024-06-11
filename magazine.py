class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters inclusive")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category cannot be empty")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value

    def add_article(self, article):
        if not isinstance(article, article):
            raise TypeError("Article must be of type Article")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]
