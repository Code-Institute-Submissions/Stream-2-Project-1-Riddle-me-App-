# Math's Riddle

A fun math riddle game. Very simple and straight forward. Customize it by adding as much questions you like.

[Demo](https://riddleapp.herokuapp.com/)


 
## UX
 
This game is created for  students who take interest in mathematics. 

- Users will play this game to enhance their cognitive ability to solve small riddles. 
- To compete with fellow students in the ability to solve simple math riddles.

It is interactive and fun to play.

## Features

- Ability to use images as well as text in questions.
- Leader board to show top performing users.
- Remembers the game state even if you close browser and come back to play.
- Show the last guess if the guess is incorrect.

 
### Existing Features

- All the features are implemented.

### Features Left to Implement
- All features are implemented.

## Technologies Used

This project uses HTML 5, CSS, and Bootstrap 4, Font Awesome, Google Fonts

## Testing

###Functionality

1. Start a New Game
- Go to Start New Game page
- Try to submit username field without any input
- Verify that a required field message pops up

2. Submit an Answer
- Go to question page after doing 1.
- Try to submit answer field without any input and verify that a required field message pops up.
- Try to enter any input except numbers and verify if the field allows it. Field should only only allow numeric input.


###Responsiveness

- Test the website
    - on mobile devices
    - on tablets
    - on desktop

and ensure maximum compatibility on Safari and Google Chrome.





## Deployment

Deployment to Heroku

- Create an App on Heroku after Sign up
- Install Heroku CLI
- Install Gunicorn (pip install gunicorn)
- Check dependencies and write them on requirements.txt (pip freeze > requirements.txt)
- Create a Procfile and specify Heroku to run gunicorn (web: gunicorn app:app)
- Now initialize a git repository in your project
- Add Heroku servers as remotes to git repository
- Commit all files and push to Heroku
- Test the app. 

## Credits
Riddles were copied from rd.com
