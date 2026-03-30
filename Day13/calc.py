import re
class Solution:
    def op_apply(self):
        b = self.num_stack.pop()
        a = self.num_stack.pop()
        op = self.ops_stack.pop()
        if op == '/':
            self.num_stack.append(int(a/b))
        elif op == '*':
            self.num_stack.append(a*b)
        elif op == '-':
            self.num_stack.append(a-b)
        else:
            self.num_stack.append(a+b)

    def print_stacks(self):
        print(self.num_stack, self.ops_stack)

    def calculate(self, s):
        s = s.replace(' ', '')
        s = re.split(r'([-+*/()])', s)
        tokens = [token for token in s if token != '']
        print(tokens)
        self.num_stack = []
        self.ops_stack = []
        self.print_stacks()
        prev = None

        for token in tokens:
            if token == ')':
                last_op = self.ops_stack[-1]
                while(last_op != '('):
                    self.op_apply()
                    last_op = self.ops_stack[-1]
                self.ops_stack.pop()
            elif token in '(+*/':
                self.ops_stack.append(token)
            elif token == '-':
                if prev is None or prev in '(+*-/':
                    self.num_stack.append(0)
                self.ops_stack.append(token)
            else:
                self.num_stack.append(int(token))
                        
            prev = token
            self.print_stacks()

        while(len(self.num_stack) > 1 and self.ops_stack):
            self.op_apply()

        self.print_stacks()

        return self.num_stack[0]
        



s = Solution()
print(s.calculate('(3+2*2)*(2*2)'))
print(s.calculate('(1+(4+5+2)-3)+(6+8)'))
print(s.calculate("- (3 + (4 + 5))"))
print(s.calculate('5/2'))
print(s.calculate('-5/2'))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate('2-(5-6)'))
print(s.calculate("(7)-(0)+(4)"))