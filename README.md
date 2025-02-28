# SpamBotText

SpamBotText es un bot multifuncional escrito en Python que permite automatizar tareas comunes como el minado automático en Minecraft, el envío masivo de mensajes en WhatsApp y el spam de stickers. Utiliza las bibliotecas `pyautogui`, `keyboard` y `time` para interactuar con la pantalla y el teclado.

## Características
- **Minado Automático (Minecraft):** Mantiene presionados los botones necesarios para minar de manera continua.
- **Spamear Mensajes (WhatsApp):** Escribe y envía un mensaje repetidamente en la ventana activa de WhatsApp Web.
- **Spamear Stickers (WhatsApp):** Realiza clics repetidos en un sticker para enviarlo múltiples veces.

## Requisitos
Para que el script funcione correctamente, es necesario instalar las siguientes bibliotecas de Python:
```sh
pip install pyautogui keyboard
```

## Uso
1. **Ejecutar el script**
   ```sh
   python script.py
   ```
2. **Seleccionar una opción:**
   - `[1]` Minado automático en Minecraft
   - `[2]` Spamear mensajes en WhatsApp
   - `[3]` Spamear stickers en WhatsApp

### **Modo Minado Automático (Minecraft)**
1. Selecciona la opción `1`.
2. Espera la cuenta regresiva.
3. El script mantendrá presionadas las teclas necesarias para minar.
4. Para detenerlo, presiona `Ctrl + L`.

### **Modo Spam de Mensajes (WhatsApp)**
1. Selecciona la opción `2`.
2. Ingresa el mensaje a spamear.
3. Especifica la cantidad de veces que se enviará el mensaje.
4. Tienes 5 segundos para colocar el cursor en el cuadro de texto de WhatsApp.
5. El script comenzará a escribir y enviar el mensaje automáticamente.

### **Modo Spam de Stickers (WhatsApp)**
1. Selecciona la opción `3`.
2. Ingresa la cantidad de veces que deseas enviar el sticker.
3. Tienes 5 segundos para colocar el cursor sobre el sticker.
4. El script hará clic repetidamente sobre el sticker.

## Convertir en Ejecutable (.exe)
Si deseas usar el script sin necesidad de Python instalado, puedes convertirlo en un `.exe` con `PyInstaller`:
```sh
pip install pyinstaller
pyinstaller --onefile --noconsole script.py
```
El ejecutable se generará en la carpeta `dist/`.

## Precauciones
⚠ **Usa este script con responsabilidad.** Abusar del spam en WhatsApp podría generar restricciones en tu cuenta. Además, ten en cuenta que el uso de bots en juegos puede estar en contra de sus términos y condiciones.

## Contribuciones
Si quieres mejorar este proyecto, ¡eres bienvenido a contribuir! Puedes hacer un fork y enviar un pull request.

## Licencia
Este proyecto se distribuye bajo la licencia Creative Commons BY-NC.