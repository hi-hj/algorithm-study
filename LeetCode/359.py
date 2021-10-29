from typing import List

class Logger:

    def __init__(self):
        self._msg_dict = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp + 10
            return True

        else:
            if self._msg_dict[message] <= timestamp:
                self._msg_dict[message] = timestamp + 10
                return True
            elif self._msg_dict[message] > timestamp:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

