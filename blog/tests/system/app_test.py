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
