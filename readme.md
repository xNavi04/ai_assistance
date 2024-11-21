# Rasa AI Assistant - Installation and Configuration Guide

## 3. **Environment Setup**

Before running the application, it is necessary to create a virtual environment and install all dependencies. Follow these steps:

### **Steps:**

1. **Install Miniconda (if not already installed):**
   - Miniconda is a lightweight version of Anaconda that allows package and environment management in Python. You can download Miniconda from the [official page](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions.

2. **Create a new virtual environment:**
   - Open a terminal and run the following command to create a new environment with the name `myenv` (you can replace `myenv` with any name you prefer):
     ```bash
     conda create --name myenv python=3.8
     ```
   - You can also install other versions of Python by changing `3.8` to the required version.

3. **Activate the environment:**
   - After creating the environment, activate it with the command:
     ```bash
     conda activate myenv
     ```

4. **Install all dependencies:**
   - Ensure you are in the active environment, then install the required packages. You can do this using the `requirements.txt` file, if it exists:
     ```bash
     pip install -r requirements.txt
     ```

5. **Type the appropriate command:**
   - Type in:
     ```bash
     rasa run
     ```

6**Deactivate the environment after finishing work:**
   - After you finish working in the environment, deactivate it with:
     ```bash
     conda deactivate
     ```

### **Benefits of Using Miniconda:**
- **Dependency Management:** Miniconda makes it easy to install and manage packages, eliminating dependency issues.
- **Environment Creation and Management:** You can easily create, activate, and deactivate different virtual environments, allowing for project separation.
- **Support for Different Python Versions:** You can have different Python versions installed in different environments.

Following these steps will ensure you are ready to work on your application in a well-configured environment!



# Dokumentacja API

## Endpoint `/webhook`

The `/webhook` endpoint is used to send a message from the user to the server, which then returns a formatted response that may include text, images, or videos.

### HTTP Method

- `POST`

### Request

#### URL

`/webhook`

#### Headers

- `Content-Type: application/json`

#### Request Body

The request body should be a JSON object containing the following properties:

- `message` (string): The message from the user to be sent to the server.
- `feedback` (string, optional): Information indicating whether the user rated the response positively or negatively.
##### Przykładowe żądanie

```json
POST /webhook
Content-Type: application/json

{
  "message": "Cześć, bot!"
}
```
lub

```json
POST /webhook
Content-Type: application/json

{
  "message": "Cześć, bot!", "feedback": "yes"
}
```

### Response

#### Response Body


The response body should be a JSON object containing the following properties:

- `type` (string, optional): The type of response (e.g. `text`, `image`, `video`).
- `text` (string, optional): The text to include in the response.
- `image` (string, optional): The path or URL to an image in the response.
- `video` (string, optional): The path or URL to a video in the response.
- `recipient_id` (string, optional): The recipient identifier (can be used to indicate to whom the response is directed).

##### Example Response

```json
[
   {
      'type': 'text', 
      'text': 'Aby włączyć odkurzacz, naciśnij przycisk włącz/wyłącz znajdujący się na urządzeniu.'
   }, 
   {
      'type': 'image', 
      'image': '/static/fig15.jpg'
   }, 
   {
      'type': 'text',
      'text': 'Tak jak jest zilustrowane na obrazku powyżej.'
   }
]
```
or

```json
[
{
   'recipient_id': 'default', 
   'text': 'Odkurzacz objęty jest gwarancją. W celu zgłoszenia usterki, skontaktuj się z autoryzowanym serwisem.'
}
]
```










# Rasa AI Assistant - Instrukcja instalacji i konfiguracji

## **Konfiguracja Środowiska**

Przed uruchomieniem aplikacji konieczne jest utworzenie wirtualnego środowiska i zainstalowanie wszystkich zależności. W tym celu należy postępować zgodnie z poniższymi krokami:

### **Kroki:**

1. **Zainstaluj Miniconda (jeśli jeszcze go nie masz):**
   - Miniconda to lekka wersja Anacondy, która pozwala na zarządzanie pakietami i środowiskami w Pythonie. Możesz pobrać Minicondę ze strony [oficjalnej](https://docs.conda.io/en/latest/miniconda.html) i postępować zgodnie z instrukcjami instalacji.

2. **Utwórz nowe środowisko wirtualne:**
   - Otwórz terminal i uruchom poniższe polecenie, aby utworzyć nowe środowisko z nazwą `myenv` (możesz zastąpić `myenv` dowolną nazwą):
     ```bash
     conda create --name myenv python=3.8
     ```
   - Możesz także zainstalować inne wersje Pythona, zmieniając `3.8` na wersję, której potrzebujesz.

3. **Aktywuj środowisko:**
   - Po utworzeniu środowiska, aktywuj je poleceniem:
     ```bash
     conda activate myenv
     ```

4. **Zainstaluj wszystkie zależności:**
   - Upewnij się, że znajdujesz się w aktywnym środowisku, a następnie zainstaluj potrzebne pakiety. Możesz to zrobić, korzystając z pliku `requirements.txt`, jeśli taki istnieje:
     ```bash
     pip install -r requirements.txt
     ```
     
5. **Wykonaj odpowiednie komendy, aby uruchomić REST API od RASA:**
   - Wpisz poniższą komendę:
     ```bash
     rasa run
     ```

6. **Zdezaktywuj środowisko po zakończeniu pracy:**
   - Po zakończeniu pracy w środowisku, możesz je dezaktywować:
     ```bash
     conda deactivate
     ```

### **Zalety korzystania z Minicondy:**
- **Zarządzanie zależnościami:** Miniconda ułatwia instalację i zarządzanie pakietami, eliminując problemy z zależnościami.
- **Tworzenie i zarządzanie środowiskami:** Możesz łatwo tworzyć, aktywować i dezaktywować różne środowiska wirtualne, co pozwala na separację projektów.
- **Wsparcie dla różnych wersji Pythona:** Możesz mieć różne wersje Pythona zainstalowane w różnych środowiskach.

Dzięki tym krokom będziesz gotowy do pracy nad swoją aplikacją w dobrze skonfigurowanym środowisku!

---

# Dokumentacja API

## Endpoint `/webhook`

Endpoint `/webhook` jest używany do przesyłania wiadomości od użytkownika do serwera, który następnie zwraca sformatowaną odpowiedź, która może zawierać tekst, obrazy i wideo.

### Metoda HTTP

- `POST`

### Żądanie

#### URL

`/webhook`

#### Nagłówki

- `Content-Type: application/json`

#### Treść żądania

Treść żądania powinna być obiektem JSON zawierającym następujące właściwości:

- `message` (string): Wiadomość od użytkownika, która ma być przesłana do serwera.
- `feedback` (string, nie występuje zawsze): Informacja, która zawiera, czy użytkonik ocenił odpowiedź pozytywnie lub negatywnie.
##### Przykładowe żądanie

```json
POST /webhook
Content-Type: application/json

{
  "message": "Cześć, bot!"
}
```
lub

```json
POST /webhook
Content-Type: application/json

{
  "message": "Cześć, bot!", "feedback": "yes"
}
```

### Odpowiedź

#### Treść odpowiedzi


Treść odpowiedzi powinna być obiektem JSON zawierającym następujące właściwości:

- `type` (string, nie występuje zawsze): Typ odpowiedzi (np. `text`, `image`, `video`).
- `text` (string, nie występuje zawsze): Tekst do umieszczenia w odpowiedzi.
- `image` (string, nie występuje zawsze): Ścieżka lub URL do obrazu w odpowiedzi.
- `video` (string, nie występuje zawsze): Ścieżka lub URL do wideo w odpowiedzi.
- `recipient_id` (string, nie występuje zawsze): Identyfikator odbiorcy (może być używany do wskazania, do kogo skierowana jest odpowiedź).

##### Przykładowa odpowiedź

```json
[
   {
      'type': 'text', 
      'text': 'Aby włączyć odkurzacz, naciśnij przycisk włącz/wyłącz znajdujący się na urządzeniu.'
   }, 
   {
      'type': 'image', 
      'image': '/static/fig15.jpg'
   }, 
   {
      'type': 'text',
      'text': 'Tak jak jest zilustrowane na obrazku powyżej.'
   }
]
```
lub 

```json
[
{
   'recipient_id': 'default', 
   'text': 'Odkurzacz objęty jest gwarancją. W celu zgłoszenia usterki, skontaktuj się z autoryzowanym serwisem.'
}
]
```
