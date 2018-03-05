

class Property:
    """
    Represents a property square feet with beds, bathes
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        :return: Screen info
        """
        print("PROPERTY DETAILS")
        print('================')
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def promt_init():
        """
        :return: needed information about the property
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input('Enter number of bedrooms: '),
                    baths=input('Enter number of baths: '))

    promt_init = staticmethod(promt_init)


class Apartment(Property):
    """
    Represents a big flat - apartment
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        :param balcony: whether there is a balcony
        :param laundry: whether there is a laundry
        :param kwargs:  other needed information
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        :return: Menu information
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: &s" % self.laundry)
        print("balconies: &s" % self.laundry)

    def promt_init():
        """
        :return: gets all the information
        """
        parent_init = Property.promt_init()
        laundry = get_valid_input("What laundry facilities does "
                                  "the property has?",
                                  Apartment.valid_laundries)

        balcony = get_valid_input("Does property have balcony ?",
                                  Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    promt_init = staticmethod(promt_init)


def get_valid_input(input_string, valid_options):
    """
    This function helps in finding and getting information about the property
    :param input_string: The string of needed furniture
    :param valid_options: what is available
    :return: the response of the enter
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class House(Property):
    """
    Class represents houses
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        :return: Property information
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories".format(self.num_stories))
        print("Garage: {}".format(self.garage))
        print("Fenced yard: {}".format(self.fenced))

    def promt_init():
        """
        :return: Gets the needed information
        """
        parent_init = Property.promt_init()
        fenced = get_valid_input('Is the yard fenced?', House.valid_fenced)
        garage = get_valid_input('Is there a garage?', House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    promt_init = staticmethod(promt_init)


class Purchase(object):
    """
    The purchase "method"
    Has prices and taxes
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        :return: Purchasing informmation
        """
        super().display()
        print('PURCHASE DETAILS')
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def promt_init():
        """
        :return: Gets price and taxes
        """

        return dict(
            price=input("WHat is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    promt_init = staticmethod(promt_init)


class Rental(object):
    """
    Represents a rental "method"
    """
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        """
        :return: Shows info about rent, utilities, furniture
        """
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def promt_init():
        """
        :return: GEts the information about rent, utilities, furniture
        """
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated utilities"),
                    furnished=get_valid_input("Is the property furnished?",
                                              ("yes", "no")))

    promt_init = staticmethod(promt_init)


class HouseRental(object):

    def __init__(self):
        self.house = House()
        self.rental = Rental()

    def display(self):
        """
        :return: Shows the rental details of a house
        """
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rental.rent))
        print("estimated utilities: {}".format(self.rental.utilities))
        print("furnished: {}".format(self.rental.furnished))

    def promt_init():
        """
        :return: Gets needed rental information using composition
        """
        init = House.promt_init()
        init.update(Rental.promt_init())
        return init

    promt_init = staticmethod(promt_init)


class ApartmentRental(object):
    """
    Represents flats rental info
    """
    def __init__(self):
        self.apartment = Apartment()
        self.rental = Rental()

    def display(self):
        """
        :return: Shows a rental info
        """
        print('Rental DETAILS')
        print("rent: {}".format(self.rental.rent))
        print("estimated utilities: {}".format(self.rental.utilities))
        print("furnished: {}".format(self.rental.furnished))

    def promt_init():
        """
        :return: Gets a rental info using composition
        """
        init = Apartment.promt_init()
        init.update(Rental.promt_init())
        return init

    promt_init = staticmethod(promt_init)


class ApartmentPurchase(object):
    """
    Represents flat purchase information
    """
    def __init__(self):
        self.apartment = Apartment()
        self.purchase = Purchase()

    def display(self):
        """
        Shows prices and taxes
        :return:
        """
        print('PURCHASE DETAILS')
        print("selling price: {}".format(self.purchase.price))
        print("estimated taxes: {}".format(self.purchase.taxes))

    def promt_init():
        """
        :return: Gets prices and taxes
        """
        init = Apartment.promt_init()
        init.update(Purchase.promt_init())
        return init

    promt_init = staticmethod(promt_init)


class HousePurchase(object):
    """
    Represents a house purchase information
    """
    def __init__(self):
        self.purchase = Purchase()

    def display(self):
        """
        Shows the info about prices and taxes
        :return: None
        """
        print('PURCHASE DETAILS')
        print("selling price: {}".format(self.purchase.price))
        print("estimated taxes: {}".format(self.purchase.taxes))

    def promt_init():
        """
        :return: Gets the info about prices and taxes
        """
        init = House.promt_init()
        init.update(Purchase.promt_init())
        return init

    promt_init = staticmethod(promt_init)


class Agent:
    """
    The users client which can get you anything you want
    """
    def __init__(self):
        self.property_list = []
        self.adress = self.get_adress()

    def display_properties(self):
        """
        :return: a menu of all of the properties
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.promt_init()
        self.property_list.append(PropertyClass(**init_args))

    def read_high_limit(self):
        """
        :return: the customers wilingness to pay
        """
        maxi = input("WHat is the maximum price you "
                     "wish to pay for the property?")
        return maxi

    def get_adress(self):
        """
        :return: THe adress of the building
        """
        adress = input("Enter the adress:")
        return adress
