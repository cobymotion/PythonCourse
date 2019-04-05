const int Trigger = 11;   //Pin digital 2 para el Trigger del sensor
const int Echo = 12;   //Pin digital 3 para el Echo del sensor

long distancia;
int ledV = 5;
int ledA = 6;
int ledR = 7;
char dato;

void setup() {
  Serial.begin(9600);//iniciailzamos la comunicación
  pinMode(Trigger, OUTPUT); //pin como salida
  pinMode(Echo, INPUT);  //pin como entrada
  pinMode(ledV, OUTPUT);
  pinMode(ledA, OUTPUT);
  pinMode(ledR, OUTPUT);
  digitalWrite(Trigger, LOW);//Inicializamos el pin con 0
}

void loop(){

  distancia = medirDistancia();
  Serial.println(distancia);
  if(Serial.available() > 0 ){
      dato = Serial.read();
      switch(dato){
        case 'r': case 'R':
          digitalWrite(ledV, LOW);
          digitalWrite(ledA, LOW);
          digitalWrite(ledR, HIGH);
          break;
        case 'a': case 'A':
          digitalWrite(ledV, LOW);
          digitalWrite(ledA, HIGH);
          digitalWrite(ledR, LOW);
          break;
        case 'v': case 'V':
          digitalWrite(ledV, HIGH);
          digitalWrite(ledA, LOW);
          digitalWrite(ledR, LOW);
          break;
        case 't': case 'T':
          digitalWrite(ledV, LOW);
          digitalWrite(ledA, LOW);
          digitalWrite(ledR, LOW);
        default: break;
      }
    }
    Serial.flush();

}

long medirDistancia(){
  long t; //timepo que demora en llegar el eco
  long d; //distancia en centimetros

  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);          //Enviamos un pulso de 10us
  digitalWrite(Trigger, LOW);
  
  t = pulseIn(Echo, HIGH); //obtenemos el ancho del pulso
  d = t/59;             //escalamos el tiempo a una distancia en cm
  
  
  delay(100);          //Hacemos una pausa de 100ms
  return d;
}
