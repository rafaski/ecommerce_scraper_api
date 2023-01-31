# E-commerce Scraper API
This application was built for educational purposes and is not intended 
for production use.

## Overview
This is a web scraper API that provides product information from supported 
e-commerce websites. Web crawlers run as `celery` tasks, parsed data is stored 
in `elasticsearch`. Results are sent to a callback url.

### Motives
The main reason for creating this application was to practice web scraping, 
explore `celery` and `elasticsearch`

Main features:
- FastAPI framework
- HTTP requests using `requests` library
- Data extraction with `beautifulsoup`
- Distributed task queuing with `celery`
- `redis` as a message broker for `celery` app
- data storage in `elasticsearch`
- scraping results sent to callback url, used `pipedream.com` for testing
- OOP where applicable
- testing with `pytest`

TODO:
- support more e-commerce websites

### Supported e-commerce websites:
`www.x-kom.pl`

## Get started
To run the API you will need connect to `elasticsearch`, we use `Elastic Cloud`.
Get your `Elastic Cloud` credentials, create the `.env` file 
(use the `.env.dist` for reference) and add the `ELASTICSEARCH_CLOUD_ID` and 
`ELASTICSEARCH_PASSWORD` variables.

### Authentication
To authenticate incoming requests, we check the `api_key` header.
Create the `.env` file (use the `.env.dist` for reference) 
and add `API_KEY` to environment variables.

### Dependencies
Dependency management is handled using `requirements.txt` file.

### Local setup
1. Install dependencies from `requirements.txt` file
2. Run redis server with `redis-cli`
3. Run celery worker with `celery -A app.celery_app worker -Q crawling --pool=solo --loglevel=INFO`
4. Run the app: `uvicorn app.main:app --reload`

## Documentation
Once the application is up and running, you can access FastAPI automatic docs 
at index page `/`

## Endpoints
| Method | Endpoint | Description                     |
|--------|----------|---------------------------------|
| GET    | /crawl   | Create a data scraping task     |


## Examples
### Hit API endpoint
```shell
curl -X 'GET' 'http://127.0.0.1:8080/crawl?url={XKOM_URL}&callback_url={CALLBACK_URL}' -H 'accept: application/json'
  ```

### API response
```json
{
  "success": true,
  "message": "Task accepted",
  "result": null
}
```
### Elasticsearch API console
```shell
GET /profiles-v2/_search
````
```json
{
  "hits": {
    "hits": [
      {
        "_score": 1,
        "_id": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja",
        "_source": {
          "review_count": 46,
          "name": "Apple MacBook Air M2/16GB/256/Mac OS Midnight",
          "average_rating": 5.91,
          "url": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja",
          "price": 6999,
          "currency": "zł",
          "reviews": [
            "Mam ten komp tylko z dyskiem 1TB, - to jest bestia. Używam do fullstack developmentu, masa apek, docker, jetbrains rider + webstorm, nodejs, .net core, teamsy, dsiesiątki tabów w chrome, parallels z win11 - żadnego problemu. CPU temp na poziomie 35 - 50C, przeważnie 35C, 50 osiąga przy indeksacji projektu albo ładowaniu win11 - wszystko jest mega szybkie. Tak powinien wyglądać sprzęt przyszłości. Nigdy więcej kompów z wiatrakami.... Rozwiń dalej",
            "Żona zadowolona a szczęśliwa kobieta to możliwość wyjścia z kumplami na piwo.... Rozwiń dalej",
            "Zacznę od minusów: dla kogoś kto od 25 lat korzystał wyłączanie z Windows to jest to \"kulturowy szok\". Żeby nie było, ja uwielbiam windowsa i uważam że jest to świetny system. Dlatego przyzwyczajenie się do MacOS zajmie dużo czasu. W okres adaptacji mocno spadnie efektywność pracy. Nie działają klasyczne skróty klawiszowe, przyzwyczajenia z Windows będą przeszkadzać w pracy. Po pewnym czasie jednak zaczyna być wygodniej. Do minusów należy też zaliczyć ograniczenia systemu (nie jest tak otwarty jak windrws). Teraz plusy: wygląd fenomenalny, bateria absolutnie genialna, kultura pracy dotychczas nieosiągalna nawet na naprawdę topowych maszynach z windows.... Rozwiń dalej",
            "Jak dla mnie to genialny sprzęt do lżejszej pracy i domowego użytku. Bateria wytrzymuje cały dzień bez ładowania. 8GB ramu też wystarcza do większości zadań domowych (obsługa kilkunastu zakładek w chromie, spotify, evernote, outlook).... Rozwiń dalej",
            "To mój pierwszy Mac, wcześniej windows, w tym wydajne maszyny biznesowe do pracy biurowej. Jakość wykonania na najwyższym poziomie, touchpad i klawiatura nie mają sobie równych. Klawisze mają przyjemny click, jest wyraźna \"podróż\" klawisza, ale te na thinkpadach chyba przyjemniejsze są. Płynność działania i performance na najwyższym poziomie, wszystko chodzi niesamowicie płynnie i znosi całkiem mocny multitasking. Nie testowałem jeszcze niczego bardziej wymagającego (rendering fotografii, Machine learning etc). Jeśli zastanawiasz się czy na pewno Mac to jest dobra droga, to po 2 tygodniach mówię zdecydowanie że tak. Wygląda niesamowicie, bateria starcza na bardzo długo - kilkanaście godzin bym powiedział. Jako całkliem power user, jeszcze jest pare rzeczy do których się muszę przyzwyczaić ale generalnie jest bajka. Super głośniki grają jak na tak małą obudowę, nawet nie wiedziałem, że to zwróci moją uwagę a są super wyważone, ofc mało basu, ale czego tu wymagać od laptopa który jest gruby na troch ponad centymetr.Z wad może si zdarzyć, że ten dysk będzie za mały, ale jeśli ma się dysk zewn i lubi korzystać z chmury to powinno być bez problemu. Ludzie co mówią, że są smugi i si ten kolor rysuje. Smugi zupełnie nie przeszkadzają, są łatwo zmywalne i serio to nie przeszkadza, chyba że dla jakichś pedantów. Ten kolor wygląda nieprawdopodobnie elegancko i nowocześnie. Ponoć po dłuższym czasie si rysuje i widać kolor aluminimum - nie wiem, po prostu kupiłem bardzo dobry pokrowiec i wkładam go podczas przenoszenia.... Rozwiń dalej",
            "Laptop jest super!... Rozwiń dalej",
            "W mojej opinii to bardzo dobrze wykonany sprzet. W mojej pracy wystarcza a czesto kompiluje programy. Nie odczuwam spadku mocy procka. Dla porównania pracuje też na macbook'u pro M1 32GB i kompilacja programów trwa w przybliżeniu tyle samo.... Rozwiń dalej",
            "Petarda jak dla mnie w tej konfiguracji przepaść techniczna do maca pro z 2017….kolor palcuje się... Rozwiń dalej",
            "Na ten moment bez zastrzeżeń, idealnie sprawdza się przy pracy biurowej oraz przy obróbce zdjęć/video - choć w przypadku tego drugiego po podłączeniu do monitora. Jedyny minus to strasznie uciążliwe ślady palców przy tym kolorze Maca.... Rozwiń dalej",
            "Miałem wielkie szczęście, że mój MacBook z poszukiwaną specyfikacją był już w moim miejskim sklepie. Zamówiłem w sobotę rano - i w sobotę przy obiedzie dostalem SMSa ze Mackbook gotowy do odbioru.No i jak to zawsze z Apple - bardzo dobrze i bezpiecznie zapakowane. Unboxing laptopa to tez bardzo przyjemna rzecz, nie było żadnych wad.Dzięki X-KOM za dobrą i szybką obsługę.... Rozwiń dalej",
            "Świetny ultrabook, który w zasadzie zastąpił mi na co dzień mocną stacjonarkę we wszystkich zastosowaniach poza najnowszymi grami. Do 15 godzin pracy na baterii, jasna matryca, piękna metalowa obudowa, klawiatura wygodna jak żadna inna. W związku z powyższym oprócz niszowych zastosowań typu programowanie w stacku Microsoftu przestaję widzieć jakikolwiek sens istnienia dla laptopów na Windowsie (nawet tych droższych).... Rozwiń dalej",
            "To jest fajna maszyna... Rozwiń dalej",
            "Pobiera 5W, by wykonać tą samą pracę co PC metr obok, z Ryzenem 7 3700X.Jeżeli komuś potrzeba procesora z dobrym IPC pod software typu NodeJS, czy nawet w C#, który nie wyssie życia z baterii, to Intel/AMD w tym świetle zaczynają tracić na wartości.... Rozwiń dalej",
            "Super sprzęt , w brew temu co sugerował sprzedawca nie nagrzewa się i nie zwróciłem go :)... Rozwiń dalej",
            "FAJNY SPRZĘT... Rozwiń dalej"
          ]
        }
      }
    ]
  }
}
```
### Pipedream callback payload
`HTTP POST`
```json
{
  "body": {
    "average_rating": 5.91,
    "currency": "zł",
    "name": "Apple MacBook Air M2/16GB/256/Mac OS Midnight",
    "price": 6999,
    "review_count": 46,
    "reviews": [
            "Mam ten komp tylko z dyskiem 1TB, - to jest bestia. Używam do fullstack developmentu, masa apek, docker, jetbrains rider + webstorm, nodejs, .net core, teamsy, dsiesiątki tabów w chrome, parallels z win11 - żadnego problemu. CPU temp na poziomie 35 - 50C, przeważnie 35C, 50 osiąga przy indeksacji projektu albo ładowaniu win11 - wszystko jest mega szybkie. Tak powinien wyglądać sprzęt przyszłości. Nigdy więcej kompów z wiatrakami.... Rozwiń dalej",
            "Żona zadowolona a szczęśliwa kobieta to możliwość wyjścia z kumplami na piwo.... Rozwiń dalej",
            "Zacznę od minusów: dla kogoś kto od 25 lat korzystał wyłączanie z Windows to jest to \"kulturowy szok\". Żeby nie było, ja uwielbiam windowsa i uważam że jest to świetny system. Dlatego przyzwyczajenie się do MacOS zajmie dużo czasu. W okres adaptacji mocno spadnie efektywność pracy. Nie działają klasyczne skróty klawiszowe, przyzwyczajenia z Windows będą przeszkadzać w pracy. Po pewnym czasie jednak zaczyna być wygodniej. Do minusów należy też zaliczyć ograniczenia systemu (nie jest tak otwarty jak windrws). Teraz plusy: wygląd fenomenalny, bateria absolutnie genialna, kultura pracy dotychczas nieosiągalna nawet na naprawdę topowych maszynach z windows.... Rozwiń dalej",
            "Jak dla mnie to genialny sprzęt do lżejszej pracy i domowego użytku. Bateria wytrzymuje cały dzień bez ładowania. 8GB ramu też wystarcza do większości zadań domowych (obsługa kilkunastu zakładek w chromie, spotify, evernote, outlook).... Rozwiń dalej",
            "To mój pierwszy Mac, wcześniej windows, w tym wydajne maszyny biznesowe do pracy biurowej. Jakość wykonania na najwyższym poziomie, touchpad i klawiatura nie mają sobie równych. Klawisze mają przyjemny click, jest wyraźna \"podróż\" klawisza, ale te na thinkpadach chyba przyjemniejsze są. Płynność działania i performance na najwyższym poziomie, wszystko chodzi niesamowicie płynnie i znosi całkiem mocny multitasking. Nie testowałem jeszcze niczego bardziej wymagającego (rendering fotografii, Machine learning etc). Jeśli zastanawiasz się czy na pewno Mac to jest dobra droga, to po 2 tygodniach mówię zdecydowanie że tak. Wygląda niesamowicie, bateria starcza na bardzo długo - kilkanaście godzin bym powiedział. Jako całkliem power user, jeszcze jest pare rzeczy do których się muszę przyzwyczaić ale generalnie jest bajka. Super głośniki grają jak na tak małą obudowę, nawet nie wiedziałem, że to zwróci moją uwagę a są super wyważone, ofc mało basu, ale czego tu wymagać od laptopa który jest gruby na troch ponad centymetr.Z wad może si zdarzyć, że ten dysk będzie za mały, ale jeśli ma się dysk zewn i lubi korzystać z chmury to powinno być bez problemu. Ludzie co mówią, że są smugi i si ten kolor rysuje. Smugi zupełnie nie przeszkadzają, są łatwo zmywalne i serio to nie przeszkadza, chyba że dla jakichś pedantów. Ten kolor wygląda nieprawdopodobnie elegancko i nowocześnie. Ponoć po dłuższym czasie si rysuje i widać kolor aluminimum - nie wiem, po prostu kupiłem bardzo dobry pokrowiec i wkładam go podczas przenoszenia.... Rozwiń dalej",
            "Laptop jest super!... Rozwiń dalej",
            "W mojej opinii to bardzo dobrze wykonany sprzet. W mojej pracy wystarcza a czesto kompiluje programy. Nie odczuwam spadku mocy procka. Dla porównania pracuje też na macbook'u pro M1 32GB i kompilacja programów trwa w przybliżeniu tyle samo.... Rozwiń dalej",
            "Petarda jak dla mnie w tej konfiguracji przepaść techniczna do maca pro z 2017….kolor palcuje się... Rozwiń dalej",
            "Na ten moment bez zastrzeżeń, idealnie sprawdza się przy pracy biurowej oraz przy obróbce zdjęć/video - choć w przypadku tego drugiego po podłączeniu do monitora. Jedyny minus to strasznie uciążliwe ślady palców przy tym kolorze Maca.... Rozwiń dalej",
            "Miałem wielkie szczęście, że mój MacBook z poszukiwaną specyfikacją był już w moim miejskim sklepie. Zamówiłem w sobotę rano - i w sobotę przy obiedzie dostalem SMSa ze Mackbook gotowy do odbioru.No i jak to zawsze z Apple - bardzo dobrze i bezpiecznie zapakowane. Unboxing laptopa to tez bardzo przyjemna rzecz, nie było żadnych wad.Dzięki X-KOM za dobrą i szybką obsługę.... Rozwiń dalej",
            "Świetny ultrabook, który w zasadzie zastąpił mi na co dzień mocną stacjonarkę we wszystkich zastosowaniach poza najnowszymi grami. Do 15 godzin pracy na baterii, jasna matryca, piękna metalowa obudowa, klawiatura wygodna jak żadna inna. W związku z powyższym oprócz niszowych zastosowań typu programowanie w stacku Microsoftu przestaję widzieć jakikolwiek sens istnienia dla laptopów na Windowsie (nawet tych droższych).... Rozwiń dalej",
            "To jest fajna maszyna... Rozwiń dalej",
            "Pobiera 5W, by wykonać tą samą pracę co PC metr obok, z Ryzenem 7 3700X.Jeżeli komuś potrzeba procesora z dobrym IPC pod software typu NodeJS, czy nawet w C#, który nie wyssie życia z baterii, to Intel/AMD w tym świetle zaczynają tracić na wartości.... Rozwiń dalej",
            "Super sprzęt , w brew temu co sugerował sprzedawca nie nagrzewa się i nie zwróciłem go :)... Rozwiń dalej",
            "FAJNY SPRZĘT... Rozwiń dalej"
    ],
    "url": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja"
  }
}
```