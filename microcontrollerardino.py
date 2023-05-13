'''This program is written by Tehzeeb imtiaz(2021_Mc_73) and amina ahmed(2021_Mc_71) 
this program is used to control the car by using hand gesture and written
 in complete python using media pipe '''
import pyfirmata as py
port='COM4'
out=""
ardiuno_board=py.Arduino(port)
# (pintype:pin num:pin mode)
RightSpeed=ardiuno_board.get_pin('d:7:o')
Rightpin1=ardiuno_board.get_pin("d:11:o")
Rightpin2=ardiuno_board.get_pin("d:12:o")
Leftpin3=ardiuno_board.get_pin("d:13:o")
Leftpin4=ardiuno_board.get_pin("d:8:o")
Leftspeed=ardiuno_board.get_pin("d:9:o")

def rcCarControl(Total):
    if Total==0:
      RightSpeed.write(0)
      Rightpin1.write(0)
      Rightpin2.write(0)
      Leftpin3.write(0)
      Leftpin4.write(0)
      Leftspeed.write(0)
      print ('Brake')
      return 'Brake'
    if Total==2:
      RightSpeed.write(0)
      Rightpin1.write(0)
      Rightpin2.write(0)
      Leftpin3.write(1)
      Leftpin4.write(0)
      Leftspeed.write(1)
      print ('Right')
      return 'Right'
    if Total==3:
      RightSpeed.write(1)
      Rightpin1.write(1)
      Rightpin2.write(0)
      Leftpin3.write(0)
      Leftpin4.write(0)
      Leftspeed.write(0)
      print ('Left')
      return 'Left'
    if Total==4:
      RightSpeed.write(1)
      Rightpin1.write(0)
      Rightpin2.write(1)
      Leftpin3.write(0)
      Leftpin4.write(1)
      Leftspeed.write(1)
      print ('Backward')
      return 'backward'
    if Total==5:
      RightSpeed.write(1)
      Rightpin1.write(1)
      Rightpin2.write(0)
      Leftpin3.write(1)
      Leftpin4.write(0)
      Leftspeed.write(1)
      print ('Forward')
      return 'Forward'
    
      
              
       






