def tower_of_hanoi(n,from_rod,aux_rod,to_rod):
      if n==0:
            return
      tower_of_hanoi(n-1,from_rod,aux_rod,to_rod)
      print("Moving Disk",n,"from rod",from_rod,"to rod",to_rod)
      tower_of_hanoi(n-1,aux_rod,to_rod,from_rod)
n=3
tower_of_hanoi(n,'A','B','C')
 