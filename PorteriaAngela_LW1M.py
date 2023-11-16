def create_stack():
    stack_name = input("Name the Stack: ")
    stack = list()
    print(f"Created Stack: {stack_name}", stack)
    return stack_name, stack

def isempty(stack):
    return len(stack) == 0

def push(stack, element):
    stack.append(element)
    print("Added Element: "+ element)

def pop(stack):
    if (isempty(stack)):
        pass
    else:
        return stack.pop()

def show(stack):
    if (isempty(stack)):
        print("Stack is empty")
    else:
        print(f"{stack_name} Elements:")
        for i in stack:
            print(i, end =',')

def peek(stack):
    if (isempty(stack)):
        print("Stack is empty")
    else:
        return stack[-1]

stack = None

while True:
    operations = ("""\n\n[C]: Create Stack\n[A]: Append Element to Stack\n[D]: Remove Element to Stack\n[P]: Peek the Top Element of Stack
[S]: Show the Stack Elements\n[E]: Exit\n""")
    print(operations)
    choice = input("Choose what stack operation to use: ").upper()

    if choice == 'C':
        stack_name, stack = create_stack()
    elif choice == 'A':
        if stack is not None:
            element = input("Element to add in the Stack: ")
            push(stack, element)
            show(stack)
        else:
            print("Create a stack first")
    elif choice == 'D':
        if stack is not None:
            pop(stack)
            show(stack)
        else:
            print("Create a stack first")
    elif choice == 'P':
        if stack is not None:
            peek_stack = peek(stack)
            print("Peek Content: ",peek_stack)
            show(stack)
        else:
            print("Create a stack first")
    elif choice == 'S':
        if stack is not None:
            show(stack)
        else:
            print("Create a stack first")
    elif choice == 'E':
        break
    else:
        print("Select only from the choices.")

