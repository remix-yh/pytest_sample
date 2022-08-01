class DeviceController():
    def execute(self, value):
        # GPIO処理
        raise Exception("device not found!!!")

class Controller():
    def execute_control(self, value):
        device = DeviceController()
        device.execute(value)
        device.execute(value + 1)
        device.execute(100)
        if value == 1000:
            device.execute(value + 1000)
