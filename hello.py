class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']


# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!


class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length
    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"

# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world