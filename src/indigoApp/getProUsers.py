#from keywordScrape import KeywordProvider
from models import CategoryCustomerMap
from models import Customers

class ProUsers:

    def getUsers(self, category, keyword):
        if category:
            return self.getUsersFromCategory(category)

        if keyword:
            #keywords = KeywordProvider.getKeywords(KeywordProvider, keyword)
            return self.getUsersFromKeyword(keyword)


    def getUsersFromCategory(categoryInput):
        for categoryCustomer in CategoryCustomerMap.objects.filter(category=categoryInput):
            customers = Customers.objects.filter(Id=categoryCustomer.CustomerId)
            for customer in customers:
                print customer.Name
        return

    def getUsersFromKeyword(keyword):
        return



ProUsers.getUsers(ProUsers, "Appliances", None)

