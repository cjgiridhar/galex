from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from journal.models import Article

# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(author_id=1, title="Chetan")
        Article.objects.create(author_id=2, title="Giridhar")

    def test_article_detail(self):
        article = Article.objects.get(title="Chetan")
        self.assertEquals(article.author_id, 1)

    def test_article_doesnt_exist(self):
        try:
            article = Article.objects.get(title="Sanjay")
        except ObjectDoesNotExist:
            self.assertTrue("Passed!")

    def test_article_list(self):
        articles = Article.objects.all()
        self.assertEquals(len(articles),2)