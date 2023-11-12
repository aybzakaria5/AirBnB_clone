#!/usr/bin/python3
"""a inittest for the consol module
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, func, *args):
        func(*args)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='create BaseModel')
    @patch('models.storage')
    def test_create(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('{}\n'.format(BaseModel().id), HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')

    @patch('builtins.input', return_value='show BaseModel {}'.format(BaseModel().id))
    @patch('models.storage')
    def test_show(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('{}\n'.format(repr(BaseModel())), HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')

    @patch('builtins.input', return_value='all')
    @patch('models.storage')
    def test_all(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('[{}]'.format(repr(BaseModel())), HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')

    @patch('builtins.input', return_value='count BaseModel')
    @patch('models.storage')
    def test_count(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('1\n', HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')

    @patch('builtins.input', return_value='destroy BaseModel {}'.format(BaseModel().id))
    @patch('models.storage')
    def test_destroy(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('', HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')
        mock_storage.all.return_value = {'BaseModel.{}'.format(BaseModel().id): MagicMock()}
        mock_storage.save.assert_called_once()

    @patch('builtins.input', return_value='update BaseModel {} name "new_name"'.format(BaseModel().id))
    @patch('models.storage')
    def test_update(self, mock_storage, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout('', HBNBCommand().cmdloop)
        mock_input.assert_called_once_with('(hbnb) ')
        mock_storage.all.return_value = {'BaseModel.{}'.format(BaseModel().id): MagicMock()}
        mock_storage.save.assert_called_once()

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(HBNBCommand().onecmd('quit'))
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().emptyline()
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_do_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
            self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()