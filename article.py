class Article:
    def __init__(self, title, content, category, author):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (2 <= len(title) <= 100):  # Example length constraint
            raise ValueError("Title must be between 2 and 100 characters inclusive")

        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        if len(content) == 0:
            raise ValueError("Content cannot be empty")

        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category cannot be empty")

        if not isinstance(author, author):
            raise TypeError("Author must be an instance of Author class")

        self._title = title
        self._content = content
        self._category = category
        self._author = author
        self._summary = self._generate_summary()

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("Content must be a string")
        if len(value) == 0:
            raise ValueError("Content cannot be empty")
        self._content = value
        self._summary = self._generate_summary()

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

    @property
    def author(self):
        return self._author

    @property
    def summary(self):
        return self._summary

    def _generate_summary(self):
        # Assuming summary is first 30 characters of content
        return self._content[:30] + "..." if len(self._content) > 30 else self._content
