def get_input():
                try:
                                mob=int(input("Enter Your Mobile Number :"))
                                if len(str(mob)) > 10 or len(str(mob)) < 10:
                                                print("\n NOT VALID...........\n")
                                                mob=get_input()
                                else:
                                                print("\n Successful \n")

                except ValueError:
                                print("\n NOT VALID...........\n")
                                mob=get_input()
                return mob
print("Your Mobile Number is :",get_input())
                                                
