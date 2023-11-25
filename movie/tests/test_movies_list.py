from django.test import TestCase, Client
from movie.models import Movie, Actor


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test Film', imdb=9.2, year='2023-02-23', genre='Drama')
        self.client = Client()

    def test_get_all_movie(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertAlmostEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Test Film')

    def test_search_movie(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'Test Film')

    def test_order_movies_by_imdb(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)






