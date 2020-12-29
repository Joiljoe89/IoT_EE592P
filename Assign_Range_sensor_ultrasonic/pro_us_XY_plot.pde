import processing.serial.*;
Serial myPort;
//int values;
int[] values=new int[2];
float xPos=0;
float yPos=0;

void setup(){
  size(500,500);
   printArray(Serial.list()); //list all the available serial ports
  String portName = Serial.list()[0];//index 1 in serial list for arduino
  myPort = new Serial(this, portName, 9600);//don't generate a serialEvent() until you get a newline character
  myPort.bufferUntil('\n');
  
}
void draw(){
  /*if (myPort.available()>0) {
    values=myPort.read();
  }*/
  background(255); //0for blk and 255 for white
  
  stroke(0,0,200);
  strokeWeight(5);
  line(values[0],0,values[0],values[1]);
  stroke(0,200,0);
  line(0,values[1],values[0],values[1]);
  
}


void serialEvent(Serial myPort){
  
      String inString=myPort.readStringUntil('\n');//get the ASCII string
      
      if(inString!=null){
        inString=trim(inString);//trim off any whitespace
        values=int(splitTokens(inString,", \t")); //split the string, delimiter can be comma or tab
        printArray(values);
        
      }
}