from unittest.mock import call
import pytest
from src.control import Controller

class TestClassController():
    def test_execute_control(self, mocker):
        device_control_mock = mocker.patch('src.control.DeviceController')
        controller = Controller()
        controller.execute_control(1001)
        hoge = device_control_mock()
        hoge.execute.assert_has_calls([call(1001), call(1002), call(100)])

        
