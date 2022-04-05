<p align="center">
  <img src="https://github.com/TechLabs-Dortmund/wine-quality-prediction/blob/ux-design/design/Wine.png?raw=true" width="350" title="hover text">
</p>

# Vino Chance - find your perfect wine
As there is a overwhelming selection of different wines at supermarkets, a lack of knowledge and different tastes of wines, vino chance helps selecting the right wine for the right occasion. 
We help wine newcomers and enthusiasts with their selection, recommend the perfect wine fitting to their taste or depending on the dish they want to eat and help wine experts or those to-be to broaden their horizon. 


## How to Setup and Run

To get a local copy up and running, proceed as follows:

First you need to navigate into the ```backend``` directory to set up a ```virtual environment```, ```activate``` it and ```install``` all necessary packages: 

```bash
  #windows
  cd backend
  python -m venv venv
  venv/Scripts/activate
  pip install -r requirements.txt
```
```bash
  #macOS/Linux
  cd backend
  python3 -m venv venv
  venv/bin/acitvate
  pip3 install -r requirements.txt
```

Now use the following command to run the ```backend```:

```bash
  #windows
  python app.py
```
```bash
  #macOS/Linux
  python3 app.py
```
After successful installation and activation of the backend-part use the ```frontend``` directory to start the project:

```bash
  cd frontend
  npm install
  npm start
```
(note that you need two different terminals: one for the backend and one for the frontend-application)

# About the Project 

## Built with

- [ReactJs](https://reactjs.org/)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)


## Roadmap

- [x] find and clear suitable Dataset 
- [x] decide on a design 
- [x] built a wireframe
- [x] connect wine to food
- [x] write filters
- [x] built website 
- [x] built a backend structure
- [x] connect backend and frontend
- [x] implement a filter 
- [ ] implement all filters
- [ ] add QR-Code scanner
- [ ] implement a food-to-wine-recommendation-system based on a machine learning approach

  ...

Our full roadmap can be found on our [trelloboard](https://trello.com/b/xTmpwCmt/sprint-planning). 

## UX-Design 

You will find the Figma-Design for the Prototype and Wireframe [here](https://www.figma.com/file/T3KvUyKeOfTDaO2BfhJeCN/Vino-Chance?node-id=0%3A1). You find further information on the design process on our [mural](https://app.mural.co/t/techlabsglobal7643/m/techlabsglobal7643/1642006139698/e96378074736f92c197cee7de931f3bfe0a83c8e?sender=uefb7a45f031abd7b381e2509).

  
## Authors

- [@pauline](https://www.github.com/paulinemilia) 
- [@kathi](https://github.com/ihtaak)
- [@Anna](https://github.com/annoboe)
  

