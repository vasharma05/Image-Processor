# Initial Setup

### `npm install`

Then Run

### `npm start`

along with the django's server ready alongside

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Working with the Live Chat

> * Open the project on an incognito window(Chrome) or a private window(Firefox), otherwise you won't be able to logout. I'm finding a solution to it.
> * Go to [localhost:3000](http://localhost:3000)
> * You will be redirected to signin page first. From there you can sign up or can login by the following credentials:
>
> username: vineet
>
> password: 1234

After signing in, you will see the landing page, where you can customize the chatbot according to your choice, change it on the left and can see the live changes on the right section.

If you go to the Dashboard( please ignore the Navbar, some work is still pending out there.

You will see a message box, with 2 tabs, left side shows the list of all consumers, and the right one will show all the messages. I would recommend you to first read the details in the backend, then proceed further.

When the page loads, it will load till the admin's websocket is connected, once connected it will show the above mentioned Chat box similar to Whatsapp Web.

Working:

* When the admin websocket is connected with the url ws://127.0.0.1:8000/ws/room/< username >, it sends a message to the with context:

{

command: 'fetch_rooms'

},

who's response is the list of all the rooms:

{

command: 'rooms',

rooms: [List of all the rooms]

}

Every room detail is of the format of

{
consumer: name of the consumer of that room,
messages: [An array of the messages]
}.

After all the fetching of the rooms is done, every room is then displayed on the left side of the panel, with the latest message in that particular room.

If a room has no messages in it, it won't be displayed in the list but will be connected to fetch new messages.

If a new room is made, when one opens the page described in the backend's readme, it will send the request to the server with the request as

{

command: 'new_room',

consumer: consumer name

}, which the server checks is it an old room, opened again or a new one. If it's a new one, then the server directs the response as

{

command:'new_room',

room: details of the room

}

where the detail of the room is of the format:

{
consumer: name of the consumer of that room,
messages: [An array of the messages]
}.

If it already exits, then no action is taken from the front end.

In the former case, the admin's websocket recieves the above request and then in the front end, it connects to the websocket of that consumer and but won't be displayed on the list till it get's a new message.

Clicking any item will open the chatbox on the right section with all the messages that will fetched from the consumer's websocket.

You can use it by opening the admin's chatbox on one window and the backend's chatbot on the other by filling up the correct details in the url as mentioned on the backend's README.

If a websocket disconnects, it will be notified on the webpage by a Snackbar and on reconnection it will again pop up with success notification. On disconnection, donot refresh the page, it will reconnect on its own.

This is the brief working on the frontend's side.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br/>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br/>
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br/>
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br/>
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br/>
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
