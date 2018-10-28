 # bondi-script

Script realizado con la intención de tener en una terminal la información que aplicaciones como "Como Ir" o "Cutcsa" te dan en Android.
La idea es luego de tener la información que querés, configurar un cron con algúna aplicación de notificaciones (mail, o mensajes de slack) para avisarte cuando está por pasar el ómnibus que te interese en la parada más cercana, sin la necesidad de sacar tu celular.

## Uso

``` python bondi-script.py -p<numero-de-parada> -b<linea-de-omnibus> ```

Ejemplo

``` 
python bondi-scipt.py -p2664 -b328 
=======
``` python bondi-scipt.py -p2664 -b328 
El 328 está a punto de pasar en 23 minutos
```


