from datetime import datetime
import sqlite3

class Hotel():
    NO_OF_ROOMS = 10
    NOT_FOUND = -1
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.noOccupiedRooms = 0
        #self.theRooms = []*self.NO_OF_ROOMS
        self.theRooms = []
        self.numOfRooms = 0

    def isFull(self):
        if self.noOccupiedRooms == self.NO_OF_ROOMS:
            return True
        else:
            return False

    def isEmpty(self):
        if self.noOccupiedRooms == 0:
            return True
        else:
            return False

    def addRoom(self ,roomnumber,bedtype,smoking,price):
        new_room = Room(roomnumber,bedtype,smoking,price)
##        self.roomnumber = roomnumber
##        self.bedtype = bedtype
##        self.smoking = smoking
##        self.price = price
        self.occupied = False
        #self.theRooms[self.numOfRooms] = '{},{},{},{},{}'.format(self.roomnumber,self.bedtype,self.smoking,self.price,self.occupied)
        #file_data = open('F:/Python_Object_Oriented_Programming/SummitWorksTraining/Day5/Assignment/assignment_file.txt','w')
        self.theRooms.append(new_room)
##        file_data.write('{},{},{},{},{}'.format(self.roomnumber,self.bedtype,self.smoking,self.price,self.occupied))
##        file_data.close()
        self.numOfRooms += 1

##    def addReservation(self,occupantName ,smoking, bedtype):
##        self.noOccupiedRooms += 1
##        pass

    def getHotelName(self): #DONE
        return self.name

    def getHotelLocation(self): #DONE
        return self.location

    def setHotelName(self, newhotelname): #DONE
        self.name = newhotelname

    def setHotelLocation(self, newhotellocation): #DONE
        self.location = newhotellocation

    def occupancyPercentage(self): #DONE
        return round((self.noOccupiedRooms / self.numOfRooms) * 100,2)

    def findReservtion(self, occupantname): #DONE
        idx = 0
        for i in range (len(self.theRooms)):
            if(self.theRooms[i].getOccupant()== occupantname):
                return idx
            else:
                idx += 1                
        return self.NOT_FOUND

    def cancelReservation(self,occupantname): #DONE
        idx = self.findReservtion(occupantname)
        if(idx >= 0):
            self.theRooms[idx].setOccupied(False);
            self.noOccupiedRooms -= 1
            print("Reservation was cancelled.")
        else:
            print("Reservation was not canceled.")

    def printReservationList(self): #DONE
        if self.isEmpty == True:
            print('Sorry, There is no room to display.')
            
        else:
            for i in range(len(self.theRooms)):
                if self.theRooms[i].getOccupied() == True:
                    print("The Reservation Information is: ")
                    print("""Room Number: %d \nOccupant name: %s \nSmoking room: %s \nBed Type: %s \nRoom Rate: %d\
                    """%(self.theRooms[i].roomNum, self.theRooms[i].occupantName, self.theRooms[i].bedType, self.theRooms[i].smoking, self.theRooms[i].rate))
                    # %(self.roomNum, self.occupantName, self.smoking, self.bedType, self.price)

    def getDailySales(self): #DONE
        if self.isEmpty == True:
            print('Sorry, There is no room to display.')
            return

        else:
            dailySales = 0
            for i in range(len(self.theRooms)):
               if self.theRooms[i].getOccupied() == True:
                   dailySales = dailySales + self.theRooms[i].rate
            return dailySales
##            today = datetime.date.today()       
##            print('The Daily Sales of ',today, ' is: ',dailySales)       

    def addReservation(self,occupant_name ,smoking, bedtype): #DONE
        reserved = False
        for idx in range(len(self.theRooms)):
            if (self.theRooms[idx].smoking == smoking) and (self.theRooms[idx].bedType == bedtype):
                if (self.theRooms[idx].occupied == False):
                    self.theRooms[idx].occupied = True
                    self.theRooms[idx].occupantName = occupant_name
                    self.noOccupiedRooms += 1
                    reserved = True
        if reserved == False:
            print('The reservation was not made.')
        else:
            print('The reservation was made.')

    
    def __str__(self): #DONE
        return """Hotel Name: %s \nNumber of Rooms: %d\n Number of Occupied Rooms %d\nRoom Details are:\n
        """ %(self.name, self.numOfRooms,self.noOccupiedRooms)
        #Room Details are:\nRoom Number: %d \nOccupant name: %s \nSmoking room: %s \nBed Type: %s \nRoom Rate: %d\
        #,self.theRooms.roomNum, self.theRooms.occupantName, self.theRooms.smoking, self.theRooms.bedType, self.theRooms.rate)
       
                           

class Room():
    def __init__(self, roomNum, bedType, smoking, rate):
        self.roomNum = roomNum
        self.bedType = bedType
        self.smoking = smoking
        self.rate = rate
        self.occupied = False
        self.occupantName = 'Not Occupied'

    def getBedType(self): #DONE
        return self.bedType

    def getSmoking(self): #DONE
        return self.smoking

    def getRoomNum(self): #DONE
        return self.roomNum

    def getRoomRate(self): #DONE
        return self.rate

    def getOccupant(self): #DONE
        return self.occupantName

    def getOccupied(self): #DONE
        return self.occupied

    def setOccupied(self, occupied): #DONE
        self.occupied = occupied

    def setOccupant(self, occupant): #DONE
        self.occupantName = occupant

    def setRoomNum(self, roomno): #DONE
        self.roomNum = roomno

    def __str__(self): #DONE
        return """The Rooms Information:\nRoom Number: %d \nOccupant name: %s \nSmoking room: %s \nBed Type: %s \nRoom Rate: %d\
        """ %(self.roomNum, self.occupantName, self.smoking, self.bedType, self.rate)

    def setBedType(self, bedtype): #DONE
        self.bedType = bedtype

    def setRate(self, roomrate): #DONE
        self.rate = roomrate

    def setSmoking(self, somokingstatus): #DONE
        self.smoking = somokingstatus

    def isOccupied(self): #DONE
        return self.occupied
        
############################TESTING PART####################################
conn = sqlite3.connect('database_68')
cur = conn.cursor()
cur.execute('CREATE TABLE Hotel (hotel_id INTEGER, hotel_name VARCHAR, hotel_address VARCHAR, PRIMARY KEY (hotel_id));')
print('CONNECTION')
conn.commit()

conn.close()
    
hotel = Hotel('Diana Hotel','London') #Testing, creating an instance of Hotel class
hotel.addRoom(101,'queen','n',88) #Testing the addRoom() Function
hotel.addRoom(102,'queen','s',99) #Testing the addRoom() Function
hotel.addRoom(103,'twin','n',77)  #Testing the addRoom() Function
hotel.addRoom(101,'twin','s',66)  #Testing the addRoom() Function
hotel.addRoom(105,'king','n',112) #Testing the addRoom() Function
hotel.addRoom(106,'king','s',133) #Testing the addRoom() Function
print(hotel.theRooms[0].bedType) #Testing, accessing the bedtype of room
hotel.addReservation('Eyad','s','king') #Testing the addReservation() Function
s = hotel.getDailySales()#Testing the getDailySales() Function
print('The daily sales is: ', s, ' Dollar') #Testing the getDailySales() Function by printing its return value
hotel.printReservationList() # Testing the printReservationList() Function
hotel.cancelReservation('Eyad') #Testing the cancelReservation() Function
hotel.printReservationList()    #Testing the printReservationList() Function
hotel.addReservation('Eyad','s','king') #Testing the addReservation() Function
hotel.addReservation('Akram','n','twin')#Testing the addReservation() Function
hotel.printReservationList() #Testing the printReservationList() Function
print('The hotel is full: ',hotel.isFull()) #Testing the isFull() Function
print('The hotel is empty: ',hotel.isEmpty()) #Testing the isEmpty() Function
print('The hotel name is ',hotel.getHotelName()) #Testing the getHotelName() Function 
print('The hotel location is ', hotel.getHotelLocation()) #Testing the getHotelLocation() Function
hotel.setHotelName('Taj Mahal Hotel') #Testing the setHotelName() Function
print('The hotel new name is ',hotel.getHotelName()) #Testing the getHotelName() Function 
hotel.setHotelLocation('Mumbai') #Testing the setHotelLocation() Function
print('The hotel new location is ', hotel.getHotelLocation()) #Testing the getHotelLocation() Function
print('The occupancy percentage of the hotel is: ', hotel.occupancyPercentage())#Testing the occupancyPercentage() Function
print(hotel.findReservtion('Eyad')) #Testing the findReservtion() Function
print('The bed type is : ' ,hotel.theRooms[0].getBedType()) # Testing the getBedType() Function
print('The smoking in this room is :',hotel.theRooms[0].getSmoking()) # Testing the getSmoking() Function
print('The room No. is: ', hotel.theRooms[0].getRoomNum()) # Testing the getRoomNum() Function
print('The room rate is: ', hotel.theRooms[0].getRoomRate()) #Testing the getRoomRate() Function
print('The occupant name is: ', hotel.theRooms[0].getOccupant()) #testing the getOccupant() Function
print('Is this room occupied?-getOccupied(): ', hotel.theRooms[0].getOccupied()) #testing the getOccupied()Function
hotel.theRooms[0].setOccupied(False) #testing the setOccupied()Function
hotel.theRooms[0].setOccupant('Maruthi') #testing the setOccupied()Function
hotel.theRooms[0].setRoomNum(107) #testing the setOccupied()Function
hotel.theRooms[0].setBedType('Twin') #testing the setOccupied()Function
hotel.theRooms[0].setRate(159) #testing the setOccupied()Function
hotel.theRooms[0].setSmoking('s') #testing the setOccupied()Function
print('Is the room occupied?-isOccupied(): ',hotel.theRooms[0].isOccupied())
print(hotel)
