class Room:

   def __init__(self, name, room_capacity):
        self.name = name
        self.room_capacity = room_capacity
        self.guest_list = []
        self.playlist =  []
        

   def check_in(self, guest):
      if len(self.guest_list) < self.room_capacity:
         self.guest_list.append(guest.name)
         return "Welcome"
      else:
         return "try again later"

   def check_out(self, guest):
      self.guest_list.remove(guest.name)

   def add_song(self, song1):
      self.playlist.append(song1.title)
      