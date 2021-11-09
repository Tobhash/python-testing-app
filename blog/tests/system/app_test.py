from unittest import TestCase
from unittest.mock import patch     # let us look what things do!
import blog.app as app
from blog.blog import *


class AppTest(TestCase):

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_ask_create_blog(self):
        # with patch ('blog.app.ask_create_blog') as mocked_ask_create_blog:
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def task_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input', return_value='Test'):
            with patch('blog.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)


    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('blog.app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = app.POST_TEMPLATE.format('Post title', 'Post content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test title')
            self.assertEqual(blog.posts[0].content, 'Test Content')

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author')

            app.menu()

            self.assertIsNotNone(app.blogs['Test Create Blog'])

