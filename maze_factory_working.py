from enum import Enum

class Mapsite():
    def Enter(self):
        raise NotImplementedError('Abstract base class method')

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Room(Mapsite):
    def __init__(self, roomNo):
        self._sides = [Mapsite] * 4
        self._roomNumber = int(roomNo)

    def GetSide(self, Direction):
        return self._sides[Direction]

    def SetSide(self, Direction, Mapsite):
        self._sides[Direction] = Mapsite

    def Enter(self):
        print('   You have entered room:  ' + str(self._roomNumber))

class Wall(Mapsite):
    def Enter(self):
        print('   You just ran into the wall.... ')

class Door(Mapsite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False

    def OtherSideFrom(self, Room):
        print('\t Door obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room =  self._room2
        else:
            other_room = self._room1
        return other_room

    def Enter(self):
        if self._isOpen: print(' ****** You have passed through this door ******')
        else: print(' *** This door needs to be opened before you can pass through ***')

class Maze():
    def __init__(self):
        #dictionary to hold room_number, room_obj <key, value> pairs
        self._rooms = {}

    def AddRoom(self, room):
        #use roomNumber as lookup value to retrieve room object
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms[room_number]


class MazeFactory():
    @classmethod
    def MakeMaze(cls):
        return Maze()

    @classmethod
    def MakeWall(cls):
        return Wall()

    @classmethod
    def MakeRoom(cls, n):
        return Room(n)

    @classmethod
    def MakeDoor(cls, r1, r2):
        return Door(r1, r2)


class MazeGame():
    def CreateMaze(self, factory=MazeFactory, number_of_rooms = 2):
        aMaze = factory.MakeMaze()

        for i in range(0, number_of_rooms-1):
              r1 = factory.MakeRoom(i)
              r2 = factory.MakeRoom(i+1)
              aDoor = factory.MakeDoor(r1,r2)

              aMaze.AddRoom(r1)
              aMaze.AddRoom(r2)

              r1.SetSide(Direction.North.value, factory.MakeWall())
              r1.SetSide(Direction.East.value, aDoor)
              r1.SetSide(Direction.South.value, factory.MakeWall())
              r1.SetSide(Direction.West.value, factory.MakeWall())

              r2.SetSide(Direction(0).value, factory.MakeWall())
              r2.SetSide(Direction(1).value, factory.MakeWall())
              r2.SetSide(Direction(2).value, factory.MakeWall())
              r2.SetSide(Direction(3).value, aDoor)

        return aMaze


def find_maze_rooms(maze_obj):

        #find its rooms
        maze_rooms = []
        for room_number in range(5):
            try:
                # get the room number
                room = maze_obj.RoomNo(room_number)
                print('\n ^^^ Maze has room: {}'.format(room_number, room))
                print('     Entering the Room...')
                room.Enter()
                #append rooms to list
                maze_rooms.append(room)
                for idx in range(4):
                    side = room.GetSide(idx)
                    side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")
                    print(' Room: {}, {:<15s}, Type: {}'.format(room_number,Direction(idx), side_str))
                    print(' Trying to enter:  ', Direction(idx))
                    side.Enter()
                    #if Door in side_str:
                    if 'Door' == side_str:
                        door = side
                        if not door._isOpen:
                            print('     *** Opening the door...')
                            door._isOpen = True
                            door.Enter()
                        print('\t', door)
                        # get the room on the other side of the door
                        other_room = door.OtherSideFrom(room)
                        print('\t On the other side of the door is Room: {}\n'.format(other_room._roomNumber))

            except KeyError:
                print('No room:', room_number)

        num_of_rooms = len(maze_rooms)

        print ('******************************************************')
        print(' YOU HAVE WON!')
        print('******************************************************')
        print(' ')
        print(' There were {} rooms in the Maze' .format(num_of_rooms))
        print(' Door were either on the East or tbe West side of the rooms')
        print(' You managed to pass through all the doors and explore all the room! :)')



if __name__ == '__main__':

#*********** USER INPUT ********************************************************

    # Please specify the numbers of rooms in the maze
    number_of_rooms = int(input("\n\nPlease specify the size of the maze? Where size means the number of rooms: "))

#*******************************************************************************

    print('*' * 21 )
    print('~~~The Maze Game~~~')
    print('*' * 21 )

    #Creating the original maze and passing it as a factory
    factory = MazeFactory() #pass in class directly
    print(factory)

    maze_obj =  MazeGame().CreateMaze(factory, number_of_rooms)
    find_maze_rooms(maze_obj)
