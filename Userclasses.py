class Subject:
    def __init__(self,name,rating,price):
        self.name = name
        self.rating = rating
        self.price = price

class User:

    def __init__(self, name, email, password, location="", qualifications=[]):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.name = name  # string
        self.email = email  # string
        self.password = password
        self.location = location #string
        self.qualifications = qualifications #list of Class Subjects

        """
        Write method to update qualifications
        """

    """takes a User,"""
    def add_sub(self,sub_name):
        self.qualifications.append(sub_name)

    def update_loc(self,location_str):
        self.location = location_str


"""Here starts the backend pseudo code"""




"""Here Starts some test code"""
user1 = User("Jake","email", "password")
sub1 = Subject("econ",5,69)
user1.add_sub(sub1)
print(user1.qualifications[0].price)