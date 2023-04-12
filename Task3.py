channels = ["BBC", "Discovery", "TV1000"]

class TVConrtoller():

    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, N):
        self.current_index = N - 1
        return self.channels[self.current_index]

    def next_channel(self):
        if self.current_index == len(channels) - 1:
            self.current_index = 0
        else:
            self.current_index = self.current_index + 1
        return self.channels[self.current_index]

    def previous_channel(self):
        if self.current_index == 0:
            self.current_index = len(channels) - 1
        else:
            self.current_index = self.current_index - 1
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def is_exist(self, N_name):
        if type(N_name) == int:
            if N_name >= 1 and N_name <= len(channels):
                return 'Yes'
            else:
                return 'No'
        else:
            if N_name in self.channels:
                return 'Yes'
            else:
                return 'No'

controller = TVConrtoller(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(2))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist('BB'))