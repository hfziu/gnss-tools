class Register:
    def __init__(self, length, feedback, out=1, *init):
        if init:
            self.init = init[0]
            self.register_list = init[0]
        else:
            self.init = []
            for _ in range(length):
                self.init.append(1)
            self.register_list = self.init

        # Feedback Position (list)
        self.feedback = []
        for fb in feedback:
            self.feedback.append(fb-1)

        # Output Position (list)
        if isinstance(out, int):
            out = [out]
        self.out = out

    def shift(self):
        output = []
        for op in self.out:
            output.append(self.register_list[op-1])

        head = (self.register_list[self.feedback[0]] ^
                self.register_list[self.feedback[1]])
        if len(self.feedback) > 2:
            for fb in self.feedback[2:]:
                head = head ^ self.register_list[fb]

        # Shift
        self.register_list = [head] + self.register_list[:-1]
        return output

    def reset(self):
        self.register_list = self.init
