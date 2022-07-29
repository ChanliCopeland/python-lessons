import argparse
import sys

employees = []

class CreatePerson(object):
    def __init__ (self, name, number, status):
        #set variables
        self.name = name
        self.number = number
        self.status = status

    def deactivate_person(self):
        self.status = "deactivated"
        return f"{self.name} has been {self.status}"

    def activate_person(self):
        self.status = "deactivated"
        return f"{self.name} has been {self.status}"


        
  

if __name__ == "__main__":
    #ask for docker repo information
    try:
        parser = argparse.ArgumentParser(description = 'Creates a person')

        parser.add_argument('-i', 
                            '--interactive',
                            dest='INTERACTIVE', 
                            required='--interactive' not in sys.argv, 
                            choices=['true','false'], 
                            default='false', 
                            help='Boolean true/false to start interactive mode')
        parser.add_argument('-n', 
                            '--name', 
                            dest='NAME', 
                            required='--interactive' == 'false',
                            help='Persons Name')
        parser.add_argument('-d', 
                            '--identification', 
                            dest='NUMBER', 
                            required='--interactive' == 'false',
                            help='Persons Id')
        parser.add_argument('-s', 
                            '--status', 
                            dest='STATUS', 
                            required='--interactive' == 'false',
                            choices=['active','deactive'],
                            help='Persons work status')                                                        
                         
        args = parser.parse_args()
    except Exception as e:
        print(e)
        parser.print_help()
        sys.exit(0)


    #If interactive then set variables based on input
    if args.INTERACTIVE == 'true':
        args.NAME = input("Person's Name?: ")
        args.NUMBER = input('Employee ID?" ')
        args.STATUS = input('Employee Status?" ')

    chandler = CreatePerson(args.NAME, args.NUMBER, args.STATUS)
    print(vars(chandler))
#    chandler.deactivate_person()
#    print(chandler.status)
#    chandler.activate_person()
#    print(chandler.status)
    


