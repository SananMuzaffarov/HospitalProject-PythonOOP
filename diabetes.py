class Diabetes:
    def __init__(self, Room_Num, Total_Client, Doctor_Count):
        self.Room_Num = Room_Num
        self.Total_Client = Total_Client
        self.Doctor_Count = Doctor_Count

    def DiabetesInfo(self):
        return """
                Welcome to Diabetes branch!

                Room Number : {}

                Total Number of Clients : {}

                Doctor Count : {}

                """.format(self.Room_Num, self.Total_Client, self.Doctor_Count)
