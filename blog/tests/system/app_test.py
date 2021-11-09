from unittest import TestCase
from unittest.mock import patch     # let us look what things do!
import blog.app as app
from blog.blog import *


class AppTest(TestCase):

    def setUp(self):
        self.blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': self.blog}

# Testing methods

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('blog.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(self.blog)


    def test_print_posts(self):
        self.blog.posts.append(Post('Test Post', 'Test content'))
        with patch('blog.app.print_post') as mocked_print_post:
            app.print_posts(self.blog)

            mocked_print_post.assert_called_with(self.blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = app.POST_TEMPLATE.format('Post title', 'Post content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test Content')
            app.ask_create_post()
            self.assertEqual(self.blog.posts[0].title, 'Test title')
            self.assertEqual(self.blog.posts[0].content, 'Test Content')

# Testing menu

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author','q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_menu_calls_read_blogs(self):
        with patch('blog.app.ask_read_blog') as mocked_ask_read_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('r', self.blog.title, 'q')
                app.menu()
                mocked_ask_read_blog.assert_called_with()

    def test_menu_calls_create_post(self):
        with patch('blog.app.ask_create_post') as mocked_ask_create_post:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('p', self.blog.title, 'Test title', 'Test content', 'q')
                app.menu()
                mocked_ask_create_post.assert_called_with()
